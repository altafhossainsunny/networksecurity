from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.entity.config_entity import DataIngestionConfig
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
        print(dataingestionartifact)

    except Exception as e:
        logging.error(f"Error occurred while initiating data ingestion: {e}")
        raise NetworkSecurityException(e, sys)