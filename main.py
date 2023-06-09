import os
import yfinance as yf
save_path = "Watchlists"
#stock = yf.Ticker("MSFT")

# get all stock info
#price = stock.info['currentPrice']
#print(price)
watchlists = {"Tech": ['AAPL','MSFT','NVDA','PLTR','AMD','TSM','TSLA'],'Finance': ['JPM','BAC','MS','GS','C','RY','SCHW'],'Healthcare':['PFE','AMGN','JNJ','LLY','GILD','AZN','MRNA']}


def gettingData(choice):
    stock = yf.Ticker(choice)
    price = stock.info['currentPrice']
    print("Last Price:",price)


while True:
    start = input("Which watchlist would you like to read from (Tech, Finance or Healthcare)? ")
    print("\nPlease choose a stock to read from:")
    for i in watchlists[start]:
        print(i)
    choiceOfStock = input("\n")
    gettingData(choiceOfStock)
    running = input("\nWould you like to read more data (y/n)? ")
    if running == "n":
        break
#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance