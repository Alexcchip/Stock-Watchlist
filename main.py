#Importing the yFinance package. This package provides easy access to the Yahoo finance API
import yfinance as yf

#Creating a default watchlist of the largest companies within a few different sectors
watchlists = {"Tech": ['AAPL','MSFT','NVDA','PLTR','AMD','TSM','TSLA'],'Finance': ['JPM','BAC','MS','GS','C','RY','SCHW'],'Healthcare':['PFE','AMGN','JNJ','LLY','GILD','AZN','MRNA']}

"""
This function takes in the choice parameter which is inputted by the user. By creating a yFinance object, 
I was able to use stock.info to call data using stock.info (a dictionary/JSON object). I found the keys of the dictionary by 
itterating through stock.info (I deleted those lines).

"""

    
def gettingData(choice):
    stock = yf.Ticker(choice)
    print(f'''      Quick Facts:\n
    Last Price: {stock.info['currentPrice']}
    52 Week Change: {100*float(format(stock.info['52WeekChange'],".4f"))}%
    Exchange Traded On: {stock.info['exchange']}
    Share Float: {stock.info['floatShares']}
    Last Split Date: {stock.info['lastSplitDate']}\n
        Finances:\n
    Gross Profits: {stock.info['grossProfits']}
    Total Debt: {stock.info['totalDebt']}
    Free Cash Flow: {stock.info['freeCashflow']}
    Revenue Per Share: {stock.info['revenuePerShare']}
    Shares Short: {stock.info['sharesShort']}''')
    

'''
This is a loop that runs as long as the user wants. This allows the user to either choose to input 
a ticker or to choose a list of stocks from a hard coded watchlist.
'''
while True:
    userInputOrWatchlist = input('Would you like to input your own ticker or search from premade watchlist ("input" or "watchlist")? ')
    if userInputOrWatchlist == 'input':
        choiceOfStock = input("Input ticker:\n")
        gettingData(choiceOfStock)
    else:
        watchlistInput = input("Which watchlist would you like to read from (Tech, Finance or Healthcare)? ")
        print("\nPlease choose a stock to read from:")
        for i in watchlists[watchlistInput]:
            print(i)
        choiceOfStock = input("\n")
        gettingData(choiceOfStock)
    running = input("\nWould you like to read more data (y/n)? ")
    if running == "n":
        break
#https://stackoverflow.com/questions/61104362/how-to-get-actual-stock-prices-with-yfinance

'''
Below is the list of keys in the stock.info dictionary:

address1
city
state
zip
country
phone
fax
website
industry
industryDisp
sector
longBusinessSummary
fullTimeEmployees
companyOfficers
auditRisk
boardRisk
compensationRisk
shareHolderRightsRisk
overallRisk
governanceEpochDate
compensationAsOfEpochDate
maxAge
priceHint
previousClose
open
dayLow
dayHigh
regularMarketPreviousClose
regularMarketOpen
regularMarketDayLow
regularMarketDayHigh
dividendRate
dividendYield
exDividendDate
payoutRatio
fiveYearAvgDividendYield
beta
trailingPE
forwardPE
volume
regularMarketVolume
averageVolume
averageVolume10days
averageDailyVolume10Day
bid
ask
bidSize
askSize
marketCap
fiftyTwoWeekLow
fiftyTwoWeekHigh
priceToSalesTrailing12Months
fiftyDayAverage
twoHundredDayAverage
trailingAnnualDividendRate
trailingAnnualDividendYield
currency
enterpriseValue
profitMargins
floatShares
sharesOutstanding
sharesShort
sharesShortPriorMonth
sharesShortPreviousMonthDate
dateShortInterest
sharesPercentSharesOut
heldPercentInsiders
heldPercentInstitutions
shortRatio
shortPercentOfFloat
impliedSharesOutstanding
bookValue
priceToBook
lastFiscalYearEnd
nextFiscalYearEnd
mostRecentQuarter
earningsQuarterlyGrowth
netIncomeToCommon
trailingEps
forwardEps
pegRatio
lastSplitFactor
lastSplitDate
enterpriseToRevenue
enterpriseToEbitda
52WeekChange
SandP52WeekChange
lastDividendValue
lastDividendDate
exchange
quoteType
symbol
underlyingSymbol
shortName
longName
firstTradeDateEpochUtc
timeZoneFullName
timeZoneShortName
uuid
messageBoardId
gmtOffSetMilliseconds
currentPrice
targetHighPrice
targetLowPrice
targetMeanPrice
targetMedianPrice
recommendationMean
recommendationKey
numberOfAnalystOpinions
totalCash
totalCashPerShare
ebitda
totalDebt
quickRatio
currentRatio
totalRevenue
debtToEquity
revenuePerShare
returnOnAssets
returnOnEquity
grossProfits
freeCashflow
operatingCashflow
earningsGrowth
revenueGrowth
grossMargins
ebitdaMargins
operatingMargins
financialCurrency
trailingPegRatio'''