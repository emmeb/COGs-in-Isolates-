import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

##the data 
N = 5
gene1 = (20, 25, 30, 35, 27)
gene2 = (25,32,34,20,25)

## variables 
index = np.arange(N)
width = 0.35



rects1 = ax.bar(index, gene1, width, color = 'b', label ='gene1')
rects2 =ax.bar(index + width, gene2, width, color ='r', label ='gene2')

##axes and labels 
ax.set_xlabel('Feature')
ax.set_ylabel('Feature Counts')
ax.set_xticks(index + width)
ax.set_xticklabels(('Carbohydrates', 'Phosophorous Metabolism', 'Sulfer Metabolism', 'Amino Acids & Derivatives', 'Stress Responsess'))
ax.legend()
for tick in ax.get_xticklabels():
    tick.set_rotation(45)


plt.plot()
plt.show()
