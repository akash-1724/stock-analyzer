# file: src/data_processor.py

import pandas as pd

def process_to_dataframe(candles_data):
    """Converts raw candle data into a clean pandas DataFrame."""
    if not candles_data:
        return pd.DataFrame()

    # Define column names as per Upstox API response structure
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'open_interest']
    df = pd.DataFrame(candles_data, columns=columns)

    # --- Data Cleaning and Formatting ---
    # Convert timestamp to a readable datetime format and set as index
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.set_index('timestamp', inplace=True)

    # Convert relevant columns to numeric types
    for col in ['open', 'high', 'low', 'close', 'volume']:
        df[col] = pd.to_numeric(df[col])

    # Reverse the DataFrame to have the oldest date first
    df = df.iloc[::-1]

    return df