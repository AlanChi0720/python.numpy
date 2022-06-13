import numpy as np
# 逐元運算 elementtwise 針對每個資料逐一進行運算
# data= np.array([3,2,10])
# data2= np.array([1,3,6])
# result= data + data2
# print(result)

# 矩陣運算 matrix
# 內積
# data1 = np.array([
#     [1,2]
# ])
# data2 = np.array([
#     [1,2,3],[2,2,2]
# ])
# print(data1@data2) == data1.dot(data2)
# 1*2 @ 2*3 = 1*3 
#外積
#n np.outer(data1,data2)  ex: 4*1 外積 1*3 = 4*3
# ex: 1*2 outer 2*3 = 2*6

# 統計運算 statisuic
# data = np.array([
#     [2,1,7],
#     [3,-5,8]
# ])
# data.sum(axis=1)
# axis=0 計算 column, axis=1 計算 row
# data.min() 全部中最小值
# data.cumsum() 逐值累積
# data.mean() 平均數
# data.std() 標準差