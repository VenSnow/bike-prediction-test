# Load dataset
import pandas

def load_data(path='../data/bike_buyers.csv'):
    """ Return read csv """
    return pandas.read_csv(path)