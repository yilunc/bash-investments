#!/usr/bin/env python

from yahoo_finance import Share
from portfolio import Portfolio
import pickle
import os
import sys

PICKLE_PATH = 'portfolio.pickle'

if not os.path.exists(PICKLE_PATH):
  with open(PICKLE_PATH, 'wb') as f:
    pickle.dump(Portfolio(), f)

with open(PICKLE_PATH, 'rb') as f:
      portfolio = pickle.load(f)

if len(sys.argv) == 2:
  if sys.argv[1] == "r": # Prints a review of your portfolio to console.
    print(str(portfolio))
elif len(sys.argv) == 5:
  if sys.argv[1] == "a": # Add a set of shares purchased at a price.
    portfolio.add_shares(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]))
else:
  if sys.argv[1] == "s": # Sell a set of shares purchased at a price for a selling price.
    portfolio.sell_shares(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]))
  
with open(PICKLE_PATH, 'wb') as f:
    pickle.dump(portfolio, f)
