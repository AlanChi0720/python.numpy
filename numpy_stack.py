import numpy as np
# 合併 stacking

# 合併第一個維度 np.vstack(()) 裡面放tuople(不可改變
# 合併第二個維度 np.hstack(())

arr1 = np.array([
    [1,2,3],
    [4,5,6]
])
arr2 = np.array([
    [7,8,9],
    [10,11,12]
])
arr3 = np.array([
    [2,3],
    [4,5]
])
# result1 = np.vstack((arr1,arr2,arr3))
result2 = np.hstack((arr1,arr2,arr3))

# print(result1)
print(result2)