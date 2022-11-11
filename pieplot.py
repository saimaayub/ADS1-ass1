# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 14:03:42 2022

@author: steve
"""

import pandas as pd
import matplotlib.pyplot as plt
Debt = pd.read_excel(r"C:\Users\saima\Debt data.xls")
print(Debt)
debt= Debt.iloc[:,1]
mylabels = Debt.iloc[:, 0]
plt.pie(debt, labels = mylabels, counterclock=False, autopct='%1.1f%%', shadow=True)
plt.title("Debt (% of GDP) of lower income countries")
plt.show()