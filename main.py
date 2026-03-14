from networksecurity.components import data_validation
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys, os

if __name__ == "__main__":
    try:
        logging.info("Starting the data ingestion process.")
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion process completed successfully.")

        logging.info("Starting the data validation process.")
        data_validation_config = DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Data validation process completed successfully.")
        logging.info("Initiating data validation")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation process completed successfully.")

    except Exception as e:
        logging.error(f"Error occurred while initiating data ingestion: {e}")
        raise NetworkSecurityException(e, sys)