# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:04:07 2022

@author: steve
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
Debt = pd.read_excel(r"C:\Users\saima\Debt data.xls")
print(Debt)
debt= Debt.iloc[:,1]
Years = Debt.iloc[:, 0]
plt.bar(Years, debt, color ='darkblue',  width = 0.4)
plt.xlabel("Years")
plt.ylabel("Debt(% of GDP)")
plt.title("Debt of lower income countries")
plt.show()


