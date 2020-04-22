###logistic regression model in Python in order to determine whether candidates would get admitted to a prestigious university.
###Admitted denoted by 1  vs. Rejected by 0 .
## the  dataset contains appx 40 observations. you need to have more records for accuracy 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import seaborn as sn
import matplotlib.pyplot as plt
## creating data, series 
candidates = {'Score':[781, 751, 691, 711, 681, 731, 691, 721, 741, 691, 611, 691, 711, 681, 771, 611, 581, 651, 541, 591, 622, 602, 552, 552, 572, 672, 662, 582, 652, 662, 642, 622, 662, 662, 682, 652, 672, 582, 592, 692, ] ,
              'gpa': [5,4.9,3.3,3.7,3.7,3.7,2.3,3.3,3.3,1.7,2.9,3.7,3.7,3.3,3.3,3,2.7,3.7,2.8,2.3,3.3,2,2.3,2.7,3,3.3,3.6,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.2,1.7,4],
              'Experience': [4,4,3,5,4,6,2,4,5,1,3,5,6,4,3,1,4,7,2,3,2,1,4,1,2,6,4,3,6,5,1,2,4,6,5,1,2,1,4,5],
              'admitted_Yes_1': [1,1,0,1,0,1,0,1,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,0,0,0,0,1]
              }
### to dataframe
df = pd.DataFrame(candidates,columns= ['Score', 'gpa','Experience','admitted_Yes_1'])
### split , dep and indep variables
X = df[['Score', 'gpa','Experience']]
y = df['admitted_Yes_1']
###  separating train and test set 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.15,random_state=28)
### applying log reg.
logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)
#### evaluation 
print('Evaluated Accuracy is : ',metrics.accuracy_score(y_test, y_pred))
####Accuracy  can be improved using more variables and observations 