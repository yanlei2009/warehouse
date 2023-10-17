import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['SimHei']

data=np.random.randint(0,100,100)
a=plt.hist(data)
plt.show()