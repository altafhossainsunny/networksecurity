import os
import sys
import json
import certifi
import numpy as np
import pandas as pd
import pymongo

#My packages
from networksecurity.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from dotenv import load_dotenv

load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URI")
#print(MONGODB_URL)

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def csv_to_json_converter(self, csv_file_path:str, json_file_path:str):
        try:
            df = pd.read_csv(csv_file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def insert_data_to_mongodb(self, records: list, database:str, collection: str):
        try:
            self.database = database
            self.records = records
            self.mongo_client = pymongo.MongoClient(MONGODB_URL, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[collection]
            self.collection.drop()  # clear existing data before re-inserting
            self.collection.insert_many(self.records)
            return len(self.records)

        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    
if __name__== "__main__":
    FILE_PATH = r"C:\Users\Public\NetworkSecurity\Network_Data\phisingData.csv"
    DATABASE ="ALTAF"
    COLLECTION = "NetworkData"
    obj = NetworkDataExtract()

    logging.info("Data conversion has started")

    record = obj.csv_to_json_converter(FILE_PATH, "phishingData.json")
    print(f"Number of records converted: {len(record)}")

    no_of_records = obj.insert_data_to_mongodb(record, DATABASE, COLLECTION)
    print(f"Number of records inserted: {no_of_records}")

    logging.info("Data insertion process started")

    number_of_records=obj.insert_data_to_mongodb(record, DATABASE, COLLECTION)
    print(f"Number of records inserted: {number_of_records}")