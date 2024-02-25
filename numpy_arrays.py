# numpy in python

# Numpy is an implementation of array in python
# Python lists are built in, but they are slow
# Numpy array or ndarray are faster because they are arranged in a
# contigious memory location on the memory
# Numpy is partially written in Python but more performance heavy
# algo of numpy are written in C/C++

import numpy as np

# Scalar array
arr_0D = np.array(16)
print(arr_0D)

# 1D array
arr_1D = np.array([0,1,2,3,4,5,6])
print(f"{arr_1D} : Type {type(arr_1D)}")

print(arr_1D[3]) # indexing
print(arr_1D[1:5]) # slicing
# Note: indexing and slicing not allowed in Scalar array

# 2D array
arr_2D = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(f"{arr_2D} of shape: {arr_2D.shape}")

# Memory View
arr_2D_memoryview = arr_2D.data
print(f"{arr_2D_memoryview} : Type {type(arr_2D_memoryview)}")
print(f"is contiguous: {arr_2D_memoryview.contiguous}")
print(f"size: {arr_2D_memoryview.itemsize}")

print(f"{type(arr_2D_memoryview.obj)}")

# Change Data using memoryview
arr_2D_memoryview.obj[2,1] = 99
print(arr_2D)

print(arr_2D_memoryview.__getitem__((2,1))) # underlying functionality used in slicing
print(arr_2D_memoryview.tobytes()) # return data in array buffer as byte string

# basic data types

# i - int
# b - bool
# u - unsigned int
# c - complex float
# f - float
# s - string

my_array = np.array([1,2,3,4,5,6])
print(f"{my_array} has dtype: {my_array.dtype}") # int64
print(type(my_array[0]))
print(my_array[0] + my_array[1]) # sum

my_array = np.array([1,2,3,4,5,"6"])
print(f"{my_array} has dtype: {my_array.dtype}") #<U21
# '<' : Little endian; 'U' : unicode; '21' : 21 characters
print(type(my_array[0]))
print(my_array[0] + my_array[1]) # string concat

my_array = np.array([0,1,2,3,4,5,6], dtype=np.complex128)
print(f"{my_array} has dtype: {my_array.dtype}")

my_array = np.array([0,1,2,3,4,5,6+9j])
print(f"{my_array} has dtype: {my_array.dtype}")

# copy creates new numpy array
arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
copy_of_arr = arr.copy()
copy_of_arr[2] = 16
print(f"original: {arr}")
print(f"copy: {copy_of_arr}")

# view gets reference to the existing numpy array
arr = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12])
view_of_arr = arr.view()
view_of_arr[2] = 16
print(f"original: {arr}")
print(f"view: {view_of_arr}")

print(arr.base) # original array itself is the base
print(view_of_arr.base) # original array is base for the view

# shape
my_array = np.array(
    [[1,   2,  3], 
    [ 4,   5,  6], 
    [ 7,   8,  9], 
    [ 10, 11, 12]]
)
print(f"{my_array} shape: {my_array.shape}")

my_5D_array = np.array(my_array, ndmin=5)
print(f"{my_5D_array} shape: {my_5D_array.shape}")

# reshape
new_arr = my_array.reshape(3,2,2)
print(f"{new_arr} shape: {new_arr.shape}")

# Iterate over ndarray
for index, data in enumerate(my_array):
    print(f"Index({index}) : {data}")

# Iterate through the scalars of nD-array 
# nested for loops, nD-array will take 'n' many 'for' loops
for i in my_array:
    for j in i:
        print(j)

# nditer is faster than using 'n' many 'for' loops
for i in np.nditer(my_array):
    print(i)

# slicing
print(my_array[:,1])
print(my_array[:,0:2])
print(my_array[2,:])
print(my_array[:,::-1]) 

# Joining ndarrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2)) # Joining 1D arrays
print(arr)

arr1 = np.array([[1, 2, 3],[7, 8, 9]])
arr2 = np.array([[4, 5, 6],[10, 11, 12]])
arr = np.concatenate((arr1, arr2)) # Joining 2D arrays
print(arr)

arr = np.stack((arr1, arr2), axis=1)
print(arr)

# search in ndarray
arr = np.array([1,2,3,2,4,5,2,6])
x = np.where(arr == 2)
print(x)

x = np.where(arr%2 == 0)
print(x)

if 2 in arr:
    print("found 2")

# sort
sorted_arr = np.sort(arr) # makes a copy
print(f"original: {arr}")
print(f"sorted: {sorted_arr}") 

