import yfinance as yf

# Define stock tickers to fetch
tickers = ["AAPL", "MSFT", "GOOGL", "TSLA"]

# ANSI color codes for highlighting
GREEN = '\033[92m'
BOLD = '\033[1m'
RED = '\033[91m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Track failed tickers
failed_tickers = []

# Print table header
print("\n" + "="*80)
print(f"{'Ticker':<10} {'Price':<15} {'Daily Change':<15} {'52W High':<15} {'Status':<15}")
print("="*80)

# Fetch and display data for each ticker
for ticker_symbol in tickers:
    try:
        ticker = yf.Ticker(ticker_symbol)
        info = ticker.info

        current_price = info.get('currentPrice', 'N/A')
        percent_change = info.get('regularMarketChangePercent', 0)
        week_52_high = info.get('fiftyTwoWeekHigh', 'N/A')

        # Check if we got valid data
        if current_price == 'N/A' or current_price is None:
            failed_tickers.append((ticker_symbol, "No price data available"))
            continue

        # Format price and percent change
        price_str = f"${current_price:.2f}"
        change_str = f"{percent_change:+.2f}%"

        if week_52_high != 'N/A' and week_52_high is not None:
            high_str = f"${week_52_high:.2f}"
        else:
            high_str = "N/A"

        # Check if within 5% of 52-week high
        status = ""
        highlight = ""
        if week_52_high != 'N/A' and week_52_high is not None:
            percent_from_high = ((week_52_high - current_price) / week_52_high) * 100
            if percent_from_high <= 5:
                status = "🔥 Near High!"
                highlight = GREEN + BOLD

        # Print row with highlighting if near 52-week high
        if highlight:
            print(f"{highlight}{ticker_symbol:<10} {price_str:<15} {change_str:<15} {high_str:<15} {status:<15}{RESET}")
        else:
            print(f"{ticker_symbol:<10} {price_str:<15} {change_str:<15} {high_str:<15} {status:<15}")

    except Exception as e:
        failed_tickers.append((ticker_symbol, str(e)))
        continue

print("="*80)

# Display warnings for failed tickers
if failed_tickers:
    print(f"\n{YELLOW}⚠️  Warnings:{RESET}")
    for ticker_symbol, error in failed_tickers:
        print(f"{RED}  ✗ {ticker_symbol}: {error}{RESET}")
    print()

