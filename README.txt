This program generates buy and sell signals for trading financial securities. These signals are
generated from simple moving average crossovers. This script is intended to be run at a point in
time in which a trade could be made, as signals are only generated for that specific moment.

Simple Moving Average Crossovers:
    A simple moving average is the average closing price of the previous n periods of a security.
    It is generated continuously and can be used to indicate momentum in the movement of a
    financial security such as a company's stock or futures contracts. A crossover occurs when
    two moving averages cross over each other, indicating a change in momentum. If the "faster"
    moving average (the one the takes the average of fewer periods and is more responsive to recent
    price data) crosses above the "slower" average, that could be interepreted as a signal to buy
    that security since it's momentum is to the upside. The opposite is true if the faster average
    crosses below the slower average.

Picking Moving Averages:
    The program aims to generate optimum signals by only using moving average pairs that resulted
    in the best buy and sell signals recently.