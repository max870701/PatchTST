import yfinance as yf

# Download S&P 500 index history data
df = yf.download('^GSPC', start='2000-01-01', end='2023-12-31')

# Save the data to CSV
df.to_csv("sp500.csv")