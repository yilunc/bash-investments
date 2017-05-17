from yahoo_finance import Share

class Portfolio():
  def __init__(self):
    self.stocks = {}
    self.cap_in = 0
    self.cap_gain = 0;
    self.curr_value = 0
    self.last_value = 0

  def __str__(self):
    str =  "---YOUR PORTFOLIO---\n"
    for ticker in self.stocks:
      str += ("\t{0}: \n").format(ticker)
      curr_share = Share(ticker)
      for num_shares, price in self.stocks[ticker]:
        basis = num_shares * price
        curr_price = float(curr_share.get_price())
        gain = float(curr_price * num_shares) - basis
        return_p = float(curr_price-price)/float(price)
        str += ("\t  {0} shares. Basis: ${1} | Curr. Price: ${2} | Gain: ${2} | Return: {2}% \n") \
          .format(num_shares, basis, curr_price, gain, return_p)
    return str

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
      ticker_index = self.stocks[ticker].index((num_shares, price))
      self.stocks[ticker][ticker_index] = (num_shares - sell_num_shares, buy_price)
      self.cap_gain += (sell_price - buy_price) * sell_num_shares
      self.cap_in -= buy_price * sell_num_shares
    else:
      print("ERROR: You do not own any {0} stock.").format(ticker)

  def set_last_value(self):
    self.last_value = self.get_curr_value()

  def get_curr_value(self):
    value = 0
    for ticker in self.stocks:
      for num_shares, price in self.stocks[ticker]:
        value += Share(ticker).get_price() * num_shares
    return value

  def get_curr_p_gain(self):
    return (get_curr_value - self.cap_in) / self.cap_in

  def get_curr_c_gain(self):
    return get_curr_value - self.cap_in

  def get_cap_gain(self):
    return self.cap_gain





