# Model Evaluation
from sklearn.metrics import accuracy_score, classification_report

def evaluate(y_test, y_pred):
    print("Accuracy: ", accuracy_score(y_test, y_pred))
    print("Report:\n", classification_report(y_test, y_pred))