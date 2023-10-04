'''
np.zeros
np.ones
np.diag
np.arange
np.linespace
np.meshgrid
np.fromfunction
'''
import numpy as np
def print_list(fname,name):
    print(fname,':')
    print(name)
    print(f'dtype: {name.dtype}')
    print(f'shape: {name.shape}')
    print(f'size:  {name.size}')
    print(f'ndim:  {name.ndim}')
    print(f'nbytes:{name.nbytes}')
    print()

zeros=np.zeros((3,3))
ones=np.ones((3,3))
diag=np.diag([1,2,3])
arange=np.arange(1,4,1)
linespace=np.linspace(1,3,3)
meshgrid=np.array(np.meshgrid([1,2,3],[3,2,1],))


print_list('zeros()',zeros)
print_list('ones()',ones)
print_list('diag()',diag)
print_list('arange()',arange)
print_list('linespace()',linespace)
print_list('meshgrid()',meshgrid)