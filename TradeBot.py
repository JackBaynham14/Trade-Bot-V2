'''
This program generates a buy or sell signal for the latest period in the input price data.
'''
import os

def tradeBot(dataFile, minLength=1, maxLength=100):
    '''
    Main function which calls helper functions to analyze data and generate signals
    Inputs:
        - dataFile: filename for input price data
        - maxPeriod: largest period length to test
        - minPeriod: smallest period length to test
    Outputs:
        - string containing a signal if present and information about the used moving averages
    '''
    # Input validation
    assert maxLength > minLength

    # Load closing price data into array
    data = loadData(dataFile, minLength, maxLength)

    # Initialize running best pair values
    bestPair = [1, 2]
    bestPairScore = 0

    # Iterate through every allowed moving average pair
    for slowLength in range(minLength, maxLength):
        slowLength += 1

        # Find values for slow moving average

        for fastLength in range(minLength, slowLength):
            # Find values for fast moving average

            # Find crossovers

            # Calculate performance

            # Update current bestPair/bestPairScore if better
            pass
    
    # Check for crossover of best pair in most recent period

    # Return crossover if present and information about the best pair
    return

def loadData(dataFile, minLength, maxLength):
    '''
    Load closing price data from file, validate the format, and return an array of closing prices
    '''
    # Input validation
    assert os.path.isfile(dataFile)
    assert maxLength > minLength

    data = []

    with open(dataFile, 'r') as file:
        lines = file.readlines()

        # Check file format
        assert lines[0] == 'Date,Open,High,Low,Close,Adj Close,Volume\n'

        # Iterate over each line to check and save closing price
        for line in lines[1:]:
            line = line.split(',')
            data.append(float(line[4]))

    return data

def findMovAvgValues(data, length):
    '''
    Finds the values of a moving average
    '''

    pass

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
tradeBot('Data/TMHC.csv')