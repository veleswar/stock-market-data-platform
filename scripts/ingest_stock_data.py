import yfinance as yf
import pandas as pd
from datetime import datetime,timezone
import os

TICKERS = ["AAPL","MSFT","GOOG"]

OUTPUT_DIR = "data/raw"
os.makedirs(OUTPUT_DIR,exist_ok = True)

# data fetching from yfinance api
for ticker in TICKERS:
    print(f"fetching data for {ticker}")
    df = yf.download(ticker,period="30d",interval="1d")
    df.reset_index(inplace=True)
    df["ticker"] = ticker
    df["ingestion_timestamp"] = datetime.now(timezone.utc)

    file_path = f"{OUTPUT_DIR}/{ticker}.csv"

    df.to_csv(file_path, index=False)

    print(f"Saved {ticker} data to {file_path}")