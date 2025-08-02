import yfinance as yf
import pandas as pd
import sys

def fetch_sp500_market_caps():
    # Gets the S&P 500 ticker symbols from Wikipedia
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    sp500_df = table[0]
    tickers = sp500_df["Symbol"].tolist()
    
    data = [] # List to store rows for the CSV
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            market_cap = stock.info.get("marketCap", None)
            optionable = "yes" if stock.options else "no"
            if market_cap is not None:
                market_cap_in_millions = (market_cap / 1_000_000) # Convert to millions
                data.append([ticker, market_cap_in_millions, optionable])
            print(f"{ticker},{market_cap},{optionable}")
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return data
    
if __name__ == "__main__":
    data = fetch_sp500_market_caps()
     
    # Create a DataFrame and save to CSV
    df = pd.DataFrame(data, columns = ["symbol","marketcap (in millions)","optionable"])
    df.to_csv("sp500_market_caps.csv", index=False)
    print("Market capitalizations fetched and saved successfully.")