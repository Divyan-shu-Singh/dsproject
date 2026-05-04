from src.dsproject.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.dsproject.utils.common import read_yaml, create_directories
import urllib.request as requests
import zipfile
import os
from src.dsproject import logger
from pathlib import Path
from src.dsproject.entity.config_entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(self, config_file_path: Path = CONFIG_FILE_PATH, 
                 params_file_path: Path = PARAMS_FILE_PATH,
                 schema_file_path: Path = SCHEMA_FILE_PATH):
        
        self.config_info = read_yaml(config_file_path)
        self.params_info = read_yaml(params_file_path)
        self.schema_info = read_yaml(schema_file_path)

        create_directories([self.config_info.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_info.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )
        
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config_info.data_validation
        schema = self.schema_info.COLUMNS
        
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            unzip_data_dir = config.unzip_data_dir,
            all_schema = schema
        )
        return data_validation_config
    
