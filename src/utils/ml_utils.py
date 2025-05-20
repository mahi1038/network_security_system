from src.entity.artifact_entity import ClassificationMetricArtifact
from sklearn.metrics import f1_score, precision_score, recall_score, r2_score

def get_classification_score(y_true, y_pred) -> ClassificationMetricArtifact:
    model_f1_score = f1_score(y_true, y_pred)
    model_recall_score = recall_score(y_true, y_pred)
    model_precision_score = precision_score(y_true, y_pred)

    classification_metric = ClassificationMetricArtifact(model_f1_score, model_precision_score, model_recall_score)

    return classification_metric

from sklearn.metrics import r2_score

def evaluate_model(X_train, y_train, X_test, y_test, models: dict) -> dict:
    report = {}
    for name, model in models.items():
        model.fit(X_train, y_train)

        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)

        train_model_score = r2_score(y_train, y_train_pred)
        test_model_score = r2_score(y_test, y_test_pred)

        report[name] = test_model_score

    return report 

