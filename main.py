import config
import os
import yfinance as yf

#stock = yf.Ticker("MSFT")

# get all stock info
#price = stock.info['currentPrice']
#print(price)

print("     Welcome to your personalized stock watchlist")

initial = int(input("""
Add: 1
Delete: 2
"""))
if initial == 1:
    fileName= input("Name of watchlist: ")
    f = open(f"{fileName}", "w+")
    num = int(input("How many stocks to watch? "))
    for i in range (num):
        sAdd = input("Ticker name: ")
        f.write(sAdd+",")
elif initial == 2:
    toDelete = input("File name to delete: ")
    os.remove(f"{toDelete}")


#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance