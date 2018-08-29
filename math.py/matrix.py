# create matrix A
#A = np.array([(1, 2, 3), (4, 5, 6)])
import numpy
A = numpy.array([(1,2,3),(4,5,6)])
print(A)

# Multiplying A by 5
B = 5 * A
print(B)

# Multiplying A by -1
B = -1 * A
print(B)

B= numpy.array([(0,2,3),(7,8,9)])

#sum A vs B
#way 1
c = A+B
print(c)
 
#way 2
d=numpy.add(A,B)
print(d)

#subtraction A-B
#way 1
s1= A-B
print(s1)

#way2
s2=numpy.subtract(A,B)
print(s2)

s3= numpy.subtract(B,A)
print(s3)

s4=A-2
print(s4)

#A*B
#create C
B1 = numpy.array([(1,2),(3,4),(5,6)])
s5 = A.dot(B1)
print(s5)

#way2
s6 = numpy.dot(A,B1)
print(s6)

#transpose matrix
A1 = numpy.transpose(A)
print (A1)

#something else
a = numpy.arange(10)
b = numpy.ones(10)
print(a,b)
c = a.dot(b)
print(c)

#inverser matrix
A2 = numpy.linalg.pinv(A)
print(A2)
#if number of row equal number of column, we use inv instead of pinv
C = numpy.array([(1,2,3),(4,5,6),(7,8,9)])
C1 = numpy.linalg.inv(C)
print(C1)