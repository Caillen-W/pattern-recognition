from sklearn.datasets import load_breast_cancer
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
# 加载数据
data = load_breast_cancer().data
# 数据中心化
data = pd.DataFrame(data)
data = data - data.mean()
# 求协方差矩阵
cov = 1 / np.shape(data)[0] * np.dot(np.transpose(data), data)
# 求特征值与特征向量
eigen_value, eigen_vector = np.linalg.eig(cov)
# 取特征值最大的k个特征向量作为基底矩阵
eig_pairs = [(np.abs(eigen_value[i]), eigen_vector[:,i]) for i in range(len(eigen_value))]
eig_pairs.sort(key=lambda x: x[0])
feature_matrix = np.array([eig_pairs[-i-1][1] for i in range(3)])
# 计算新基底下的数据
new_data = np.dot(feature_matrix, np.transpose(data))
# 绘制图像
x = new_data[0, :]  # [ 0  3  6  9 12 15 18 21]
y = new_data[1, :]  # [ 1  4  7 10 13 16 19 22]
z = new_data[2, :]  # [ 2  5  8 11 14 17 20 23]

# 绘制散点图
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x, y, z, c = load_breast_cancer().target)

# 添加坐标轴(顺序是Z, Y, X)
ax.set_zlabel('Z', fontdict={'size': 15, 'color': 'red'})
ax.set_ylabel('Y', fontdict={'size': 15, 'color': 'red'})
ax.set_xlabel('X', fontdict={'size': 15, 'color': 'red'})
plt.show()


