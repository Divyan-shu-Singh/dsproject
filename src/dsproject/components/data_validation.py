import os
import zipfile
from src.dsproject import logger
from src.dsproject.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_data(self):
        try:
            if not os.path.exists(self.config.unzip_data_dir):
                raise FileNotFoundError(f"Unzipped data file not found at {self.config.unzip_data_dir}")
            
            df = pd.read_csv(self.config.unzip_data_dir)
            expected_columns = set(self.config.all_schema.keys())
            actual_columns = set(df.columns)

            if expected_columns != actual_columns:
                raise ValueError(f"Column mismatch. Expected: {expected_columns}, Actual: {actual_columns}")

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write("Data validation successful.")
            
            logger.info("Data validation completed successfully.")
        
        except Exception as e:
            logger.exception(f"Data validation failed: {e}")
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Data validation failed: {e}")