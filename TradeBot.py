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

    # Load closing price data into array
    data = loadData(dataFile, minLength, maxLength)

    # Initialize running best pair values
    bestPair = [1, 2]
    bestPairScore = 0

    # Iterate through every allowed moving average pair
    for slowLength in range(minLength, maxLength):
        slowLength += 1
        # Find values for slow moving average

        for fastLength in range(minLength, maxLength):
            # Find values for fast moving average

            # Find crossovers

            # Calculate performance

            # Update current bestPair/bestPairScore if better
    
    # Check for crossover of best pair in most recent period

    # Return crossover if present and information about the best pair

def loadData(dataFile, minLength, maxLength):
    '''
    Load closing price data from file, validate the format, and return an array of closing prices
    '''