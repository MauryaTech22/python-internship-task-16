import numpy as np
import time

print("===== NUMPY OPERATIONS TASK =====\n")

arr1 = np.array([1, 2, 3, 4, 5])   # 1D
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])       # 2D
arr3 = np.array([[[1, 2], [3, 4]],
                 [[5, 6], [7, 8]]])  # 3D

print("1D Array:\n", arr1)
print("2D Array:\n", arr2)
print("3D Array:\n", arr3)

print("\nShape of 2D array:", arr2.shape)
print("Dimensions of 3D array:", arr3.ndim)

print("\nAddition:", arr1 + 5)
print("Multiplication:", arr1 * 2)
print("Square:", arr1 ** 2)

broadcast_result = arr2 + 10
print("\nBroadcasting (Add 10 to 2D array):\n", broadcast_result)

print("\nMean:", np.mean(arr1))
print("Median:", np.median(arr1))
print("Standard Deviation:", np.std(arr1))
print("Sum:", np.sum(arr1))
print("Maximum:", np.max(arr1))

random_array = np.random.randint(1, 100, size=(3, 3))
print("\nRandom 3x3 Array:\n", random_array)

size = 1000000

list1 = list(range(size))
list2 = list(range(size))

start = time.time()
result_list = [list1[i] + list2[i] for i in range(size)]
end = time.time()
print("\nPython List Time:", end - start)

array1 = np.arange(size)
array2 = np.arange(size)

start = time.time()
result_array = array1 + array2
end = time.time()
print("NumPy Array Time:", end - start)

numbers = np.arange(1, 11)
optimized_result = numbers * 10
print("\nVectorized Multiplication:\n", optimized_result)

print("\n===== TASK COMPLETED SUCCESSFULLY =====")
