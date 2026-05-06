from src.dsproject import logger
from src.dsproject.entity.config_entity import ModelTrainerConfig
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train_model(self):
        logger.info("Loading training data...")
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        X_train = train_data.drop(columns=[self.config.target_column.name])
        y_train = train_data[self.config.target_column.name]
        X_test = test_data.drop(columns=[self.config.target_column.name])
        y_test = test_data[self.config.target_column.name]

        logger.info("Training the ElasticNet model...")
        model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        model.fit(X_train, y_train)

        model_path = self.config.root_dir / self.config.model_name
        model_path.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, model_path)
        logger.info(f"Model saved at {model_path}")
