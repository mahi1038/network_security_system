class DataIngestionArtifactConfig:
    def __init__(self, train_path, test_path):
        self.train_path = train_path
        self.test_path = test_path

class DataValidationArtifactConfig:
    def __init__(self, validation_status: bool,
                 valid_train_file_path: str,
                 valid_test_file_path: str,
                 invalid_train_file_path: str,
                 invalid_test_file_path: str,
                 drift_report_file_path: str,):
        self.validation_status = validation_status
        self.valid_train_file_path = valid_train_file_path
        self.valid_test_file_path = valid_test_file_path
        self.invalid_train_file_path = invalid_train_file_path
        self.invalid_test_file_path = invalid_test_file_path
        self.drift_report_file_path = drift_report_file_path

class DataTransformationArtifactConfig:
    def __init__(self, transformed_train_file_path: str,
                 transformed_test_file_path: str,
                 transformed_object_file_path: str):
        self.transformed_train_file_path = transformed_train_file_path
        self.transformed_test_file_path = transformed_test_file_path
        self.transformed_object_file_path = transformed_object_file_path
    