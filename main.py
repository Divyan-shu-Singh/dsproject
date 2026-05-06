from src.dsproject import logger
from src.dsproject.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.dsproject.pipeline.data_validation_pipeline import DataValidationPipeline
from src.dsproject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.dsproject.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.dsproject.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

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

    try:
        logger.info("Starting the data transformation pipeline.")
        transformation_pipeline = DataTransformationTrainingPipeline()
        transformation_pipeline.initiate_data_transformation()
        logger.info("Data transformation pipeline completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred in the main execution: {e}")

    try:
        logger.info("Starting the model training pipeline.")
        model_training_pipeline = ModelTrainingPipeline()
        model_training_pipeline.initiate_model_training()
        logger.info("Model training pipeline completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred in the main execution: {e}")

    try:
        logger.info("Starting the model evaluation pipeline.")
        model_evaluation_pipeline = ModelEvaluationPipeline()
        model_evaluation_pipeline.initiate_model_evaluation()
        logger.info("Model evaluation pipeline completed successfully.")
    except Exception as e:
        logger.exception(f"An error occurred in the main execution: {e}")

        

    