import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

HMM = []
SSD = []
OGS = []

# file = open("malwareBenignScores.txt","r+")
# for line in file.read():
#     print(line)
#
# file.close()

file = open("malwareBenignScores.txt", 'r')

#malware
for line in file:
    line = line.split()
    HMM.append(line[1])
    SSD.append(line[2])
    OGS.append(line[3])


#idk why i had to do this again
file = open("malwareBenignScores.txt", 'r')
#benign
for line in file:
    line = line.split()
    #print(line)
    HMM.append(line[4])
    SSD.append(line[5])
    OGS.append(line[6])

HMM = np.array(HMM)
SSD = np.array(SSD)
OGS = np.array(OGS)
print(len(HMM))
# print(SSD)
# print(OGS)

x = [i for i in range(1, 41)]

plt.scatter(x, HMM)
#sk.svm.LinearSVC()