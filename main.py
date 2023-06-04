import conflig

print("     Welcome to your personalized stock watchlist")
while True:
    initial = int(input("""Add: 1
    Read: 2
    Edit: 3
    Exit: 4
    """))
    if initial == 1:
        listName= input("Name of watchlist: ")
        listName = []
        num = int(input("How many stocks to watch? "))
        for i in range (num):
            sAdd = input("Ticker name: ")
            listName.append(sAdd)
    elif initial == 2:
        pass
    elif initial == 3:
        pass
    elif initial == 4:
        break



