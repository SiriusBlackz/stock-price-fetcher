# Stock Price Fetcher

A Python script that fetches real-time stock prices and displays them in a formatted table with 52-week high tracking.

## Features

- Fetches current stock prices for multiple tickers (AAPL, MSFT, GOOGL, TSLA)
- Shows daily percentage change
- Displays 52-week high prices
- Highlights stocks that are within 5% of their 52-week high
- Graceful error handling for failed ticker lookups

## Requirements

- Python 3.7+
- yfinance library

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python fetch_stock_price.py
```

## Example Output

```
================================================================================
Ticker     Price           Daily Change    52W High        Status
================================================================================
AAPL       $178.50         +1.25%          $182.00         🔥 Near High!
MSFT       $375.20         +0.80%          $380.00
GOOGL      $142.75         -0.50%          $155.00
TSLA       $245.30         +2.10%          $300.00
================================================================================
```

## Customization

To track different stocks, edit the `tickers` list in `fetch_stock_price.py`:

```python
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]
```
