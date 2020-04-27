#Scaling. This means that you're transforming your data so that it fits within a specific scale, like 0–100 or 0–1. You want to scale data when you're using methods based on measures of how far apart data points, like support vector machines, or SVM or k-nearest neighbors, or KNN.
#All algorithms that are distance based require scaling. Feature Scaling or Standardization: It is a step of Data Pre Processing which is applied to independent variables or features of data. It basically helps to normalise the data within a particular range. Sometimes, it also helps in speeding up the calculations in an algorithm. There are several types , std,min-max , robust ...
x = [10,2,300,400,2,30,58,39.2,12.68,8]  # test Data
mn=min(x)
mx=max(x)

scl=[]
for i in x:
    scl.append((i-mn)/(mx-mn))
print(scl)  #std Data
# by sklearn
from sklearn.preprocessing import StandardScaler
import numpy as np
sc = MinMaxScaler()
x = ([[10,2],[300,400],[2,30],[58,39.2],[12.68,8]])  # test Data, in nd required as input
xar=np.array(x)
xar.shape
sc.fit(xar)
print( sc.fit_transform(xar))
