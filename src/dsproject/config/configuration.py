from src.dsproject.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.dsproject.utils.common import read_yaml, create_directories
import urllib.request as requests
import zipfile
import os
from src.dsproject import logger
from pathlib import Path
from src.dsproject.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig

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
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        data_transformation_config = self.config_info.data_transformation
        create_directories([data_transformation_config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir = data_transformation_config.root_dir,
            data_path = data_transformation_config.data_path
        )
        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        model_trainer_config = self.config_info.model_trainer
        params = self.params_info.ElasticNet
        schema = self.schema_info.TARGET_COLUMN

        return ModelTrainerConfig(
            root_dir=Path(model_trainer_config.root_dir),
            train_data_path=Path(model_trainer_config.train_data_path),
            test_data_path=Path(model_trainer_config.test_data_path),
            model_name=model_trainer_config.model_name,
            alpha=params.alpha,
            l1_ratio=params.l1_ratio,
            target_column=schema
        )
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        model_evaluation_config = self.config_info.model_evaluation
        params = self.params_info.ElasticNet
        schema = self.schema_info.TARGET_COLUMN

        model_evaluation_config_dir = Path(model_evaluation_config.root_dir)
        create_directories([model_evaluation_config_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=model_evaluation_config_dir,
            model_path=Path(model_evaluation_config.model_path),
            test_data_path=Path(model_evaluation_config.test_data_path),
            metric_file_name=Path(model_evaluation_config.metric_file_name),
            all_params= params,
            target_column= schema.name,
            mlflow_uri=os.getenv("MLFLOW_URI")
        )

        return model_evaluation_config
