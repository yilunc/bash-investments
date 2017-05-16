from yahoo_finance import Share
from Portfolio import Portfolio
import pickle

PICKLE_PATH = '~/Dev/investments/portfolio.pickle'

if not os.path.exists(PICKLE_PATH):
  with open(PICKLE_PATH, 'wb') as f:
    pickle.dump(, f)

with open(PICKLE_PATH, 'rb') as f:
      portfolio = pickle.load(f)

portfolio
