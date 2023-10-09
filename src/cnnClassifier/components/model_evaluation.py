import os
os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/sandmanGPU/kdc_mlflow.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="sandmanGPU"
os.environ['MLFLOW_TRACKING_PASSWORD']="170fae55eed33119e40cf121df270c286e09c95f"

import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from src.cnnClassifier.utils.common import save_json

from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.entity.config_entity import EvaluationConfig
from src.cnnClassifier import logger

# model = tf.keras.models.load_model("artifacts/training/model.h5")

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def evaluation(self):
        self.model = self.load_model(self.config.path_to_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store=urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy":self.score[1]}
            )

            if tracking_url_type_store != "file":

                mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16model")
            else:
                mlflow.keras.log_model(self.model, "model")


try:
    config= ConfigurationManager()
    eval_config=config.get_evaluation_config()
    evaluation=Evaluation(eval_config)
    evaluation.evaluation()
    evaluation.log_into_mlflow()

except Exception as e:
    raise e
    