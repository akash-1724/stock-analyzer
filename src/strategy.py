# file: src/strategy.py

import pandas as pd
import numpy as np

def generate_signals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generates trading signals based on the Golden Cross strategy.
    - BUY (1): When the short-term SMA (50) crosses above the long-term SMA (200).
    - SELL (-1): When the short-term SMA (50) crosses below the long-term SMA (200).
    - HOLD (0): Otherwise.
    """
    signals = pd.DataFrame(index=df.index)
    signals['price'] = df['close']
    signals['signal'] = 0

    # The 'position' helps identify the exact crossover point
    # Position is 1 when SMA_50 > SMA_200, and -1 when SMA_50 < SMA_200
    signals['position'] = np.where(df['SMA_50'] > df['SMA_200'], 1, -1)

    # The signal is the difference in position from the previous day
    # A change from -1 to 1 is a Buy signal (diff = 2, so we mark it as 1)
    # A change from 1 to -1 is a Sell signal (diff = -2, so we mark it as -1)
    signals['signal'] = signals['position'].diff().apply(lambda x: 1 if x > 1 else (-1 if x < -1 else 0))

    return signals