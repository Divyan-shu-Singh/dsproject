
import pandas as pd
import mlflow
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np
import joblib
from urllib.parse import urlparse
from pathlib import Path
from src.dsproject.utils.common import save_json
from sklearn.metrics import mean_squared_error
from src.dsproject.entity.config_entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self, actual, predicted):
        rmse = np.sqrt(mean_squared_error(actual, predicted))
        r2 = r2_score(actual, predicted)
        mae = mean_absolute_error(actual, predicted)
        return rmse, r2, mae

    def log_metrics_to_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_X = test_data.drop(columns=[self.config.target_column])
        test_y = test_data[self.config.target_column]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted = model.predict(test_X)
            rmse, r2, mae = self.evaluate_model(test_y, predicted)

            scores = {
                "rmse": rmse,
                "r2": r2,
                "mae": mae
            }

            save_json(path = Path(self.config.metric_file_name), data = scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

        if tracking_url_type_store != "file":
            mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNetModel")
        else:
            mlflow.sklearn.log_model(model, "model")

