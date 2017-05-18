# bash-investments
### A stock dashboard for your terminal

###### For a portfolio summary:

```./portfolio.py r ```

###### To add a stock:

```./portfolio.py a *num_shares* *price*```

###### To remove ("sell") a stock:

```./portfolio.py s *purchase_num_shares* *purchase_price* *sell_num_shares* *sell_price*```

###### Sample output:

```
---YOUR PORTFOLIO---
Total equity: $155007.50
Capital gain: $13578.38
Percentage gain: 9.69%
--------------------
    GOOG at $943.0:
         100 shares | Basis: $91000.0 | Purch. Price: $910.0 | Gain: $3300.0 | Return: 3.63%
         50 shares | Basis: $42000.0 | Purch. Price: $840.0 | Gain: $5150.0 | Return: 12.26%
    SNAP at $20.78:
         75 shares | Basis: $1312.5 | Purch. Price: $17.5 | Gain: $246.0 | Return: 18.74%
    SHOP at $94.93:
         100 shares | Basis: $4593.0 | Purch. Price: $45.93 | Gain: $4900.0 | Return: 106.68%
    P at $9.35:
         300 shares | Basis: $2679.0 | Purch. Price: $8.93 | Gain: $126.0 | Return: 4.7%
```
