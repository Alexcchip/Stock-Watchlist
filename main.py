import config
import os
import yfinance as yf
save_path = "M:\Coding\Python\Stock-Watchlist\Watchlists"
#stock = yf.Ticker("MSFT")

# get all stock info
#price = stock.info['currentPrice']
#print(price)

def readWLs():
    for i in os.listdir(save_path):
            print("     "+i+"\n")
def readStocks():
     for i in f.readlines():
        print(i)
     f.close()

print("     Welcome to your personalized stock watchlist")
while True:
    initial = int(input("""
    Add: 1
    Delete: 2
    Read: 3
    Edit: 4
    Exit: 5
    """))
    if initial == 1:
        fileName= input("Name of watchlist: ")
        directedFile =  os.path.join(save_path, fileName)
        f = open(f"{directedFile}", "a")
        num = int(input("How many stocks to watch? "))
        for i in range(num):
            sAdd = input("Ticker name: ")
            f.write(str(i)+": "+sAdd)
            f.write("\n")
        f.close()
    elif initial == 2:
        toDelete = input("File name to delete: ")
        os.remove(f"Watchlists"+"\\"+toDelete)
    elif initial == 3:
        print("Which watchlist would you like to read from? ")
        readWLs()
        readingWL = input("\n")
        f = open(save_path+"\\"+readingWL)
        readStocks()
        print("Which stock would you like to see the price of? ")
        stockReadingChoice = input("\n")
        stock = yf.Ticker(stockReadingChoice)
        price = stock.info.get('currentPrice')
        print(price)
    elif initial == 4:
        print("Which watchlist would you like to edit? ")
        readWLs()
        wlEdit = input()
    elif initial == 5:
        break
#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance