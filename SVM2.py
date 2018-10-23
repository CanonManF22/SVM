import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

HMM = []
SSD = []
OGS = []

file = open("malwareBenignScores.txt", 'r')

#malware
for line in file:
    line = line.split()
    HMM.append([line[0], line[1]])
    SSD.append([line[0], line[2]])
    OGS.append([line[0], line[3]])


#idk why i had to do this again
file = open("malwareBenignScores.txt", 'r')
#benign
for line in file:
    line = line.split()
    #print(line)
    HMM.append([line[0],line[4]])
    SSD.append([line[0],line[5]])
    OGS.append([line[0],line[6]])

HMM = np.array(HMM)
SSD = np.array(SSD)
OGS = np.array(OGS)

#reshape
HMM = HMM.reshape(len(HMM), -1)

#0 for malware
y0 = [0 for i in range (0, 20)]
#1 for benign
y1 = [1 for i in range(20, 40)]
y = y0 + y1

#define classifier
clf = svm.SVC(kernel = 'linear')
clf.fit(HMM, y)
#print(clf.predict([40, -2.4662]))
cld.predict
