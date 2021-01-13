'''
This program generates a buy or sell signal for the latest period in the input price data.
'''
import os

def tradeBot(dataFile, minLength=1, maxLength=100):
    '''
    Main function which calls helper functions to analyze data and generate trade signals
    Inputs:
        - dataFile: filename for input price data
        - minPeriod: smallest period length to test
        - maxPeriod: largest period length to test
    Outputs:
        - string containing a signal if present and information about the used moving averages
    '''
    # Input validation
    assert maxLength > minLength

    # Load closing price data into array
    data, dates = loadData(dataFile, maxLength)

    # Initialize running best pair values
    bestPair = [1, 2]
    bestPairScore = 0

    # Iterate through every allowed moving average pair
    for slowLength in range(minLength, maxLength):
        slowLength += 1

        # Find values for slow moving average
        slowValues = findMovAvgValues(data, slowLength)

        for fastLength in range(minLength, slowLength):
            # Find values for fast moving average
            fastValues = findMovAvgValues(data, fastLength)

            # Find crossovers

            # Calculate performance

            # Update current bestPair/bestPairScore if better
            pass
    
    # Check for crossover of best pair in most recent period

    # Return crossover if present and information about the best pair
    return

def loadData(dataFile, maxLength):
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
        assert len(lines) > maxLength

        # Iterate over each line to save the date and closing price
        for line in lines[1:]:
            line = line.split(',')
            data.append(round(float(line[4]), 2))
            dates.append(line[0])

    return data[-maxLength:], dates[-maxLength:]

def findMovAvgValues(data, length):
    '''
    Finds the values of a moving average
    '''
    # Input validation
    assert len(data) >= length

    values = []

    # Iterate over valid periods and find the value of the average
    for i in range(length, len(data)+1):
        values.append(round(sum(data[i:i+length]) / length, 2))
    
    return values

def findCrossovers(fastValues, slowValues):
    '''
    Finds crossovers of the fast values crossing the slow values
    '''

    pass

def findPerformance(data, crossovers):
    '''
    Finds average sell and buy prices and returns the difference
    '''

    pass

#Program testing
print(findMovAvgValues([1, 2, 1, 2, 1, 2], 3))