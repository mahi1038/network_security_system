from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig, DataTransformationConfig
from src.entity.config_entity import ModelTrainerConfig
from datetime import datetime

if __name__ == '__main__':
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config)
    data_ingestion = DataIngestion(data_ingestion_config)
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    print("successfully implemented data ingestion")

    data_validation_config = DataValidationConfig(training_pipeline_config)
    data_validation = DataValidation(data_ingestion_artifact, data_validation_config)
    data_validation_artifact = data_validation.initiate_data_validation()
    print("successfully completed data validation")

    data_transformation_config = DataTransformationConfig(training_pipeline_config)
    data_tranformation = DataTransformation(data_validation_artifact, data_transformation_config)
    data_transformation_artifact = data_tranformation.initiate_data_transformation()
    print('successfully completed data transfomation')

    model_trainer_config = ModelTrainerConfig(training_pipeline_config)
    model_trainer = ModelTrainer(model_trainer_config, data_transformation_artifact)
    model_trainer_artifact = model_trainer.initiate_model_trainer()
    print("successfully completed model trainer")
    print(model_trainer_artifact.test_metric_artifact.f1_score)
    print(model_trainer_artifact.test_metric_artifact.precision_score)
    print(model_trainer_artifact.test_metric_artifact.recall_score)
