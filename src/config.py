# file: src/config.py

import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root
load_dotenv()

# --- API Configuration ---
API_KEY = os.getenv("UPSTOX_API_KEY")
API_SECRET = os.getenv("UPSTOX_API_SECRET")
ACCESS_TOKEN = os.getenv("UPSTOX_ACCESS_TOKEN")

# --- Sanity Checks ---
# We check that all required credentials are present.
if not all([API_KEY, API_SECRET, ACCESS_TOKEN]):
    missing = []
    if not API_KEY: missing.append("UPSTOX_API_KEY")
    if not API_SECRET: missing.append("UPSTOX_API_SECRET")
    if not ACCESS_TOKEN: missing.append("UPSTOX_ACCESS_TOKEN")
    raise ValueError(f"Missing required environment variables in .env file: {', '.join(missing)}")

# --- Data Configuration ---
DATA_RAW_DIR = "data/raw"
DATA_PROCESSED_DIR = "data/processed"

# --- Trading Configuration ---
# Instrument key for TCS. Format: EXCHANGE|TOKEN
INSTRUMENT_KEY = "NSE_EQ|INE467B01029"
INTERVAL = "1day"
FROM_DATE = "2022-01-01"
TO_DATE = "2024-06-20"