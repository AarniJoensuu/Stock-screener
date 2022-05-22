import requests
import json

import pandas as pd
from bs4 import BeautifulSoup as bs

BASE_URL = "https://finance.yahoo.com/quote/{ticker}/key-statistics?p={ticker}"

def get_stock_data(ticker):
  url = BASE_URL.replace("{ticker}", ticker)
  print(f"Fetching {ticker}")
  response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
  soup = bs(response.text, "lxml")
  stats = soup.find_all('table', class_="W(100%) Bdcl(c)")
  dfs = []
  for i in range(0, len(stats)):
    dfs.append(pd.read_html(str(stats[i]))[0])

  try:
    data = json.loads(pd.concat(dfs, ignore_index=True).to_json(orient="records"))
  except ValueError:
    return { "Symbol": ticker, "data": {} }

  parsed_data = {}
  for item in data:
    keys = list(item.keys())
    parsed_data[item[keys[0]]] = item[keys[1]]
  return { "Symbol": ticker, "data": parsed_data }

def main():
  print(get_stock_data("AAPL"))

if __name__=="__main__":
  main()
