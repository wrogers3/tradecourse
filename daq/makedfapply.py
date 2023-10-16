#%%
import pandas as pd
import numpy as np

# we are grabbing data from csv and eliminating the fat
# such as weekends and maybe non adjusted closes...
# this opens up space for processing more stocks in the dataframe

def test_run():
    start_date='2021-01-22'
    end_date='2021-01-26'
    dates=pd.date_range(start_date, end_date)
    df1=pd.DataFrame(index=dates)    
    print(df1)

test_run()

# %%
