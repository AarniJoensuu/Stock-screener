import requests
import json

import pandas as pd
from bs4 import BeautifulSoup as bs

URL = 'https://www.slickcharts.com/sp500'

def get_spy_tickers():
  request = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
  soup = bs(request.text, "lxml")
  stats = soup.find('table', class_='table table-hover table-borderless table-sm')
  companies = json.loads(pd.read_html(str(stats))[0].to_json(orient="records"))
  tickers = []
  for company in companies:
    tickers.append(company["Symbol"])
  return tickers

def main():
  print(get_spy_tickers())

if __name__=="__main__":
  main()
