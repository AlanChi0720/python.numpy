import numpy as np
# 分割 splitting
# 切割第一個維度 np.vsplit((陣列, 數量)) 
# 切割第二個維度 np.vsplit((陣列, 數量)) 

arr = np.array([
    [1,2,3,4,5,6,7,8],
    [5,6,7,8,1,2,3,4]
]) #2*8

result1 = np.vsplit(arr,2)
result2 = np.hsplit(arr,4)

print(result1)
print(result2)

