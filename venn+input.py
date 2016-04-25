from matplotlib import pyplot as plt
from matplotlib_venn import venn3, venn3_circles
import numpy as np
number = []
names = []


file = open('sample.txt', 'r')
num=file.readline().strip('\n').split(',')
names = file.readline().strip('\n').split(',')
test= file.readline().strip('\n').split(',')


for item in num:
    number.append(int(item))


a = number[0]
b = number[1]
c = number[2]
d = number[3]
e = number[4]
f = number[5]
g = number[6]


v = venn3(subsets=(a,b,c,d,e,f,g), set_labels = ('A', 'B', 'C'))
v.get_label_by_id('A').set_text(names[0])
v.get_label_by_id('B').set_text(names[1])
v.get_label_by_id('C').set_text(names[2])
plt.title(test[0])
plt.show()
