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

    def get_preprocessor_obj(self) -> Pipeline:
        """
        Args:
        cls: DataTransformer
        """
        imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS )

        pipeline = Pipeline([("imputer", imputer)])

        return pipeline

        


    def initiate_data_transformation(self) -> DataTransformationArtifactConfig:
        train_df = read_data(self.data_validation_artifact_config.valid_train_file_path)
        test_df = read_data(self.data_validation_artifact_config.valid_test_file_path)

        X_train_df = train_df.drop(columns = [TARGET_COLUMN], axis = 1)
        y_train_df = train_df[TARGET_COLUMN]
        y_train_df.replace(-1, 0, inplace=True)

        X_test_df = test_df.drop(columns = [TARGET_COLUMN], axis = 1)
        y_test_df = test_df[TARGET_COLUMN]
        y_test_df.replace(-1, 0, inplace=True)

        preprocessor_obj = self.get_preprocessor_obj()
        transformed_X_train = preprocessor_obj.fit(X_train_df)
        transformed_X_train = preprocessor_obj.transform(X_train_df)
        transformed_X_test = preprocessor_obj.transform(X_test_df)

        train_arr = np.c_[transformed_X_train, np.array(y_train_df)]
        test_arr = np.c_[transformed_X_test, np.array(y_test_df)]

        save_numpy_array_data(self.data_transformation_config.transformed_train_file_path, array=train_arr)
        save_numpy_array_data(self.data_transformation_config.transformed_test_file_path, array=test_arr)
        save_object_pkl(self.data_transformation_config.tranformed_object_file_path, obj=preprocessor_obj)

        save_object_pkl("final_model/preprocessor.pkl", preprocessor_obj)

        data_transformation_artifact_config = DataTransformationArtifactConfig(
            transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
            transformed_test_file_path=self.data_transformation_config.transformed_test_file_path,
            transformed_object_file_path=self.data_transformation_config.tranformed_object_file_path
        )

        return data_transformation_artifact_config


        
