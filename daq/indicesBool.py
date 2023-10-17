import numpy as np

a = np.array([(65,34,76,98,23,65,86,5),(3,6,6,2,7,9,56,23)])
mean = a.mean()
print(mean)
#we want all values that are over the mean
print(a[a>mean])
