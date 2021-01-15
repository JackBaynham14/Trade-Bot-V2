'''
This program generates a buy or sell signal for the latest period in the input price data.
'''
import os

def tradeBot(dataFile, testLength=90, minLength=1, maxLength=100):
    '''
    Main function which calls helper functions to analyze data and generate trade signals
    Inputs:
        - dataFile: filename for input price data
        - testLength: number of periods to test for best pair
        - minPeriod: smallest period length to test
        - maxPeriod: largest period length to test
    Outputs:
        - string containing a signal if present and information about the used moving averages
    '''
    # Input validation
    assert maxLength > minLength

    # Load closing price data into array
    data, dates = loadData(dataFile)

    # Check for sufficient amount of data and remove extra data
    assert len(data) > (testLength + maxLength - 1)
    data = data[-(testLength + maxLength - 1):]

    print(data)
    print(len(data))

    # Initialize current best pair values
    bestPair = [1, 2]
    bestPairScore = 0

    # Iterate through every allowed moving average pair
    for slowLength in range(minLength, maxLength):
        slowLength += 1

        # Find values for slow moving average and remove extra values
        slowValues = findMovAvgValues(data, slowLength)

        for fastLength in range(minLength, slowLength):
            # Find values for fast moving average and remove extra values
            fastValues = findMovAvgValues(data, fastLength)

            # Find crossovers
            crossovers = findCrossovers(fastValues, slowValues)

            # Calculate performance

            # Update current bestPair/bestPairScore if better
            pass
    
    # Check for crossover of best pair in most recent period

    # Return crossover if present and information about the best pair
    return

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

def findMovAvgValues(data, length):
    '''
    Finds the values of a moving average
    Inputs:
        - data: Price data as an array
        - length: Length of moving average to calculate for all valid periods
    Outpus:
        - list containing the moving average values for the data and length
    '''
    # Input validation
    assert isinstance(data, list)
    assert isinstance(length, int)
    assert len(data) >= length

    values = []

    # Iterate over valid periods and find the value of the average
    for i in range(length, len(data)+1):
        values.append(round(sum(data[i:i+length]) / length, 2))
    
    return values

def findCrossovers(fastValues, slowValues):
    '''
    Finds crossovers of the fast values crossing the slow values
    Inputs:
        - fastValues: array of values values that crossover the slowValues
        - slowValues: array of values that are crossovered by the fastValues
    Outputs:
        - array of crossover at each period (0, 1, -1)
    '''
    # Input validation
    assert isinstance(fastValues, list)
    assert isinstance(slowValues, list)
    assert len(fastValues) == len(slowValues)
    assert len(fastValues) > 1

    crossovers = [0]

    # Iterate over each period and add crossover status
    for i in range(1, len(fastValues)):
        prevDif = fastValues[i-1] - slowValues[i-1]
        newDif = fastValues[i] - slowValues[i]

        # Check if signs changed
        if prevDif > 0 and newDif < 0:
            crossovers.append(-1)
        elif prevDif < 0 and newDif > 0:
            crossovers.append(1)
        else:
            crossovers.append(0)
    
    return crossovers

def findPerformance(data, crossovers):
    '''
    Finds average sell and buy prices and returns the difference
    Inputs:
        - data: price data used to determine price at trade signals
        - crossovers: list of crossover locations and types
    Outputs:
        - Average buy and sell prices
    '''
    # Input validation
    assert isinstance(data, list)
    assert isinstance(crossovers, list)
    assert len(data) == len(crossovers)

    buys = []
    sells = []

    # Iterate over each period and add appropriate trades
    for i in range(len(data)):
        if crossovers[i] == 1:
            buys.append(data[i])
        elif crossovers[i] == -1:
            sells.append(data[i])
    
    # Calculate average buy, sell, and profit
    avgBuy = sum(buys) / len(buys)
    avgSell = sum(sells) / len(sells)
    avgProfit = avgSell - avgBuy

    return avgProfit, avgBuy, avgSell

#Program testing
tradeBot('Data/TMHC.csv', testLength=10, maxLength=5)