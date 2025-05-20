from src.constant.training_pipeline import MODEL_TRAINER_BEST_TRAINED_MODEL_FILE_NAME
import os

class NetworkModel:
    def __init__(self, preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model


    def predict(self, x):
        x_transform = self.preprocessor.transform(x)
        y_pred = self.model.predict(x_transform)
        return y_pred