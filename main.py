import os
import yfinance as yf
#save_path = "Watchlists"
#stock = yf.Ticker("MSFT")

# get all stock info
#price = stock.info['currentPrice']
#print(price)
WLS = dict()
def readWLs():
    for i in WLS:
            print("     "+i+"\n")
    print(WLS)
def readStocks():
     for i in f.readlines():

        stock = yf.Ticker(i)
        price = stock.info.get('currentPrice')  
        print(i)
        print(price)

print("     Welcome to your personalized stock watchlist")
while True:
    initial = int(input("""\n 
    Add: 1 | Delete: 2 | Read: 3 | Edit: 4 | Exit: 5
    """))
    if initial == 1:
        wlName= input("Name of watchlist: ")
        grouping = []
        num = int(input("How many stocks to watch? "))
        for i in range(num):
            sAdd = input("Ticker name: ")
            grouping.append(sAdd)
        WLS[wlName] = grouping
    elif initial == 2:
        toDelete = input("Watchlist to delete: ")
        WLS.pop(toDelete)
    elif initial == 3:
        print("Which watchlist would you like to read from? ")
        readWLs()
        readingWL = input("\n")
        #f = open(save_path+"\\"+readingWL)
        readStocks()
    elif initial == 4:
        print("Which watchlist would you like to edit? ")
        readWLs()
        wlEdit = input()
    elif initial == 5:
        break
#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance