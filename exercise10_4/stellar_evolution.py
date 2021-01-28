import matplotlib.pyplot as plt
import numpy as np

x = []
y = []
z = []
data = []

key_names = ['step', 'age', 'mass', 'luminosity', 'radius', 'T_surface', 'T_central', 'density', 'pressure', 'central_electron_degeneracy', 'hydrogen_fraction', 'helium_fraction', 'carbon_fraction', 'nitrogen_fraction', 'oxygen_fraction', 'time_dyn', 'time_KH', 'time_nuc', 'L_pp', 'L_CNO', 'L_3alpha', 'L_z', 'L_v', 'M_He', 'M_C', 'M_O', 'R_He', 'R_C', 'R_O']

with open('exercise10_4/summary.txt','r') as txtfile:
    lines = txtfile.readlines()
    for row in lines:
        values = []
        raw_values = row.split()
        for v in raw_values:
            values.append(float(v))
        data.append(dict(zip(key_names, values)))
    

print(data[0])

for d in data:
    x.append(d['step'])
    y.append(d['age'])

fig, ax = plt.subplots()

ax.plot(x,y, '.')
#ax.plot(x,z, '-')
#ax.set_xlabel('step')
#ax.set_ylabel('radius')

#plt.title('Closest Stars')
#plt.xticks(np.arange(-0.3, 2, 0.2))
#plt.yticks(np.arange(-10, 20, 5))

plt.show()
