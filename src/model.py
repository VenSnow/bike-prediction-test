# Model and prediction
from sklearn.ensemble import RandomForestClassifier

def train_model(x_train, y_train):
    model = RandomForestClassifier()
    model.fit(x_train, y_train)
    return model

def predict(model: RandomForestClassifier, x_test):
    return model.predict(x_test)