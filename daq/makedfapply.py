import pandas as pd
import numpy as np

# we are grabbing data from csv and eliminating the fat
# such as weekends and maybe non adjusted closes...
# this opens up space for processing more stocks in the dataframe


def test_run():
    start_date='2022-01-01'
    end_date='2022-12-30'
    dates=pd.date_range(start_date, end_date)
    df1=pd.DataFrame(index=dates)    

    dfSPY = pd.read_csv("AAPL.csv", index_col="Date", parse_dates = True, usecols=['Date', 'Adj Close'], na_values=['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close' : 'SPY'})

    #joining the 2 dataframes and dropping null rows
    df1 = df1.join(dfSPY, how='inner')
    df1 = df1.dropna()

    #adding other symbols in 
    symbols = ["GOOG", 'IBM', 'GLD']
    for symbol in symbols:
        df_temp=pd.read_csv("{}.csv".format(symbol), index_col='Date', parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.dropna()
        df_temp = df_temp.rename(columns={'Adj Close' : symbol})
        df1 = df1.join(df_temp)

    print(df1)
    df1.plot()

    # there are other row and column slices 
    
test_run()

