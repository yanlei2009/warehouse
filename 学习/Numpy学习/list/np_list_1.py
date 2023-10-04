'''
np.array()
Shape
Size
Ndim
nbytes
dtype

'''

import numpy as np
def print_list(name):
    print(name)
    print(f'dtype: {name.dtype}')
    print(f'shape: {name.shape}')
    print(f'size:  {name.size}')
    print(f'ndim:  {name.ndim}')
    print(f'nbytes:{name.nbytes}')
    print()


nlist1=np.array([i
                for i in range(0,10)])

nlist2=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9,]],dtype=int)

nlist3=np.array([],dtype=float)

print_list(nlist1)
print_list(nlist2)
print_list(nlist3)