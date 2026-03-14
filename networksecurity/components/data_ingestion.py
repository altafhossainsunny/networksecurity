from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

##Configuration for data ingestion config
from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os, sys
import pymongo
import pandas as pd
import numpy as np
from typing import List
from sklearn.model_selection import train_test_split

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URI")


class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

    ##Exporting collection data as dataframe from mongodb
    def export_collection_as_dataframe(self, collection_name:str, database_name:str) -> pd.DataFrame:

        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            collection_name = self.mongo_client[database_name][collection_name]

            dataframe = pd.DataFrame(list(collection_name.find()))
            if dataframe.empty:
                raise ValueError(
                    f"No data found in MongoDB collection '{self.data_ingestion_config.collection_name}' "
                    f"in database '{self.data_ingestion_config.database_name}'. "
                    "Please ensure the collection has been populated before running the pipeline."
                )
            if "_id" in dataframe.columns:
                dataframe = dataframe.drop(columns=["_id"])
            dataframe.replace({"null": np.nan}, inplace=True)
            logging.info(f"Fetched {len(dataframe)} records from MongoDB.")
            return dataframe
        

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
    def export_data_into_feature_store(self, dataframe:pd.DataFrame):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            #Creating directory
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path, exist_ok=True)
            dataframe.to_csv(feature_store_file_path, index=False, header=True)
            return dataframe
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    

    
    def split_data_as_train_test(self, dataframe:pd.DataFrame):
        try:
            train_set, test_set = train_test_split(
                dataframe,
                test_size=1 - self.data_ingestion_config.train_test_split_ratio,
                random_state=42
            )
            logging.info("Performed train test split on the data")

            dir_path = os.path.dirname(self.data_ingestion_config.training_data_dir)
            os.makedirs(dir_path, exist_ok=True)
            logging.info("Exporting train and test file path.")

            train_set.to_csv(self.data_ingestion_config.training_data_dir, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.testing_data_dir, index=False, header=True)
            logging.info("Exported train and test file path.")

        except Exception as e:
            raise NetworkSecurityException(e, sys)


    def initiate_data_ingestion(self):
        try:
            dataframe = self.export_collection_as_dataframe(
                collection_name=self.data_ingestion_config.collection_name,
                database_name=self.data_ingestion_config.database_name
            )
            dataframe = self.export_data_into_feature_store(dataframe)
            self.split_data_as_train_test(dataframe)
            dataingestionartifact = DataIngestionArtifact(
                trained_file_path=self.data_ingestion_config.training_data_dir,
                test_file_path=self.data_ingestion_config.testing_data_dir
            )
            return dataingestionartifact

        except Exception as e:
            raise NetworkSecurityException(e, sys)