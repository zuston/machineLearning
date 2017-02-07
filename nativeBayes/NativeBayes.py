#coding:utf-8
__author__ = 'zuston'

from numpy import *
from math import log as lg


def createData():
    postList = [
        ['dog', 'problems', 'fool'],
        ['fool', 'fuck', 'ok'],
        ['gay', 'beach', 'dog'],
        ['hate', 'c', 'fool'],
        ['kill', 'problems', 'shut'],
        ['heal', 'fuck', 'mom'],
    ]

    labels = [0,1,1,0,1,1]
    return postList,labels

def createSet(dataset):
    wordSet = set([])
    for document in dataset:
        wordSet = wordSet | set(document)
    return list(wordSet)

def diffSet(wordSet,inputList):
    returnVec = [0]*len(wordSet)
    for word in inputList:
        if word in wordSet:
            returnVec[wordSet.index(word)] = 1
        else:
            raise Exception('error,exist the unused word')
    return returnVec

def trainNativeBayes(tranList,classList):
    lenTranList = len(tranList)
    listLen = len(tranList[0])
    PA = sum(classList)/float(lenTranList)
    PB = 1.0 - PA
    P0Vec = ones(listLen)
    P0 = 2.0
    P1Vec = ones(listLen)
    P1 = 2.0
    for i in range(lenTranList):
        if classList[i] == 1:
            P1Vec += tranList[i]
            P1 += sum(tranList[i])
        else:
            P0Vec += tranList[i]
            P0 += sum(tranList[i])

    P1res = log(P1Vec/P1)
    P0res = log(P0Vec/P0)
    return P1res,P0res,PA

def classify(needDate,P1res,P0res,PA):
    p1 = sum(needDate*P1res) + lg(PA)
    p0 = sum(needDate*P0res) + lg(1-PA)
    return 1 if p1 > p0 else 0



def testNativeBayes():
    dataList,labelList = createData()
    transList = list()
    wordSet = createSet(dataList)
    for i in dataList:
        transList.append(diffSet(wordSet,i))
    P1res, P0res, PA = trainNativeBayes(transList,labelList)

    classifyList = ['hate', 'mom', 'fuck']
    wordsVec = diffSet(wordSet, classifyList)

    return classify(wordsVec,P1res,P0res,PA)

if __name__ == '__main__':
    print testNativeBayes()