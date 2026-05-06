from src.dsproject.config.configuration import ConfigurationManager
from src.dsproject.components.model_trainer import ModelTrainer
from src.dsproject import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        try:
            logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
            config_manager = ConfigurationManager()
            model_trainer_config = config_manager.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train_model()
            logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
        except Exception as e:
            logger.exception(f"An error occurred during {STAGE_NAME}: {e}")

if __name__ == "__main__":
    pipeline = ModelTrainingPipeline()
    pipeline.initiate_model_training()

