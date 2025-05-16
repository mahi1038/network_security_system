import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline
from src.constant.training_pipeline import TARGET_COLUMN, DATA_TRANSFORMATION_IMPUTER_PARAMS
from src.entity.config_entity import DataTransformationConfig
from src.entity.artifact_entity import DataTransformationArtifactConfig, DataValidationArtifactConfig
from src.utils.utils import save_numpy_array_data, save_object_pkl, read_data


class DataTransformation:
    def __init__(self, data_validation_artifact_config: DataValidationArtifactConfig, data_transformation_config: DataTransformationConfig):
        self.data_validation_artifact_config = data_validation_artifact_config
        self.data_transformation_config = data_transformation_config

    def get_preprocessor_obj(self, cls) -> Pipeline:
        """
        Args:
        cls: DataTransformer
        """
        


    def initiate_data_transformation(self) -> DataTransformationArtifactConfig:
        train_df = read_data(self.data_validation_artifact_config.valid_train_file_path)
        test_df = read_data(self.data_validation_artifact_config.valid_test_file_path)

        X_train_df = train_df.drop(columns = [TARGET_COLUMN], axis = 1)
        y_train_df = train_df[TARGET_COLUMN]
        y_train_df.replace(-1, 0, inplace=True)

        X_test_df = test_df.drop(column = [TARGET_COLUMN], axis = 1)
        y_test_df = test_df[TARGET_COLUMN]
        y_test_df.replace(-1, 0, inplace=True)

        
