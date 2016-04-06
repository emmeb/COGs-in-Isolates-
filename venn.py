import pylab as plt
from matplotlib_venn import venn3
set1 = set(['A', 'B', 'C', 'D'])
set2 = set(['B', 'C', 'D', 'E'])
set3 = set(['C', 'D',' E', 'F', 'G'])

venn3([set1, set2, set3], ('Gene1', 'Gene2', 'Gene3'))
plt.show()
