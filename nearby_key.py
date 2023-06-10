import numpy

clist = []
for i in range(1, 11, 2):#-9 ~ 9
    clist.append([i, 6])
for i in range(0, 10, 2):
    clist.append([i, 3])
for i in range(0,8,2):
    clist.append([i,0])

def fitts(a,b):
    a = numpy.array(a)
    b = numpy.array(b)
    return numpy.linalg.norm(a-b)

cvalue = [0] * len(clist)
for i in range(len(clist)):
    for j in range(len(clist)):
        cvalue[i] += fitts(clist[i],clist[j])

fin = []
for i in len(clist):
    fin[i]

print(clist)
print(cvalue)
print(mini)

