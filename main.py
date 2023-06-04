import config
import yfinance as yf
f = open("list.txt", "w+")
stock = yf.Ticker("MSFT")

# get all stock info
price = stock.info['currentPrice']
print(price)

print("     Welcome to your personalized stock watchlist")
while True:
    initial = int(input("""Add: 1
    Read: 2
    Edit: 3
    Exit: 4
    """))
    if initial == 1:
        fileName= input("Name of watchlist: ")
        f = open(f"{fileName}", "w+")
        num = int(input("How many stocks to watch? "))
        for i in range (num):
            sAdd = input("Ticker name: ")
            f.write(sAdd+",")


#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance