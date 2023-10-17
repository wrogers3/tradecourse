import numpy as np

a = np.random.random(5)
# you can access a list of indices with an np.array
indices = np.array([1,1,2,3])
print(a)
print(a[indices])

#calc mean with
mean = a.mean()
print(a[a<mean])
