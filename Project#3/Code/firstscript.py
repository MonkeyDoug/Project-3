# Imports
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
# import of

# data file
file_path = "C:\\Users\\derpe\\finance\\data\\datatest.txt"
f = open(file_path, "w")
f.truncate(0)

# Test
exxon = yf.Ticker('XOM')
hist_data = exxon.history(period = 'max', interval = '1d')



def cycle(x,y):
    hist_data = exxon.history(start = x, end = y, interval = "1d")
    f.write(str(hist_data))

# Data Download
date = {'2017-01-01':'2017-01-07','2017-01-08':'2017-01-15'}
for x,y in date.items():
    cycle(x,y) 
