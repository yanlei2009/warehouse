import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

labels=['甲','乙','丙','丁']
values=np.array([25,25,25,25],dtype=float)
plt.pie(values,labels=labels,autopct='%1.1f%%')
plt.title('饼状图')
plt.show()