'''
This program tests TradeBoy.py over a period of time
'''

from TradeBot import tradeBot

# Settings
accountBalance = 100000
positionSize = 0.2
testLength = 120
shorting = False
pyrammiding = False
fileName = 'Data/TMHC.csv'

# Helper functions definitions
def loadData(dataFile):
    '''
    Load closing price data from file, validate the format, and return an array of closing prices
    Inputs:
        - dataFile: filename for input price data
        - maxLength: largest period length; data must have enough to satisfy this
    '''
    # Input validation
    assert os.path.isfile(dataFile)

    data = []
    dates = []

    with open(dataFile, 'r') as file:
        lines = file.readlines()

        # Check file format
        assert lines[0] == 'Date,Open,High,Low,Close,Adj Close,Volume\n'

        # Iterate over each line to save the date and closing price
        for line in lines[1:]:
            line = line.split(',')
            data.append(round(float(line[4]), 2))
            dates.append(line[0])

    return data, dates