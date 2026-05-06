import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    # convert labels to numbers
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})

    # remove missing values
    df = df.dropna()

    return df