CREATE TABLE IF NOT EXISTS bronze_stock_prices (

    id SERIAL PRIMARY KEY,

    symbol VARCHAR(20),
    trade_date DATE,

    open_price NUMERIC,
    high_price NUMERIC,
    low_price NUMERIC,
    close_price NUMERIC,

    volume BIGINT,

    ingestion_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);