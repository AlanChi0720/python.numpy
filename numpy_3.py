import numpy as np
# 多微陣列都有shape 屬性
data = np.array([
    [2,4,1],
    [1,5,0]
])

data.shape # 陣列資料形狀
data.T # 陣列資料的轉置
data.T.shape # 陣列資料的轉置形狀

data.ravel() #扁平化資料 把所有資料轉化成一維

data.reshape(3,2) #重塑資料的形狀 但資料數不變
np.zeros(9).reshape(3,1,1,3)

# 初始化資料 (bounch of 0 or 1)
data = np.zeros(18).reshape(3,6)
print(data)

data = np.arange(9).reshape(3,3)
print(data)
print(data.T)