import requests
import json

import pandas as pd
from bs4 import BeautifulSoup as bs

URL = "https://www.dogsofthedow.com/dow-jones-industrial-average-companies.htm"

def get_dia_tickers():
  request = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
  soup = bs(request.text, "lxml")
  stats = soup.find('table', class_='tablepress tablepress-id-42 tablepress-responsive')
  companies = json.loads(pd.read_html(str(stats))[0].to_json(orient="records"))
  tickers = []
  for company in companies:
    tickers.append(company["Symbol"])
  return tickers

def main():
  print(get_dia_tickers())

if __name__=="__main__":
  main()