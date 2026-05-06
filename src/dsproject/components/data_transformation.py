import os
from sklearn.model_selection import train_test_split
from src.dsproject import logger
from src.dsproject.entity.config_entity import DataTransformationConfig
import pandas as pd

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def train_test_split(self):
        try:
            logger.info("Starting data transformation...")
            df = pd.read_csv(self.config.data_path)
            logger.info(f"Data loaded successfully from {self.config.data_path}")
            
            # Example transformation: splitting data into train and test sets
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
            logger.info("Data split into train and test sets successfully.")
            
            # Save transformed data
            train_df.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
            test_df.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

            logger.info(f"Transformed data saved to {self.config.root_dir}")
        except Exception as e:
            logger.exception(f"An error occurred during data transformation: {e}")