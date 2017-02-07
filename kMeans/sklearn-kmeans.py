#coding:utf-8
from sklearn.cluster import KMeans
import numpy as np

#分析中国队足球为亚洲第几梯队
rankList = [
    [1,1,0.1],
    [0.3,0,0.19],
    [0,0.15,0.13],
    [0.24,0.76,0.25],
    [0.3,0.76,0.06],
    [1,1,0],
    [1,0.76,0.5],
    [1,0.76,0.5],
    [0.7,0.76,0.25],
    [1,1,0.5],
    [1,1,0.25],
    [1,1,0.5],
    [0.7,0.76,0.5],
    [0.7,0.68,1],
    [1,1,0.5]
]
x = np.array(rankList)
kmeans = KMeans(n_clusters=3, random_state=0).fit(x)

print kmeans.labels_
# print kmeans.predict([[0, 0], [4, 4]])
print kmeans.cluster_centers_
