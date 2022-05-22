def tickers_to_tuples(tickers):
  tuples = []
  for ticker in tickers:
    tmp = []
    tmp.append(ticker)
    tuples.append(tuple(tmp))
  return tuples
