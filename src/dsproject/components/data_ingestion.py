import os
import zipfile
import urllib.request as requests
from src.dsproject import logger
from src.dsproject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = requests.urlretrieve(url = self.config.source_URL, filename = self.config.local_data_file)
            logger.info(f"Data downloaded successfully from {self.config.source_URL} to {self.config.local_data_file}")

        else:
            logger.info(f"Data already exists at {self.config.local_data_file}. Skipping download.")

    def extract_zip_file(self):
        unzip_dir = self.config.unzip_dir
        if not os.path.exists(unzip_dir):
            os.makedirs(unzip_dir)
            
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
            logger.info(f"Data extracted successfully to {self.config.unzip_dir}")