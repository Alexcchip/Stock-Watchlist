import os
import yfinance as yf
save_path = "Watchlists"
#stock = yf.Ticker("MSFT")

# get all stock info
#price = stock.info['currentPrice']
#print(price)
running = True
watchlists = {"Tech": ['AAPL','MSFT','NVDA','PLTR','AMD','TSM','TSLA'],'Bank/Finance': ['JPM','BAC','MS','GS','C','RY','SCHW'],'Healthcare':['PFE','AMGN','JNJ','LLY','GILD','AZN','MRNA']}
def getData():
    start = input("Which watchlist would you like to read from (Tech, Bank/Finance or Healthcare)? Hit enter to exit program.")
    if start == "":
        running = False
    for i in watchlists[start]:
        print(i)
    

while running:
    getData()
#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance