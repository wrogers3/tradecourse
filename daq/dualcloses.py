#%%
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("AAPL.csv")
    #print(df['Close'])
    df[['Close', 'Adj Close']].plot()
    plt.show()

test_run()

# %%
