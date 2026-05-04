from src.dsproject import logger
from src.dsproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.dsproject.pipeline.data_validation_pipeline import DataValidationPipeline

if __name__ == "__main__":
    try:
        logger.info("Starting the data ingestion pipeline.")
        pipeline = DataIngestionTrainingPipeline()
        pipeline.initiate_data_ingestion()
        logger.info("Data ingestion pipeline completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred in the main execution: {e}")
    
    try:
        logger.info("Starting the data validation pipeline.")
        validation_pipeline = DataValidationPipeline()
        validation_pipeline.initiate_data_validation()
        logger.info("Data validation pipeline completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred in the main execution: {e}")

        

    