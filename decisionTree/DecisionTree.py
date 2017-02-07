#!coding:utf-8
'''
build the decision tree
'''
from numpy import *
from math import log

def caculateShannonEnt(dataset):
    number = len(dataset)
    labelSet = {}
    for k in dataset:
        label = k[-1]
        if not labelSet.has_key(label):
            labelSet[label] = 1
        else:
            labelSet[label] += 1
    shannonEnt = 0.0
    for key,value in labelSet.items():
        currentProp = float(value)/number
        shannonEnt -= currentProp*log(currentProp,2)
    return shannonEnt


def splitDataSet(dataSet,axis,value):
    ds = []
    for key in dataSet:
        if key[axis] == value:
            tempList = key[0:axis]
            tempList.extend(key[axis+1:])
            ds.append(tempList)
    return ds

def chooseBestSplit(dataset):
    featureLen = len(dataset[0]) - 1
    baseShannon = caculateShannonEnt(dataset)
    bestValue = 0.0
    bestFeature = -1
    for i in range(featureLen):
        featureList = [temp[i] for temp in dataset]
        featureSet = set(featureList)
        currentBestShannon = 0.0
        for value in featureSet:
            splitData = splitDataSet(dataset,i,value)
            prop = float(len(splitData))/len(dataset)
            currentBestShannon += prop*caculateShannonEnt(splitData)

        ShannonGain = baseShannon - currentBestShannon
        if ShannonGain > bestValue:
            bestValue = ShannonGain
            bestFeature = i
    return bestFeature


def maxFeatures(classList):
    dictCount = {}
    for i in classList:
        if not dictCount.has_key(i):
            dictCount[i] = 1
        else:
            dictCount[i] += 1

    max = 0
    maxKey = 0
    for key,value in dictCount.items():
        if value>max:
            maxKey = key
            max = value

    return maxKey

def buildTree(dataset,labels):
    classList = [temp[-1] for temp in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]

    if len(dataset) == 1:
        return maxFeatures(classList)

    bestFeature = chooseBestSplit(dataset)
    bestLabel = labels[bestFeature]
    del(labels[bestFeature])

    currentTree = {bestLabel:{}}
    featureSet = set([temp[bestFeature] for temp in dataset])
    for key in featureSet:
        loopLabels = labels[:]
        currentTree[bestLabel][key] = buildTree(splitDataSet(dataset,bestFeature,key),loopLabels)
    return currentTree




def testCaculateShannoEnt():
    dataset = [
        [1, 1, 'ok'],
        [1, 0, 'no'],
        [0, 1, 'ok'],
        [1, 1, 'no'],
        [1, 0, 'ok'],
    ]
    return buildTree(dataset,['head big','small eye'])


if __name__ == '__main__':
    print testCaculateShannoEnt()
