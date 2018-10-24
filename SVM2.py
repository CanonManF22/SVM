import numpy as np
from matplotlib import style
style.use("ggplot")
from sklearn import svm

data = []

file = open("malwareBenignScores.txt", 'r')

#malware
for line in file:
    line = line.split()
    data.append([float(line[1]), float(line[2]), float(line[3])])

#idk why i had to do this again
file = open("malwareBenignScores.txt", 'r')
#benign
for line in file:
    line = line.split()
    data.append([float(line[4]), float(line[5]), float(line[6])])

data = np.array(data)
#reshape
data = data.reshape(len(data), -1)

#0 for malware
y0 = [0 for i in range (0, 20)]
#1 for benign
y1 = [1 for i in range(20, 40)]
y = y0 + y1

#define classifier
clf = svm.SVC(kernel = 'linear')
clf.fit(data, y)
w = clf.coef_[0]
print(w)
print(clf._get_coef())


