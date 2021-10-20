import numpy

ss = raw_input().strip().split()
ss = [int(i) for i in ss]

myArr = numpy.array(ss)
print(numpy.reshape(myArr, (3, 3)))
