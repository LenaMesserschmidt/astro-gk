import matplotlib.pyplot as plt
import numpy as np
import math
import fractions

# Elektronendichte (in n/m^3)
#n_E = pow(10,-5)

# Boltzmann-Konstante (in J/K)
K = 1.38 * pow(10, -23)

# Ionisationsenergie Wasserstoff (in eV)
X = 13.6
# in J
X = X  * 1.6 * pow(10,-19)

# Planck-Konstante (in Js)
h = 6.626 * pow(10,-34)

# Masse H-Elektron (in kg)
m_E = 0.91 * pow(10,-30)

# mittlere kinetische Energie (in J)
def k_B(T):
    return (3/2) * K * T

# Saha-Gleichung
def saha(T):
    if T != 0:
        n_E = 10**(-3)/K * T
        zaehler = (2 * math.pi * m_E * K * T)**(3/2)
        nenner = h**3
        result = (2/n_E) * (zaehler/nenner) * math.exp(-X/k_B(T))
        return result
    return 0

temp = np.linspace(0,30000,100)
y = []

for t in temp:
    value = saha(t)
    fraction = fractions.Fraction(value)
    fraction = str(fraction).split('/')
    if len(fraction) > 1:
        total = int(fraction[0]) + int(fraction[1])
        y.append(int(fraction[1])/total)
    else:
        y.append(1)


fig, ax = plt.subplots()

ax.plot(temp,y, '.')
ax.set_xlabel('Temperatur [K]')
ax.set_ylabel('Ionisierungsgrad')

plt.show()