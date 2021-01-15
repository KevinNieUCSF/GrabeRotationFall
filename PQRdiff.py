import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from collections import OrderedDict
"""This script is to be run in the location where both PQR files are located, include ".pdb" when it asks for input or manually input in this script.
The script compares two PQR files to find differences in charge assignment, important for APBSmem gating charge calculations"""

fppqr1 = open(input("Open Conformation:"),'r')
fppqr2 = open(input('Closed conformation:'),'r')

charge_pes_res_list1 = {}
charge_pes_res_list2 = {}
diffdict = {}
#sortedchargelist1 = OrderedDict()
#sortedchargelist2 = OrderedDict()
res = None
a=0
for line in fppqr1:
    if line[:4] == 'ATOM':
        if res == None:
            res = line.split()[4]
            charge_pes_res_list1[line.split()[4]] = float(line.split()[8])
        elif res == line.split()[4]:
            charge_pes_res_list1[line.split()[4]] += float(line.split()[8])
        elif res != line.split()[4]:
            res = line.split()[4]
            charge_pes_res_list1[line.split()[4]] = float(line.split()[8])
for line in fppqr2:
    if line[:4] == 'ATOM':
        if res == None:
            res = line.split()[4]
            charge_pes_res_list2[line.split()[4]] = float(line.split()[8])
        elif res == line.split()[4]:
            charge_pes_res_list2[line.split()[4]] += float(line.split()[8])
        elif res != line.split()[4]:
            res = line.split()[4]
            charge_pes_res_list2[line.split()[4]] = float(line.split()[8])
#for line in fppqr2:
    #if line[:4] == 'ATOM':
        #charge_pes_res_list2.append((line.split()[1],line.split()[8]))
for key in charge_pes_res_list1.keys():
    try:
        if charge_pes_res_list1[key] != charge_pes_res_list2[key]:
            try:
                a+=1
                print("These residues do not match   " + str(key) + "  " + str(charge_pes_res_list1[key]) + " Different Than " + str(charge_pes_res_list2[key]))
            except:
                pass
        diffdict[key] = charge_pes_res_list1[key] - charge_pes_res_list2[key]
    except:
        pass
print('Total Residues That Changed: '+ str(a))
"""for i in sorted(chargelist1):
    sortedchargelist1[i] = float(chargelist1[i])
for i in sorted(chargelist2):
    sortedchargelist2[i] = float(chargelist2[i])
sortedchargelist1 = sorted(chargelist1, key = lambda x: x[1])
sortedchargelist2 = sorted(chargelist2, key = lambda x: x[1])
a = 0
for i in range(len(sortedchargelist1)):
    if sortedchargelist1[i][1] != sortedchargelist2[i][1]:
        a += 1
        print(str(sortedchargelist1[i]) + "is different with" + str(sortedchargelist2[i]))
print(a)
#print(sortedchargelist1)
#print('_________________________________________________________________________________________________________')
#print(sortedchargelist2)
#print(sortedchargelist1[2][0])
for key in sortedchargelist1.keys():
    if sortedchargelist1[key] != sortedchargelist2[key]:
        print(sortedchargelist1[key])
sum = 0
for value in diffdict.values():
    sum += value
print(sum)
for i in range(len(diffdict)):
    sum += diffdict[i]
    """

#print(chargelist1)
xlim = len(diffdict)
plt.title('Per Residue Differences in Charge State')
plt.xlabel('Residue')
plt.ylabel('Charge Change (e)')
plt.ylim(-1,1)
x_ticks = np.arange(0,xlim,50)
plt.xticks(x_ticks)
x = diffdict.keys()
y = diffdict.values()
plt.plot(x,y)
plt.show()
