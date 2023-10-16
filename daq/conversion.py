# recieve data and make into dataframe
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np


# date open high low close, adj close and volume
def readFile(filename):
    date, opem, high, low, close, adjclose, vol = np.loadtxt(filename, unpack = True, delimiter=',', converters = {0:mdates.datestr2num("%Y%m%d%H%M%S")}) 

    fig = plt.figure(figsize=(10, 7))
    ax1 = plt.subplot2grid((40,40), (0,0), rowspan=40, colspan=40)

    ax1.plot(date, bid)
    ax1.plot(date, ask)

    ax1.xaxis,set_major_formatter(mdates.dateFormatter('%Y-%m-%d %H:%M:%S'))

    plt.grid(true)
    plt.show()

readFile('AAPL')
