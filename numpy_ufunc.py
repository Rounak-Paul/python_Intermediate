# NumPy ufunc

# ufunc stands for "Universal Functions" and they are NumPy functions that 
# operate on "ndarray"

# ufunc is used to implement "vectorization" in NumPy which is fater than
# iterating over elements in a loop

import numpy as np

# Example Loop add vs ufunc add
arr_a = np.array([1, 2, 3, 4, 5, 6])
arr_b = np.array([6, 5, 4, 3, 2, 1])

# Loop add
out = []
for a, b in zip(arr_a, arr_b):
    out.append(a + b)
print(out)

# ufunc add
out = np.add(arr_a, arr_b)
print(out)

# Create ufunc
def my_add(x, y): # this is defined for scaler, with vectorization can work on arr
    return x + y

my_add = np.frompyfunc(my_add, 2, 1) # (function, no. of input arr, no. of output arr)

print(my_add(1, 2))
print(my_add(arr_a, arr_b))

print(type(my_add))

# NumPy built-in ufunc


out = np.add(arr_a, arr_b); print(out)              # add 
out = np.subtract(arr_a, arr_b); print(out)         # subtract
out = np.multiply(arr_a, arr_b); print(out)         # multiply
out = np.divide(arr_a, arr_b); print(out)           # divide
out = np.power(arr_a, arr_b); print(out)            # power
out = np.mod(arr_a, arr_b); print(out)              # remainder
out = np.divmod(arr_a, arr_b); print(out)           # quotient

# complex array
arr_c = np.array([1+2j, 4+5j, -7+5j, -32j, 9-34j])

out = np.abs(arr_c); print(out)                     # absolute
out = np.angle(arr_c, deg=True); print(out)         # angle

arr_d = np.random.uniform(  low=-5, 
                            high=5, 
                            size=10); print(arr_d)
out = np.trunc(arr_d); print(out)                   # trunc
out = np.around(arr_d); print(out)                  # round
out = np.floor(arr_d); print(out)                       # round


