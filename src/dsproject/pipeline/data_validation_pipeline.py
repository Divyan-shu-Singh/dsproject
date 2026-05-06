from src.dsproject.config.configuration import ConfigurationManager
from src.dsproject.components.data_validation import DataValidation
from src.dsproject import logger

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        try:
            config_manager = ConfigurationManager()
            data_validation_config = config_manager.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            data_validation.validate_data()
        except Exception as e:
            logger.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    pipeline = DataValidationPipeline()
    pipeline.initiate_data_validation()
