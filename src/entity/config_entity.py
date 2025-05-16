from datetime import datetime
import os
from src.constant import training_pipeline

tp = training_pipeline
print(tp.PIPELINE_NAME)

class TrainingPipelineConfig:
    def __init__(self, timestamp = datetime.now()):
        timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.pipeline_name = tp.PIPELINE_NAME
        self.artifact_name = tp.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp

class DataIngestionConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, tp.DATA_INGESTION_DIR_NAME)
        self.train_path = os.path.join(self.data_ingestion_dir, tp.DATA_INGESTION_INGESTED_DIR, tp.TRAIN_FILE_NAME)
        self.test_path = os.path.join(self.data_ingestion_dir, tp.DATA_INGESTION_INGESTED_DIR,  tp.TEST_FILE_NAME)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir, tp.DATA_INGESTION_FEATURE_STORE_DIR, tp.FILE_NAME)
        self.train_test_ratio = float(tp.DATA_INGESTION_SPLIT_RATIO)
        self.collection_name = tp.DATA_INGESTION_COLLECTION_NAME
        self.database_name = tp.DATA_INGESTION_DATABASE_NAME


class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, tp.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir = os.path.join(self.data_validation_dir, tp.DATA_VALIDAITON_VALID_DIR_NAME)
        self.invalid_data_dir = os.path.join(self.data_validation_dir, tp.DATA_VALIDATION_INVALID_DIR_NAME)
        self.valid_train_file_path = os.path.join(self.valid_data_dir, tp.TRAIN_FILE_NAME)
        self.valid_test_file_path = os.path.join(self.valid_data_dir, tp.TEST_FILE_NAME)
        self.invalid_train_file_path = os.path.join(self.invalid_data_dir, tp.TRAIN_FILE_NAME)
        self.invalid_test_file_path = os.path.join(self.invalid_data_dir, tp.TEST_FILE_NAME)
        self.drift_report_file_path = os.path.join(self.data_validation_dir, tp.DATA_VALIDATION_DRIFT_REPORT_DIR_NAME, tp.DATA_VALIDATION_DRIFT_REPORT_NAME)

        
class DataTransformationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_transformation_dir = os.path.join(training_pipeline_config.artifact_dir, tp.DATA_TRANSFORMATION_DIR_NAME)
        self.transformed_train_file_path = os.path.join(self.data_transformation_dir, tp.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, tp.TRAIN_FILE_NAME.replace('csv', 'npy'))
        self.transformed_test_file_path = os.path.join(self.data_transformation_dir, tp.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR, tp.TEST_FILE_NAME.replace('csv', 'npy'))
        self.tranformed_object_file_path = os.path.join(self.data_transformation_dir, tp.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR, tp.PREPROCESSOR_OBJECT_FILE_NAME)



        
