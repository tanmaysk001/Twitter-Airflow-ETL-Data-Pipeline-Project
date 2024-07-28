import pandas as pd

def transform_data(df):
    df['text'] = df['text'].str.replace(r'http\S+|www.\S+', '', case=False)  # Remove URLs
    df['text'] = df['text'].str.replace(r'@\w+', '')  # Remove mentions
    df['text'] = df['text'].str.replace(r'#', '')  # Remove hashtags
    return df
