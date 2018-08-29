# create matrix a
#a = np.array([(1, 2, 3), (4, 5, 6)])
import numpy
a = numpy.array([(1,2,3),(4,5,6)])
print(a)

# Multiplying a by 5
b = 5 * a
print(b)

# Multiplying a by -1
b = -1 * a
print(b)

b= numpy.array([(0,2,3),(7,8,9)])

#sum a vs b
#way 1
c = a+b
print(c)
 
#way 2
d=numpy.add(a,b)
print(d)

#subtraction a-b
#way 1
s1= a-b
print(s1)

#way2
s2=numpy.subtract(a,b)
print(s2)