# Training pipeline constants
import os

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yml")
TARGET_COLUMN = "Result"
DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    "missing_values": float("nan"),
    "n_neighbors": 3,
    "weights": "uniform",
}

DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_VALID_DIR = "validated"
DATA_VALIDATION_INVALID_DIR = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"

DATA_INGESTION_DATABASE_NAME = "ALTAF"
DATA_INGESTION_COLLECTION_NAME = "NetworkData"
DATA_INGESTED_TRAIN_TEST_SPLIT_RATION = 0.8
DATA_INGESTION_INGESTED_DIR = "ingested"
FILE_NAME = "phisingData.csv"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_DIR_NAME = "data_ingestion"
ARTIFACT_DIR = "ArtifactS"
PIPELINE_NAME = "network_security_pipeline"
PREPROCESSING_OBJECT_FILE_NAME = "preprocessor.pkl"
DATA_TRANSFORMATION_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed_data"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
MODEL_FILE_NAME = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD = 0.05
