# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:02:23 2015

@author: edogerde
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

points_plot = []
for n in range(38):
    points_plot.append([])
data = pd.read_csv('/home/mfpgt/Desktop/mri_rt_plot_n_38.csv')
use_rad = []
rad = []
for index_row, row in data.loc[:, '1':'9'].iterrows():
    for index_col, value in row.iteritems():
	if index_col is '9': 
	    if pd.isnull(value):
	        use_rad.append(False)
	        rad.append(0)
	    else:
	        use_rad.append(True)
	        rad.append(value)
        if not pd.isnull(value) and np.isreal(value):
            points_plot[index_row].append(value)

for n in range(38):
    points_plot[n] = sorted(points_plot[n])

for n in range(38):
    plt.plot(points_plot[n], [n+1]*len(points_plot[n]), '-o')
    if use_rad[n]:
        plt.plot(rad[n], n+1, 'rD')

plt.show()
plt.title('plot_mri_time')
plt.xlabel('time_since_diagnosis')
plt.ylabel('patients')
