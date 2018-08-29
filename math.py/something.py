import numpy as np
x = np.array([[1,2,3,3]]).T
y =np.array([4,8,12,13]).T
#print(x.shape[0])
#print(np.arange(x.shape[0]))
one=np.ones((x.shape[0], 1))
Xbar =np.concatenate((one, x), axis = 1)

print(Xbar.T)
print(Xbar)
print(Xbar.dot(Xbar.T))
print(np.dot(Xbar.T,Xbar))

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
w = np.dot(np.linalg.pinv(A), b)
#print(A)
#print(b)