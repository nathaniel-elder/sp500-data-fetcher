# S&P 500 Market Cap Fetcher

This script fetches the company ticker, current market capitalization (in millions), and optionable status of S&P 500 companies and saves said data to a CSV file.

## Requirements

- Python 3.7 or higher
- Internet connection (to fetch data from Yahoo Finance and Wikipedia)

## Installation

1. Clone this repository:
   ```git clone https://github.com/yourusername/sp500-data-fetcher.git
   cd sp500-data-fetcher```

4. Install the required Python packages:
   ```pip install -r requirements.txt```

## Usage

1. Run the script:
   ```python sp500_data_to_csv.py```

The output will be saved as "sp500_market_caps.csv" in the same directory.

## Output Format

The CSV file will contain the following columns:
- "symbol": Stock ticker symbol
- "marketcap (in millions)": Market capitalization in millions
- "optionable": Whether the stock is optionable ("yes" or "no")
