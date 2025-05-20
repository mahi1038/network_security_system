import os
import numpy as np
import pandas as pd

"""
Data ingestion variables start with DATA_INGESTION var name
"""

DATA_INGESTION_COLLECTION_NAME = "NetworkData"
DATA_INGESTION_DATABASE_NAME = "MAHIDB"
DATA_INGESTION_DIR_NAME = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
DATA_INGESTION_SPLIT_RATIO = 0.2

"""
variables for training pipeline
"""

TARGET_COLUMN = 'Result'
PIPELINE_NAME = 'NetworkSecurity'
ARTIFACT_DIR = "Artifacts"
FILE_NAME = 'phisingData.csv' 

TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")


"""
variables for data validation
"""

DATA_VALIDATION_DIR_NAME = "data_validation_dir"
DATA_VALIDAITON_VALID_DIR_NAME = 'valid_dir'
DATA_VALIDATION_INVALID_DIR_NAME = 'invalid_dir'
DATA_VALIDATION_DRIFT_REPORT_DIR_NAME = 'report_dir'
DATA_VALIDATION_DRIFT_REPORT_NAME = 'report.yaml'

"""
variables for data transformation
"""

DATA_TRANSFORMATION_DIR_NAME = 'data_transformation_dir'
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = 'tranformed'
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = 'transformed_object'
PREPROCESSOR_OBJECT_FILE_NAME = 'preprocessor.pkl'

DATA_TRANSFORMATION_IMPUTER_PARAMS: dict = {
    'missing_values': np.nan,
    'n_neighbors': 3,
    'weights': 'uniform'
}


"""
varaibles for model trainer
"""

MODEL_TRAINER_DIR_NAME = "model_trainer_dir"
MODEL_TRAINER_BEST_TRAINED_MODEL_FILE_NAME = "best_model.pkl"
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_TRHESHOLD = 0.05





