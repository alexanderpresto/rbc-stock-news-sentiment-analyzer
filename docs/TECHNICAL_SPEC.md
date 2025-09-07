# Technical Specification: RBC Stock News Sentiment Analyzer

## 1. Introduction

This document outlines the technical design and architecture for the `analyzer.py` script. The script's purpose is to scrape RBC-related news headlines, download RBC stock data, perform sentiment analysis on the headlines, and visualize the correlation between stock price and news sentiment.

## 2. Script Architecture

The `analyzer.py` script will be modular, with distinct functions for each major task. This improves readability, testability, and maintainability.

The main components will be:

- **Data Gathering:** Functions to retrieve data from external sources (web and Yahoo Finance).
- **Analysis:** A function to process text and calculate sentiment scores.
- **Combination:** Logic to merge the two datasets (stock prices and sentiment scores).
- **Visualization:** A function to plot the final, combined data.
- **Main/Orchestration:** A main function to control the overall execution flow.

## 3. Data Flow

1. The `main` function will define the target company (RBC) and the time period for analysis.
2. It will call a `get_stock_data()` function, which will use the `yfinance` library to download historical stock data into a pandas DataFrame.
3. It will call a `scrape_news_headlines()` function, which will use `requests` and `BeautifulSoup4` to fetch news headlines from a specified URL and return them as a list of strings.
4. The list of headlines will be passed to an `analyze_sentiment()` function, which will use `vaderSentiment` to calculate a daily average sentiment score, returning the data in a pandas DataFrame.
5. The `main` function will then merge the stock data DataFrame and the sentiment data DataFrame based on their dates.
6. Finally, the combined DataFrame will be passed to a `plot_data()` function to generate and save the dual-axis line chart visualization.

## 4. High-Level Function Definitions

```python
def get_stock_data(ticker, period):
    """Downloads historical stock data for a given ticker and period."""
    # ... implementation using yfinance ...
    pass

def scrape_news_headlines(url):
    """Scrapes news headlines from a given URL."""
    # ... implementation using requests and BeautifulSoup ...
    pass

def analyze_sentiment(headlines):
    """Analyzes the sentiment of a list of headlines and returns daily scores."""
    # ... implementation using vaderSentiment and pandas ...
    pass

def plot_data(combined_data):
    """Generates and saves a plot from the combined stock and sentiment data."""
    # ... implementation using matplotlib/seaborn ...
    pass

def main():
    """Main function to orchestrate the data analysis workflow."""
    # ... orchestrates calls to the other functions ...
    pass

if __name__ == "__main__":
    main()
```
