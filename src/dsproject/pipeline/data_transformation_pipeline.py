from src.dsproject.config.configuration import ConfigurationManager
from src.dsproject.components.data_transformation import DataTransformation
from src.dsproject import logger

STAGE_NAME = "Data Transformation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        try:
            logger.info(f">>>>>>> Stage {STAGE_NAME} started <<<<<<<")
            config_manager = ConfigurationManager()
            data_transformation_config = config_manager.get_data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.train_test_split()
            logger.info(f">>>>>>> Stage {STAGE_NAME} completed <<<<<<<\n\n")
        except Exception as e:
            logger.exception(f"An error occurred during {STAGE_NAME}: {e}")

if __name__ == "__main__":
    pipeline = DataTransformationTrainingPipeline()
    pipeline.initiate_data_transformation()