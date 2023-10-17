import numpy as np

np.random.seed(693)
a = np.random.randint(0, 10, size=(5,4))

# axis 0 = row
# axis 1 = column
#sum of all elements
print(a.sum())
print(a.sum(axis=0))
print(a.sum(axis=1))
#gives us mean of entire array
# operations of mean are the same as sum 
print(a.mean())
print (a)
