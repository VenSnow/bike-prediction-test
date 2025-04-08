from data_loader import load_data
from preprocessing import preprocess_data
from visualization import plot_age_distribution, plot_income_vs_bike
from model import train_model, predict
from evaluation import evaluate

from sklearn.model_selection import train_test_split

def main():
    # Load
    df = load_data()

    # Visualization
    plot_age_distribution(df)
    plot_income_vs_bike(df)

    # Preprocessing
    df = preprocess_data(df)
    x = df.drop('Purchased Bike_Yes', axis=1)
    y = df['Purchased Bike_Yes']

    # Separation
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Model
    model = train_model(x_train, y_train)

    # Prediction
    y_pred = predict(model, x_test)
    evaluate(y_test, y_pred)

if __name__ == '__main__':
    main()