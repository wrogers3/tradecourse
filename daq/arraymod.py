import numpy as np

a = np.random.random((5,4))

print(a)
element = a[3,2]
wantedRange = a[0, 2:4]
wantedRange2 = a[1,:]
a[1,:] = 2
print(a)
