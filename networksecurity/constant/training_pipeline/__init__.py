import os
import sys
import numpy as np
import pandas as pd

"""
Data Ingestion related constant start with DATA_INGESTION_VAR_NAME
"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "ALTAF"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATION: float = 0.3

"""
Defining common constant variable for the training pipeline
"""
TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "ArtifactS"
FILE_NAME: str = "NetworkData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Data Validation related constant start with DATA_VALIDATION_VAR_NAME
"""

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

SCHEMA_FILE_PATH: str = os.path.join("data_schema", "schema.yml")