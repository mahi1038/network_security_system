import numpy as np
import pandas as pd
import os
import mlflow

from src.entity.config_entity import DataTransformationConfig, ModelTrainerConfig
from src.entity.artifact_entity import DataTransformationArtifactConfig, ModelTrainerArtifactConfig, ClassificationMetricArtifact

from src.utils.utils import save_numpy_array_data, save_object_pkl, load_object
from src.utils.utils import load_numpy_array, read_data
from src.utils.ml_utils import get_classification_score, evaluate_model
from src.utils.estimator_utils import NetworkModel

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    RandomForestClassifier
)

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig, data_transformation_artifact: DataTransformationArtifactConfig):
        self.model_trainer_config = model_trainer_config
        self.data_tranform_artifact_config = data_transformation_artifact

    def track_mlflow(self, best_model: object, classification_train_metric: ClassificationMetricArtifact):
        with mlflow.start_run():
            f1_score = classification_train_metric.f1_score
            precision_score = classification_train_metric.precision_score
            recall_score = classification_train_metric.recall_score

            mlflow.log_metric('f1_score', f1_score)
            mlflow.log_metric('precision_score', precision_score)
            mlflow.log_metric('recall_score', recall_score)

            mlflow.sklearn.log_model(best_model,'model')



    def train_model(self, x_train, y_train, x_test, y_test):
        models = {
            'Random Forest': RandomForestClassifier(verbose = 1),
            'Decision Tree': DecisionTreeClassifier(),
            'Gradient Boosting': GradientBoostingClassifier(),
            'Logistic Regression': LogisticRegression(verbose = 1),
            'AdaBoost': AdaBoostClassifier()
        }

        model_report = evaluate_model(x_train, y_train, x_test, y_test, models)
        best_model_score = max(sorted(model_report.values()))

        best_model_name =list(model_report.keys())[list(model_report.values()).index(best_model_score)]

        best_model = models[best_model_name]

        save_object_pkl("final_model/model.pkl", best_model)

        y_train_pred = best_model.predict(x_train)
        y_test_pred = best_model.predict(x_test)

        classification_train_metric = get_classification_score(y_true = y_train, y_pred = y_train_pred)
        classification_test_metric = get_classification_score(y_true=y_test, y_pred=y_test_pred)

        ## use mlflow to track the experiments
        ## using classification_test_metric
        ## using classification_train_metric
        self.track_mlflow(best_model, classification_train_metric)

        preprocessor = load_object(filepath = self.data_tranform_artifact_config.transformed_object_file_path)

        model_dir_name = os.path.dirname(self.model_trainer_config.trained_model_file_path)
        os.makedirs(model_dir_name, exist_ok=True)

        network_model = NetworkModel(preprocessor, best_model)

        save_object_pkl(self.model_trainer_config.trained_model_file_path, network_model)

        model_trainer_artifact = ModelTrainerArtifactConfig(self.model_trainer_config.trained_model_file_path,
                                                            classification_train_metric,
                                                            classification_test_metric)
        
        return model_trainer_artifact

      


    def initiate_model_trainer(self) -> ModelTrainerArtifactConfig:
        train_file_path = self.data_tranform_artifact_config.transformed_train_file_path
        test_file_path = self.data_tranform_artifact_config.transformed_test_file_path

        train_arr = load_numpy_array(train_file_path)
        test_arr = load_numpy_array(test_file_path)

        x_train = train_arr[:, :-1]
        y_train = train_arr[:,-1]
        x_test = test_arr[:, :-1]
        y_test = test_arr[:,-1]
        print(f'{len(x_train)}, {len(y_train)}')

        model_trainer_artifact_config =  self.train_model(x_train, y_train, x_test, y_test)
        return model_trainer_artifact_config



        



