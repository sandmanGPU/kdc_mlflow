import os
os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/sandmanGPU/kdc_mlflow.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="sandmanGPU"
os.environ['MLFLOW_TRACKING_PASSWORD']="170fae55eed33119e40cf121df270c286e09c95f"

from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_based_model import PrepareBaseModelPipeline
from src.cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from src.cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"
try:
    logger.info(f"****************************************")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX-------------------------------------------------X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f"==========================================")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj=ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX==============================X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation"
try:
    logger.info(f"==========================================")
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj=EvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nX==============================X")
except Exception as e:
    logger.exception(e)
    raise e


