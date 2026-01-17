import yfinance as yf

# Fetch Apple stock data
ticker = yf.Ticker("AAPL")
current_price = ticker.info['currentPrice']

print(f"Apple (AAPL) current stock price: ${current_price}")

