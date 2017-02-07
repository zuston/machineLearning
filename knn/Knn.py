#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

def knn(exmpleSet,dataset,labelset,k):
        if len(dataset)!=len(labelset):
            print '检查参数，标记数和数据集不对等'
            return

        dset = np.array(dataset)
        # 一维数组
        eset = np.array(exmpleSet)

        res = (((dset-eset)**2).sum(axis=1))**0.5
        index = np.argsort(res)
        resCount = {0:0,1:0}
        for c in range(k):
            labelFlag = labelset[index[c]]
            resCount[labelFlag] += 1

        # print resCount
        return 0 if resCount[0]>resCount[1] else 1

def show(exmpleSet,data,labelset,predictLabel):
    mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
    index=0
    for td in data:
        plt.plot(float(td[0])/10,float(td[1])/10,mark[labelset[index]],markersize=10)
        index += 1
    plt.plot(float(exmpleSet[0])/10,float(exmpleSet[1])/10,'pr',markersize=15)
    plt.show()

if __name__ == '__main__':
    exmpleSet = [3,2]
    dataset = [[8,3],[10,1],[45,32],[78,34],[9,18],[23,45],[34,45],[12,19]]
    labelset = [0,0,0,0,1,1,1,1]
    predictLable =  knn(exmpleSet,dataset,labelset,5)
    show(exmpleSet,dataset,labelset,predictLable)
    print predictLable