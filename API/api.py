import asyncio
from multiprocessing import Pool, freeze_support

from flask import Flask

from yahoo_parser import get_stock_data
from dia_tickers import get_dia_tickers
from spy_tickers import get_spy_tickers
from utils import tickers_to_tuples

THREADS = 20

app = Flask("Stock API")
app.config["DEBUG"] = True

@app.route("/spy/tickers", methods=["GET"])
def fetch_spy_tickers():
  return { "symbols": get_spy_tickers() }

@app.route("/spy/data", methods=["GET"])
async def fetch_spy_data():
  spy_tickers = get_spy_tickers()
  ticker_tuple = tickers_to_tuples(spy_tickers)
  with Pool(processes=THREADS) as pool:
    results = pool.starmap(get_stock_data, ticker_tuple)
  return { "results": results }

@app.route("/dia/tickers", methods=["GET"])
def fetch_dia_tickers():
  return { "symbols": get_dia_tickers() }

@app.route("/dia/data", methods=["GET"])
async def fetch_dia_data():
  dia_tickers = get_dia_tickers()
  ticker_tuple = tickers_to_tuples(dia_tickers)
  with Pool(processes=THREADS) as pool:
    results = pool.starmap(get_stock_data, ticker_tuple)
  return { "results": results }

if __name__=="__main__":
  app.run()
