import matplotlib.pyplot as plt
import numpy as np
import math
import fractions

# Boltzmann-Konstante
K = 1.38 * pow(10, -23)

temp = np.linspace(0,80000,16)
y = []


# mittlere kinetische Energie
def k_B(T):
    return (3/2) * K * T

# Boltzmann-Gleichung
def boltzmann(T):
    if k_B(T) != 0:
        result = (8/2) * math.exp(-10.2/(k_B(T)*6.242 * pow(10,18)))
        return result
    return 0

# calculate y values
for t in temp:
    # n_s2/n_s1
    value = boltzmann(t)
    fraction = fractions.Fraction(value)
    fraction = str(fraction).split('/')
    if len(fraction) > 1:
        total = int(fraction[0]) + int(fraction[1])
        # n_s2/(n_s1 + n_s2)
        y.append(int(fraction[0])/total)
    else:
        y.append(value)


fig, ax = plt.subplots()

ax.plot(temp,y, '.')
ax.set_xlabel('Temperatur [K]')
ax.set_ylabel('Anregungsgrad s=2 Wasserstoff')

plt.show()