# file: src/indicators.py

import pandas as pd
import pandas_ta as ta

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Adds a standard set of technical indicators to the DataFrame."""
    # Moving Averages for our strategy
    df.ta.sma(length=50, append=True, col_names=('SMA_50',))
    df.ta.sma(length=200, append=True, col_names=('SMA_200',))

    # Other useful indicators for future analysis
    df.ta.rsi(length=14, append=True, col_names=('RSI_14',))
    df.ta.macd(fast=12, slow=26, signal=9, append=True)

    # Drop rows with NaN values created by indicators
    df.dropna(inplace=True)
    return df