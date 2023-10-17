"""
#Series结构
#ser=pd.Series(data,index=idx)
data:
    1.An ndarray
    2.A Python dictionary
    3.标量值
"""
import pandas as pd
import numpy as np

#编号使用numpy.ndarray
np.random.seed(100)
ser=pd.Series(np.random.rand(7))
print(f'\n ser:\n{ser}')

#使用Python字典
dic={'US'     :'dollar',
      'UK'     :'pound',
      'Germany':'euro',
      'Mexico' :'peso',
      'Nigeria':'naira',
      'China'  :'yuan',
      'Japan'  :'yen'
      }
Dict_Series=pd.Series(dic)
print(f'\n Dict_Series:\n{Dict_Series}')

#使用标量值
dogSeries=pd.Series('Chihuahua',index=['breed','countryOfOrigin','name','gender'])
print(f'\ndogSeries:\n{dogSeries}')
