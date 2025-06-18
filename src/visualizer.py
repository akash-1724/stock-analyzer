# file: src/visualizer.py (Corrected)
from src import config  # <--- CORRECTED IMPORT
import matplotlib.pyplot as plt
import mplfinance as mpf
def plot_performance(df_data, portfolio, signals):
    """
    Plots the stock price with buy/sell signals and the portfolio performance.
    """
    fig = mpf.figure(style='yahoo', figsize=(15, 10))

    # Plot 1: Candlestick chart with MAs and signals
    ax1 = fig.add_subplot(2,1,1)
    ax2 = fig.add_subplot(2,1,2, sharex=ax1) # Share x-axis for alignment

    # Create plot for moving averages
    ap = [
        mpf.make_addplot(df_data[['SMA_50', 'SMA_200']], ax=ax1),
        # Plot buy signals
        mpf.make_addplot(signals.loc[signals['signal'] == 1]['price'], type='scatter', marker='^', color='g', ax=ax1, markersize=100),
        # Plot sell signals
        mpf.make_addplot(signals.loc[signals['signal'] == -1]['price'], type='scatter', marker='v', color='r', ax=ax1, markersize=100)
    ]

    mpf.plot(df_data, type='candle', addplot=ap, ax=ax1, volume=True, show_nontrading=False)
    ax1.set_title(f"{config.INSTRUMENT_KEY} - Golden Cross Strategy")

    # Plot 2: Portfolio value over time
    ax2.plot(portfolio['total'], label='Portfolio Value')
    ax2.set_title('Portfolio Performance')
    ax2.set_ylabel('Portfolio Value (INR)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    mpf.show()