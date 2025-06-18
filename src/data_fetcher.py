# file: src/data_fetcher.py (Original)
import upstox_client
from src import config

def get_api_client():
    """Configures and returns the Upstox API client."""
    api_config = upstox_client.Configuration()
    api_config.access_token = config.ACCESS_TOKEN
    return upstox_client.ApiClient(api_config)

def fetch_historical_data(api_client, instrument_key, interval, from_date, to_date):
    """Fetches historical OHLC data from Upstox."""
    api_instance = upstox_client.HistoryApi(api_client)
    try:
        api_response = api_instance.get_historical_candle_data(
            instrument_key=instrument_key,
            interval=interval,
            from_date=from_date,
            to_date=to_date,
            api_version="v2"
        )
        return api_response.data.candles
    except Exception as e:
        print(f"Error fetching data from Upstox API: {e}")
        return None