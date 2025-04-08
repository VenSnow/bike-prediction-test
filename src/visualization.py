# Visualisation: Graphic for data analyze
import seaborn
from matplotlib import pyplot

def plot_age_distribution(df):
    seaborn.histplot(df['Age'], kde=True)
    pyplot.title('Age distribution')
    pyplot.show()

def plot_income_vs_bike(df):
    if 'Purchased Bike' in df.columns:
        seaborn.boxplot(x='Purchased Bike', y='Income', data=df)
        pyplot.title("Income VS Bike Purchase")
        pyplot.show()