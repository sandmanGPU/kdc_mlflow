import os, sys

# # Determine the relative path to the 'src' directory from the script's location
# src_dir_relative = os.path.join(os.path.dirname(__file__), '../../..')

# # Convert the relative path to an absolute path
# src_dir_absolute = os.path.abspath(src_dir_relative)

# # Add the 'src' directory to the Python import path (sys.path)
# sys.path.append(src_dir_absolute)
# print(src_dir_absolute)
from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.data_ingestion import DataIngestion
from src.cnnClassifier import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ =='__main__':

    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e

