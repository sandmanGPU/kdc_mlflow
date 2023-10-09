import os
import zipfile
import gdown
from src.cnnClassifier import logger
from src.cnnClassifier.utils.common import get_size
from src.cnnClassifier.entity.config_entity import DataIngestionConfig
# from src.cnnClassifier.config.configuration import ConfigurationManager
class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config=config

    def download_file(self)->str:
        '''
        Fetch data from url
        '''

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            if os.path.isdir(self.config.unzip_dir):
                logger.info(f"Dataset already exists. Skipping download")
            else:
                logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

                file_id = dataset_url.split("/")[-2]
                prefix = 'https://drive.google.com/uc?/export=download&id='
                gdown.download(prefix+file_id,zip_download_dir)

                logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e

    def extract_zip_file(self):
        '''
        zip_file_path: str
        Extracts the zip file into the data dir
        returns none
        '''
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)


# try:
#     config = ConfigurationManager()
#     data_ingestion_config = config.get_data_ingestion_config()
#     data_ingestion = DataIngestion(config=data_ingestion_config)
#     data_ingestion.download_file()
#     data_ingestion.extract_zip_file()
# except Exception as e:
#     raise e