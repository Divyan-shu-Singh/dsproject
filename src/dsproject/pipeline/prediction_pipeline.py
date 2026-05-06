import joblib
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
    def __init__(self, model_path: Path = Path("artifacts/model_trainer/model.joblib")):
        self.model = joblib.load(model_path)

    def predict(self, input_data: pd.DataFrame) -> np.ndarray:
        predictions = self.model.predict(input_data)
        return predictions