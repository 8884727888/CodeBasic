#used to convert categorical data, or text data, into numbers, which our predictive models can better understand.
from sklearn import preprocessing
x=["paris", "paris", "tokyo","Tokyo", "amsterdam"]
le = preprocessing.LabelEncoder()
le.fit(x)
print(list(le.classes_))  # get classes in object
y= le.transform(["paris", "Tokyo","tokyo", "amsterdam"])
print(x)
print(y)
y_inv=list(le.inverse_transform([0,1,2,3]))  ## getting bacl classses
print(y_inv)

