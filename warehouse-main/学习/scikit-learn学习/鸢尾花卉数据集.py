from sklearn import datasets
import matplotlib.pyplot as plt

iris=datasets.load_iris()
x=iris.data[:,0] #x轴
y=iris.data[:,1] #y轴
species=iris.target
x_min,x_max=x.min()-0.5,x.max()+0.5
y_min,y_max=y.min()-0.5,y.max()+0.5
plt.figure()
plt.title('Iris Dataset - Classification By Sepal Sizes')
plt.scatter(x,y,c=species)
plt.xlabel('Speal length')
plt.ylabel('Speat width')
plt.xlim(x_min,x_max)
plt.ylim(y_min,y_max)
plt.xticks()
plt.yticks()
plt.show()