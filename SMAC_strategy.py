#  Description : this program uses the simple moving average crossover(SMAC) strategy using python

# import the libraries
from cProfile import label
from turtle import color
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read the HINDALCO_1D.xlsx file data
data_frame =pd.read_excel("HINDALCO_1D.xlsx")

# Set the 'Date' column as index
data_frame =data_frame.set_index(pd.DatetimeIndex(data_frame['datetime'].values))

# Function for find simple moving average for 30 days
def SMA(data,period=30,column='close'):
    return data[column].rolling(window=period).mean()

# add new column SMA30 in data frame
data_frame['SA30'] =SMA(data_frame)

# function for SMA strategy
def strategy(dframe):
    buy =[]
    sell =[]
    flag =0
    buy_price =0

    for i in range(0,len(dframe)):
        if dframe['SA30'][i] > dframe['close'][i] and flag == 0:
            buy.append(dframe['close'][i])
            sell.append(np.nan)
            buy_price =dframe['close'][i]
            flag =1
        elif dframe['SA30'][i] < dframe['close'][i] and flag == 1 and buy_price < dframe['close'][i]:
            sell.append(dframe['close'][i])
            buy.append(np.nan)
            buy_price =0
            flag =0
        else:
            sell.append(np.nan)
            buy.append(np.nan)
    
    return (buy,sell)

# Get the buy and sell list
my_strategy =strategy(data_frame)
data_frame['buy'] =my_strategy[0]
data_frame['sell'] =my_strategy[1]

# Visualise the close price with buy and sell signals
plt.figure(figsize=(22,8))
plt.title('HINDALCO Close Price With Buy and Sell Signals', fontsize =18)
plt.plot(data_frame['close'], alpha =0.5, label ='close')
plt.plot(data_frame['SA30'], alpha =0.5, label ='SA30')
plt.scatter(data_frame.index, data_frame['buy'], color ='green',label='Buy signal',marker='^',alpha =1)
plt.scatter(data_frame.index, data_frame['sell'], color ='red',label='Sell signal',marker='v',alpha =1)
plt.xlabel('Date', fontsize =18)
plt.ylabel('HINDALCO Close price in Rupees', fontsize =14)

plt.show()