### Ref:- https://www.dezyre.com/article/100-data-science-interview-questions-and-answers-general-for-2018/184
		##https://codingcompiler.com/python-coding-interview-questions-answers/
		##https://www.educative.io/blog/python-interview-questions?https://www.educative.io/courses/grokking-the-object-oriented-design-interview?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=blog-dynamic&gclid=CjwKCAjwv4_1BRAhEiwAtMDLsploTI87NHt3Q0hE89u0GNUcVs2GHkfjxvD29hdkoMUjpCoxhN-7FRoCB-MQAvD_BwE#q1
		##https://www.educative.io/blog/python-interview-questions?https://www.educative.io/courses/grokking-the-object-oriented-design-interview?aid=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=blog-dynamic&gclid=CjwKCAjwv4_1BRAhEiwAtMDLsploTI87NHt3Q0hE89u0GNUcVs2GHkfjxvD29hdkoMUjpCoxhN-7FRoCB-MQAvD_BwE
		
################################################################################################
cont ... 200426 -- https://codingcompiler.com/python-coding-interview-questions-answers/
till 15) How to generate random numbers in Python?
################################################################################################


##How to convert a list into a string?
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
print(listAsString)
#--------------------------------------------------
#How to convert a list into a tuple?
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
type(weekdays)
type(listAsTuple)
#--------------------------------------------------
#How to convert a list into a set?
#Dictionaries and sets are almost identical, except that sets do not actually contain values: a set is simply a collection of unique keys, used in set operations 
weekdays = ['sun','mon','tue','wed','thu','fri','sat','sun','tue']
listAsSet = set(weekdays)
print(listAsSet)
#--------------------------------------------------
#How to count the occurrences of a all element in the list?
weekdays = ['sun','sun','mon','tue','wed','thu','fri','sat','sun','tue','sun','sun','mon','tue','wed','thu','fri']
x=[]
for i in weekdays:
    x.append((i,weekdays.count(i)))
set(x)
#--------------------------------------------------
#What is the output of the below program? -- ans - a
names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-2])
#--------------------------------------------------
#What is Enumerate() Function in Python? ... add sequence like ...
subjects = ('Python', 'Interview', 'Questions')
for i, subject in enumerate(subjects):
    print(i, subject)
#--------------------------------------------------
#I have ['a','a','b'] , how to gte distinct 
set(['a','a','b'])  # for list  
set(('a','a','b'))     # for tuple
set({'a':1,'a':2,'b':3}) #  for dict
#--------------------------------------------------
#how to check if one element exist/not in another list/tuple/set/dic
a=['a','b','c']
b=['b','c','d']

a_in_b=[]

for i in a:
    if i not in b:
        a_in_b.append(i)
print(a_in_b)
#--------------------------------------------------
#How do you Concatenate Strings in Python?
a=['a','b','c']
b=['b','c','d']
a=a[2]
b='b'
a+b
#--------------------------------------------------
#get 4 from dict from array --a=[(1,2),3,{'d':4},[5]]
a=[(1,2),3,{'d':4},[5]]
a[2].get('d')
a[2]['d'] #another way without get()
#--------------------------------------------------
##create a array , append element , then print LastInFirstOut
a=[(1,2),3,{'d':4},[5]]
a.append(3)
a.append(4)

for i in range(7):
    print(1)
    print("The last inserted data seqwntially ... lastInFirstOut is {seq} :- ".format(seq=str(i)) + str(a.pop()) )
#--------------------------------------------------
##create a array , insert element , then print FirstInFirstOut
##append method can be use for adding new element in the list only but by using insert we can add as well as can modify already occupied position
wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0,131.10)
wmt_stock_price_queue.insert(0,132.12)
wmt_stock_price_queue.insert(0,135)

wmt_stock_price_queue.pop()
#--------------------------------------------------
##shape of array
from numpy import array
data1d=array([1,2,3])
data2d=array([[1,2],[3,4]])
data3d = array([ [ [  [[0.1], [[0.2]]], [[0.3] ], [[0.4]], [[0.5], [0.6]] ], [[0.7], [0.8],  [1.0],[6]]    ] ])
print(data1d.shape)
print(data2d.shape)
print(data3d.shape)
#--------------------------------------------------
#get the sale on "march 10" 
f=[["march 1",100],["march 2",200],["march 10",300]]
stock_prices = []
for line in f:
        day = line[0]
        price = float(line[1])
        if day!="march 2":   
            stock_prices.append([day,price])
print(stock_prices)
# by dic 
f=[["march 1",100],["march 2",200],["march 10",300]]
stock_prices = {}
for line in f:
        day = line[0]
        price = float(line[1])
        if day!="march 2":   
            stock_prices.update( {day : price} )  #for list append , dict UPDATE
print(stock_prices)
type(stock_prices)
#--------------------------------------------------
# generating random number
# seed the pseudorandom number generator
from random import seed
from random import random
# seed random number generator
seed(2)
# generate some random numbers
print(random(), random(), random())
# reset the seed
seed(1)
# generate some random numbers... diff then before seed 1 used 
print(random(), random(), random())
# reset the seed
seed(2)
# generate some random numbers... same as 1st , seed 2 used 
print(random(), random(), random())

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)
# generate some integers
for _ in range(10):
	value = randint(0, 10)
	print(value)
#How to print sum of the numbers starting from 1 to 100?
sum(range(1,101)) # range goes till 99
#--------------------------------------------------
#What is the output, Suppose list1 is [1, 3, 2], What is list1 * 2?
a=[1,2]
a*2 ## [1,2,1,2]
#--------------------------------------------------
#) What is the output when we execute list(“hello”)?
list("hello") # ['h', 'e', 'l', 'l', 'o']

# Can you write a program to find the average of numbers in a list in Python?
a=[1,2,3]
avg=sum(a)/len(a)
print(avg)

#Write a program to reverse a number in Python?
