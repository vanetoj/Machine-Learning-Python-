import numpy as np
x=np.random.randint(0,20,15)
print("The original array is:",x)
print ("The most frequent value is : ")
print(np.bincount(x).argmax())

