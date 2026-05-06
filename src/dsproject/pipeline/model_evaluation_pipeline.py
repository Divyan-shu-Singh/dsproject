from src.dsproject.config.configuration import ConfigurationManager
from src.dsproject.components.model_validator import ModelEvaluation
from src.dsproject import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
            config_manager = ConfigurationManager()
            model_evaluation_config = config_manager.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config=model_evaluation_config)
            model_evaluation.log_metrics_to_mlflow()
            logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
        except Exception as e:
            logger.exception(f"An error occurred during {STAGE_NAME}: {e}")

if __name__ == "__main__":
    try:
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
    except Exception as e:
        logger.exception(f"An error occurred in the main execution: {e}")