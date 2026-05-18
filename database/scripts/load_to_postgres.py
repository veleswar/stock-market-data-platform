import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from datetime import datetime

DB_URI = "postgresql://stock_user:stock_pass@localhost:5433/stock_market"
engine = create_engine(DB_URI)

raw_path = Path("data/raw")
csv_files = raw_path.glob("*.csv")

for file in csv_files:
    print(f"Loading {file.name}")

    df = pd.read_csv(file)
    df = df[df["Date"].notna()]
    df = df[df["Date"] != ""]
    df = df[df["Date"].astype(str).str.match(r"\d{4}-\d{2}-\d{2}")]

    # Standardize column names
    df.columns = [c.lower() for c in df.columns]
    df = df.rename(columns={
        "date": "trade_date",
        "open": "open_price",
        "high": "high_price",
        "low": "low_price",
        "close": "close_price"
    })

    # Add ingestion timestamp
    df["ingestion_timestamp"] = datetime.utcnow()

    # Load into postgres
    df.to_sql(
        "bronze_stock_prices",
        engine,
        if_exists="append",
        index=False
    )

    print(f"Loaded {len(df)} rows")