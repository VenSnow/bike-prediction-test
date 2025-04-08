# Preprocessing: delete unnecessary and one-hot encoding
import pandas

def preprocess_data(df):
    df = df.drop(columns=['CustomerID'], errors='ignore') # Delete ID if it set
    return pandas.get_dummies(df, drop_first=True)