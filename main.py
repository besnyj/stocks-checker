import time
import yfinance

apple_stock = "AAPL"


def price_compare():
    
    initial_price = yfinance.Ticker(apple_stock)
    initial_price = initial_price.history(period="1d", interval="1m")
    initial_price = initial_price["Close"].iloc[-1]
    print(initial_price)
    time.sleep(60)
    last_price = yfinance.Ticker(apple_stock)
    last_price = last_price.history(period="1d", interval="1m")
    last_price = last_price["Close"].iloc[-1]
    
    print(last_price)
    
    if last_price > initial_price:
        price_change = ((((initial_price-last_price)/initial_price)*100)*(-1))
        print(f"the price increased {price_change}% since last check")
    if last_price < initial_price:
        price_change = ((((initial_price-last_price)/initial_price)*100)*(-1))
        print(f"the price decreased {price_change}% since last check")

while True:
    price_compare()


ass = 10.5667565
ass.round()