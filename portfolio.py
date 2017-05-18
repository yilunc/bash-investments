#!/usr/bin/env python

from yahoo_finance import Share
import pickle
import os
import sys

class Portfolio():
  def __init__(self):
    self.stocks = {}
    self.cap_in = 0
    self.cap_gain = 0;
    self.curr_value = 0
    self.last_value = 0

  def __str__(self):
    s =  "---YOUR PORTFOLIO---\n"
    s += ("Total equity: ${0}\n").format(self.get_curr_value())
    s += ("Capital gain: ${0}\n").format(self.get_curr_c_gain())
    s += ("Percentage gain: {0}%\n").format(self.get_curr_p_gain())
    s +=  "--------------------\n"
    for ticker in self.stocks:
      curr_share = Share(ticker)
      curr_price = float(curr_share.get_price())
      s += ("    {0} at ${1}: \n").format(ticker, curr_price)
      for num_shares, price in self.stocks[ticker]:
        basis = num_shares * price
        gain = float(curr_price * num_shares) - basis
        return_p = round((float(curr_price-price)/float(price)) * 100, 2)
        s += ("         {0} shares | Basis: ${1} | Purch. Price: ${2} | Gain: ${3} | Return: {4}% \n") \
          .format(num_shares, basis, price, gain, return_p)
    return s

  def add_shares(self, ticker, num_shares, price):
    if ticker in self.stocks:
      self.stocks[ticker].append((num_shares, price))
    else:
      self.stocks[ticker] = [(num_shares, price)]
    self.cap_in += num_shares * price

  def sell_shares(self, ticker, curr_num_shares, buy_price, sell_num_shares, sell_price):
    if ticker in self.stocks:
      if curr_num_shares < sell_num_shares:
        print("ERROR: You do not own {0} shares of {1} stock at ${2}.").format(sell_num_shares, ticker, buy_price)
      ticker_index = self.stocks[ticker].index((curr_num_shares, buy_price))
      self.stocks[ticker][ticker_index] = (curr_num_shares - sell_num_shares, buy_price)
      self.cap_gain += (sell_price - buy_price) * sell_num_shares
      self.cap_in -= buy_price * sell_num_shares

      if self.stocks[ticker][ticker_index][0] == 0:
        self.stocks[ticker].remove((0, buy_price))
      if not self.stocks[ticker]:
        del self.stocks[ticker]
    else:
      print("ERROR: You do not own any {0} stock.").format(ticker)

  def set_last_value(self):
    self.last_value = self.get_curr_value()

  def get_curr_value(self):
    value = 0
    for ticker in self.stocks:
      curr_price = float(Share(ticker).get_price())
      for num_shares, price in self.stocks[ticker]:
        value += curr_price * num_shares
    return round(value, 2)

  def get_curr_p_gain(self):
    return round(((self.get_curr_value() - self.cap_in) / self.cap_in) * 100, 2)

  def get_curr_c_gain(self):
    return round(self.get_curr_value() - self.cap_in, 2)

  def get_cap_gain(self):
    return round(self.cap_gain, 2)

if __name__ == "__main__":
  PICKLE_PATH = 'portfolio.pickle'

  if not os.path.exists(PICKLE_PATH):
    with open(PICKLE_PATH, 'wb') as f:
      pickle.dump(Portfolio(), f)

  with open(PICKLE_PATH, 'rb') as f:
        portfolio = pickle.load(f)

  if len(sys.argv) == 2:
    if sys.argv[1] == "r": # Review of your portfolio printed to console.
      print portfolio
  elif len(sys.argv) == 5:
    if sys.argv[1] == "a": # Add a set of shares purchased at a price.
      portfolio.add_shares(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]))
  else:
    if sys.argv[1] == "s": # Sell a set of shares purchased at a price for a selling price.
      portfolio.sell_shares(sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), float(sys.argv[6]))
    
  with open(PICKLE_PATH, 'wb') as f:
      pickle.dump(portfolio, f)
