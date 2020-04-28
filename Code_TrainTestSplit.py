##Train/Test Split.The training set contains a known output and the model learns on this data ,we have the test dataset (or subset) in order to test our model's prediction .
import pandas as pd
from sklearn.model_selection import train_test_split
df=pd.read_csv("DB_TrainTestSplit.csv",index_col = None)
x=df.iloc[:,:2]
y=df.iloc[:,3:]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 11)

print(len(x))
print(len(x_train))
print(len(x_test))
print(type(x_test))
print(y.shape)

### by list as input
x=[[1,100],[2,200],[3,300],[4,400],[5,500],[6,600]]
y=[1,1,0,1,0,1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 11)
print(x_train)
type(x_test)
