import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('table_closest_stars.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    next(plots)
    for row in plots:
        if (len(row[5]) == 0) or (len(row[3]) == 0):
            continue
        else:
            x.append(float(row[5]))
            y.append(float(row[3]))

fig, ax = plt.subplots()

ax.plot(x,y, '.',)
ax.set_xlabel('color index B - V')
ax.set_ylabel('absolute Mag M_V')

plt.title('Closest Stars')
plt.xticks(np.arange(-0.3, 2, 0.2))
plt.yticks(np.arange(-10, 20, 5))

plt.show()

