import numpy as np

#takes in a list
print (np.array([(2,3,4), (5,6,7)]))
#this is 1d
print (np.empty(5))
#this is 2d
print (np.empty(5, 4))
#this will have depth 3, 5 rows, 4 columns
print (np.empty(5, 4, 3))
#this sets a 2d array with all elements as 1
print(np.ones((5,4)))
# sets a 2d array with rng between 0 and 1
#also these arent tuples
print(np.random.random(5,4))
#normal distrubution 
print(np.random.normal(size=(2,3)))

#you already know what random.randint() does
