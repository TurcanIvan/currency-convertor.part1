#App that:
# IN: money in USD
# OUT: money in EUR

moneyUSD        = int(input("enter money in USD"))  #int
rate_EUR_to_USD = 1.25   #float

moneyEUR     = moneyUSD / rate_EUR_to_USD

print("your maney in EUR :", moneyEUR)