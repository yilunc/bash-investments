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
  if sys.argv[1] == "s":
    print(str(portfolio))
elif len(sys.argv) == 5:
  portfolio.add_shares(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]))
else:
  portfolio.sell_shares(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]))
  
with open(PICKLE_PATH, 'wb') as f:
    pickle.dump(portfolio, f)
