### Histograms are used to represent data given in form of some groups. X-axis is bin ranges where Y-axis is frequency. you want to represent age wise population in form of graph ? 
##then histogram suits well as it tells you how many exists in certain group range i.e. bin.
import pandas as pd
import matplotlib.pyplot as plt
X=pd.read_csv("DB_sample.csv")
Xp=X["age"]
plt.hist(Xp,bins=20)
plt.show()
###### we may have more observations for a accurate graph
