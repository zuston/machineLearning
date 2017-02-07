import numpy as np
from sklearn.neighbors.nearest_centroid import NearestCentroid
import time

startTime = time.time()

file = open('YearPredictionMSD.txt','r')

lineList = []
for line in file.readlines():
    lineList.append(line)

trainningList = lineList[:463715]
testingList = lineList[463715:]

trainningLabelList = []
trainningSplitList = []
for lines in trainningList:
    trainningLabelList.append(float(lines.split(',')[0]))
    floatList = []
    for key in lines.split(',')[1:]:
        floatList.append(float(key))
    trainningSplitList.append(floatList)

X = np.array(trainningSplitList)
Y = np.array(trainningLabelList)

clf = NearestCentroid()

clf.fit(X,Y)
fitTime = time.time()
print 'fitting time is : '+str(fitTime-startTime)
sumNumber = len(testingList)
errorNumber = 0

for line in testingList:
    lineSplit = line.split(',')
    label = float(lineSplit[0])
    vector = lineSplit[1:]
    vetorFloat = []
    for key in vector:
        vetorFloat.append(float(key))
    predict = clf.predict([vetorFloat])[0]
    if predict==label:
        pass
    else:
        errorNumber += 1
print sumNumber
print errorNumber
# print 'the rate is : '+str(((sumNumber-errorNumber)/sumNumber))
