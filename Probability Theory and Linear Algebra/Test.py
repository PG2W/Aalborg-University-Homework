import numpy as np

# Scalar
s = 2

# Test numpy variables
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Scalar-Vector Multiplication of a and b
c = s * a * b
print("Scalar-Vector multiplication of a and b = ", c)

# Inner product of a and b
d = np.inner(a, b)
print("Inner product of a and b = ", d)