import matplotlib.pyplot as plt
import numpy as np
import math
import fractions
import balmer_lines_a as a
import balmer_lines_b as b

temp = np.linspace(0,30000,100)
y = []

for t in temp:
    boltzmann = a.boltzmann(t)
    fraction = fractions.Fraction(boltzmann)
    fraction = str(fraction).split('/')
    if len(fraction) > 1:
        n_s2 = int(fraction[0])
        total = int(fraction[0]) + int(fraction[1])
        # n_s2/(n_s1 + n_s2)
    else:
        y.append(0)
        continue
    
    saha = b.saha(t)
    fraction_saha = fractions.Fraction(saha)
    fraction_saha = str(fraction_saha).split('/')
    if len(fraction_saha) > 1:
        total = int(fraction_saha[0]) + int(fraction_saha[1])
        n_H0 = int(fraction_saha[1])
        n_Hplus = int(fraction_saha[0])
        n_H = total
    else:
        y.append(1)
        continue

    y.append((n_H0 * n_s2) / (n_H * 10**17))

fig, ax = plt.subplots()

ax.plot(temp,y, '.')
ax.set_xlabel('Temperatur [K]')
ax.set_ylabel('Combined density')

plt.show()