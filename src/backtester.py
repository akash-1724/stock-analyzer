# file: src/backtester.py

import pandas as pd
import numpy as np

def run_backtest(signals: pd.DataFrame, initial_capital=100000.0):
    """Runs a vectorized backtest on the generated signals."""
    cash = initial_capital
    positions = pd.Series(index=signals.index).fillna(0.0)
    portfolio = pd.DataFrame(index=signals.index)
    portfolio['holdings'] = 0.0
    portfolio['cash'] = initial_capital

    for i in range(len(signals)):
        price = signals['price'].iloc[i]
        signal = signals['signal'].iloc[i]

        if signal == 1: # Buy signal
            if portfolio['cash'].iloc[i-1] > 0:
                positions.iloc[i] = portfolio['cash'].iloc[i-1] / price
                portfolio['cash'].iloc[i] = 0
            else: # Already in position, carry forward
                positions.iloc[i] = positions.iloc[i-1]
                portfolio['cash'].iloc[i] = portfolio['cash'].iloc[i-1]

        elif signal == -1: # Sell signal
            if positions.iloc[i-1] > 0:
                portfolio['cash'].iloc[i] = positions.iloc[i-1] * price
                positions.iloc[i] = 0
            else: # No position to sell, carry forward cash
                positions.iloc[i] = positions.iloc[i-1]
                portfolio['cash'].iloc[i] = portfolio['cash'].iloc[i-1]
        else: # Hold signal
            positions.iloc[i] = positions.iloc[i-1]
            portfolio['cash'].iloc[i] = portfolio['cash'].iloc[i-1]

    portfolio['holdings'] = positions * signals['price']
    portfolio['total'] = portfolio['cash'] + portfolio['holdings']
    portfolio['returns'] = portfolio['total'].pct_change()

    return portfolio