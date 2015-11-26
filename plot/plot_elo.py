import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

points_plot = []
for n in range(32):
    points_plot.append([])
data = pd.read_csv('excel_forest_plot_cdr2.csv')
for index_row, row in data.loc[:, '1':'8'].iterrows():
    for index_col, value in row.iteritems():
        if not pd.isnull(value) and np.isreal(value):
            points_plot[index_row].append(value)

for n in range(32):
    points_plot[n] = sorted(points_plot[n])

print points_plot

for n in range(32):
    plt.plot(points_plot[n], [n+1]*len(points_plot[n]), '-o')

plt.show()
