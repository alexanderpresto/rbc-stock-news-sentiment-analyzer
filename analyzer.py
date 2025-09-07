# analyzer.py

# --- Part 1: Importing Libraries ---
# These lines import the tools we need for our script.

import pandas as pd  # noqa: F401
import requests
import yfinance as yf  # type: ignore
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  # type: ignore

# --- Part 2: Downloading Stock Data ---
# Here, we define which stock we want and download its data.

# Define the ticker symbol and the period
ticker = "RY.TO"
# This line calls the download function to get the data
stock_data = yf.download(ticker, period="1y")

# This prints the first 5 rows of the downloaded data
# print(stock_data.head())

# --- Part 3: Scraping News Headlines ---
# In this section, we fetch and extract news headlines from Google News.

# Scrape news headlines
query = "Royal Bank of Canada"
url = f"https://news.google.com/search?q={query}&hl=en-CA&gl=CA&ceid=CA:en"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("a", {"class": "JtKRv"})

# for headline in headlines:
#     print(headline.text)

# Perform sentiment analysis
analyzer = SentimentIntensityAnalyzer()
for headline in headlines:
    sentiment = analyzer.polarity_scores(headline.text)
    print(f"Headline: {headline.text}\nSentiment: {sentiment}\n")
