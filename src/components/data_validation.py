from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataValidationArtifactConfig, DataIngestionArtifactConfig
from scipy.stats import ks_2samp
from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.utils.utils import read_yaml_file, read_data, write_to_yaml


import os
import pandas as pd

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifactConfig, data_validation_config : DataValidationConfig):
        self.data_ingestion_artifact = data_ingestion_artifact
        self.data_validation_config = data_validation_config
        self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

    def validate_columns(self, dataframe: pd.DataFrame) -> bool:
         number_of_columns = len(self._schema_config)
         if len(dataframe.columns == number_of_columns):
             return True
         else:
             return False
    
    def check_numerical_columns(self, dataframe: pd.DataFrame) -> bool:
        for column_dict in self._schema_config['columns']:
            for column_name, datatype in column_dict.items():
                if str(dataframe[column_name].dtype) != datatype:
                    return False
        return True

    def check_data_drift(self, base_df, current_df, threshold = 0.05) -> bool:
        status = True
        report = {}

        for columns in base_df.columns:
            d1 = base_df[columns]
            d2 = current_df[columns]

            is_sample_dist = ks_2samp(d1, d2)
            if threshold <= is_sample_dist.pvalue:
                is_found = False
            else:
                is_found = True
                status = False
            report.update({
                columns:{
                    'p_value':float(is_sample_dist.pvalue),
                    'drift_status': is_found
                }
            })
        drift_report_file_path = self.data_validation_config.drift_report_file_path
        os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
        write_to_yaml(filepath = drift_report_file_path, content = report)

            
            
    def initiate_data_validation(self) -> DataValidationArtifactConfig:
        train_file_path = self.data_ingestion_artifact.train_path
        test_file_path = self.data_ingestion_artifact.test_path

        train_df = read_data(train_file_path)
        test_df = read_data(test_file_path)

        status = self.validate_columns(train_df)
        if not status:
            error_msg = f'Train dataframe does not contain all the columns.\n'
        status = self.validate_columns(test_df)
        if not status:
            error_msg = f'Test dataframe does not contain all the columns.\n'

        numeric_status = self.check_numerical_columns(train_df)
        if not numeric_status:
            error_msg = f'Train dataframe does not contain numerical columns.\n'
        
        numeric_status = self.check_numerical_columns(test_df)
        if not numeric_status:
            error_msg = f'Test dataframe does not contain numerical columns.\n'

        status = self.check_data_drift(base_df = train_df, current_df = test_df)
        dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
        os.makedirs(dir_path, exist_ok = True)

        train_df.to_csv(
            self.data_validation_config.valid_train_file_path, index = False, header = True
        )
        test_df.to_csv(
            self.data_validation_config.valid_test_file_path, index = False, header = True
        )

        data_validation_artifact = DataValidationArtifactConfig(
            validation_status = status,
            valid_train_file_path = self.data_ingestion_artifact.train_path,
            valid_test_file_path = self.data_ingestion_artifact.test_path,
            invalid_train_file_path = None,
            invalid_test_file_path = None,
            drift_report_file_path = self.data_validation_config.drift_report_file_path
        )
        return data_validation_artifact



        





