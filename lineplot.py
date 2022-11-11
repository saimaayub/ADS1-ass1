# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 20:15:41 2022

@author: steve
"""

import pandas as pd
import matplotlib.pyplot as plt
employment = pd.read_excel(r"C:\Users\saima\employment rate by wave.xlsx")
print(employment)
Months = employment.iloc[:,0]
Wave_1 = employment.iloc[:,1]
Wave_2 = employment.iloc[:,2]
plt.figure()
# plot the waves with labels
plt.plot(employment ["Months"], employment["Wave 1"], label="Wave1")
plt.plot(employment ["Months"], employment["Wave 2"], label="Wave2")
# naming the title and axis of the plot
plt.title("Monthly Employment Rate")
plt.xlabel("Months")
plt.ylabel("Employment Rate((%)")
plt.legend()
plt.show()
