from src.dsproject.config.configuration import ConfiguartionManager
from src.dsproject.components.data_ingestion import DataIngestion
from src.dsproject import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            config_manager = ConfiguartionManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_data()
            data_ingestion.extract_zip_file()
        except Exception as e:
            logger.exception(f"An error occurred: {e}")

if __name__ == "__main__":
    pipeline = DataIngestionTrainingPipeline()
    pipeline.initiate_data_ingestion()
