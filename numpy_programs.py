#basic arithmetic operations using numpy
import numpy as np

a=np.array([1, 2, 3, 4, 5])
b=np.array ([10 ,20, 30, 40, 50])
print("array a:",a)
print("array b:",b)
print("Addition:",a+b)
print("Subtraction:",a-b)
print("Multiplication:",a*b)
print("division:",a/b)

# arrray slicing and reshaping
print("First 3 elements of a:",a[:3])
print(" 2 elements of b:",b[-2:])

c=np.arange(1,10)
print("original c values:",c)
print("reshaped value as 3*3:",c.reshape(3,3))

#aggregation and statistivcal function
a=np.array([2, 5, 6, 4, 3, 2])
print("sum:",np.sum(a))
print("mean:",np.mean(a))
print("min:",np.min(a))
print("max:",np.max(a))