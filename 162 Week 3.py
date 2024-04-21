import numpy as np
# step 1: create a 2d array that is a 5x5 with numpy
array_1 = np.round(np.random.rand(5, 5), 2)
# step 2: print the whole array
print(array_1)
# step 3: print the number that is in the 2nd row, 3rd column
print(array_1[1, 2])
# step 4: print the sum of all elements in the array
print(np.round(np.sum(array_1), 2))
# step 5: print the mean of each row in the array
print(np.mean(array_1, axis=1))
# step 6: print the max value of each column of the array
print(np.max(array_1, axis=0))

