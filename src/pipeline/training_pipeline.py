import os
import sys

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

from src.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataTransformationConfig,
    DataValidationConfig,
    ModelTrainerConfig
)

from src.entity.artifact_entity import (
    DataIngestionArtifactConfig,
    DataTransformationArtifactConfig,
    DataValidationArtifactConfig,
    ModelTrainerArtifactConfig
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        data_ingestion_config = DataIngestionConfig(self.training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        return data_ingestion_artifact
     
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifactConfig):
        data_validation_config = DataValidationConfig(self.training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)

        data_validation_artifact = data_validation.initiate_data_validation()
        return data_validation_artifact
    
    def start_data_transformation(self, data_validation_artifact: DataValidationArtifactConfig):
        data_transformation_config = DataTransformationConfig(self.training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact_config=data_validation_artifact, data_transformation_config=data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()

        return data_transformation_artifact
    
    def model_trainer(self, data_transformation_artifact: DataTransformationArtifactConfig):
        model_trainer_config = ModelTrainerConfig(self.training_pipeline_config)
        model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        return model_trainer_artifact
    
    def run_pipeline(self):
        data_ingestion_artifact = self.start_data_ingestion()
        data_validation_artifact = self.start_data_validation(data_ingestion_artifact)
        data_transformation_artifact = self.start_data_transformation(data_validation_artifact)
        model_trainer_artifact = self.model_trainer(data_transformation_artifact)
        
        return model_trainer_artifact




        

     