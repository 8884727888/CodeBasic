## mean inputation 
x=[
 [2,2,3]
,['Nan','NaN',6]
,[3,6,9]
]

print(type(x))

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0 ) #In a NumPy array, axis 0 is the “first” axis. Assuming that we're talking about multi-dimensional arrays, axis 0 is the axis that runs downward down the rows.
x_imputed = imputer.fit(x) 
y=x_imputed.transform(x)
print(y)
print(y.shape)
