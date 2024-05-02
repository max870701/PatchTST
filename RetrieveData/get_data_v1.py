import yfinance as yf
import datetime

# Define the ticker and the time period
btc = yf.Ticker("BTC-USD")
start_date = (datetime.datetime.now() - datetime.timedelta(days=4*365)).strftime('%Y-%m-%d')
end_date = datetime.datetime.now().strftime('%Y-%m-%d')

# Get historical market data
hist = btc.history(start=start_date, end=end_date)

# Save the data to CSV
hist.to_csv("../BTC_USD_Daily_Data.csv")