# file: main.py

import os
import pandas as pd
from src import config, data_fetcher, data_processor, indicators, strategy, backtester, visualizer

def run_pipeline():
    """Executes the full data fetching, analysis, and backtesting pipeline."""
    # Ensure data directories exist
    os.makedirs(config.DATA_RAW_DIR, exist_ok=True)
    os.makedirs(config.DATA_PROCESSED_DIR, exist_ok=True)

    # --- Phase 1: Data Fetching and Processing ---
    print("Phase 1: Fetching and Processing Data...")
    api_client = data_fetcher.get_api_client()
    raw_candles = data_fetcher.fetch_historical_data(
        api_client, config.INSTRUMENT_KEY, config.INTERVAL, config.FROM_DATE, config.TO_DATE
    )

    if not raw_candles:
        print("Failed to fetch data. Exiting.")
        return

    df_raw = data_processor.process_to_dataframe(raw_candles)
    raw_path = os.path.join(config.DATA_RAW_DIR, f"{config.INSTRUMENT_KEY.replace('|','_')}_raw.csv")
    df_raw.to_csv(raw_path)
    print(f"Raw data saved to {raw_path}")

    # --- Phase 2: Technical Analysis ---
    print("\nPhase 2: Adding Technical Indicators...")
    df_processed = indicators.add_indicators(df_raw.copy())
    processed_path = os.path.join(config.DATA_PROCESSED_DIR, f"{config.INSTRUMENT_KEY.replace('|','_')}_processed.csv")
    df_processed.to_csv(processed_path)
    print(f"Processed data with indicators saved to {processed_path}")

    # --- Phase 3: Strategy, Backtesting & Visualization ---
    print("\nPhase 3: Generating Signals and Backtesting...")
    signals = strategy.generate_signals(df_processed)
    portfolio = backtester.run_backtest(signals)

    # --- Print Performance Metrics ---
    final_value = portfolio['total'].iloc[-1]
    pnl = final_value - 100000
    print("\n--- Backtest Results ---")
    print(f"Initial Capital: 100,000.00 INR")
    print(f"Final Portfolio Value: {final_value:,.2f} INR")
    print(f"Profit/Loss: {pnl:,.2f} INR")
    
    print("\nVisualizing results...")
    visualizer.plot_performance(df_processed, portfolio, signals)


if __name__ == "__main__":
    run_pipeline()