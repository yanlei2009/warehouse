import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

index=np.arange(5)
varlues=[1,2,3,4]
plt.bar(index,varlues)
plt.xticks(index+1,['A','B','C','D'])
plt.show()