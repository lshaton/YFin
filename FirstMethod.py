import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
aapl_df = yf.download('MSFT', 
                      start='2019-01-01', 
                      end='2021-06-12', 
                      progress=False,
)
print(aapl_df.head())