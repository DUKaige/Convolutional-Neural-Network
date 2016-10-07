__author__ = 'liukaige'
import math
def sigmoid(x):
    return 1/(1-math.e**(-x))
def indexesForKernel(size,kernelSize,index):
    x = index%(size - kernelSize + 1)
    y = (index - x)/(size - kernelSize + 1)
    result = []
    for j in range(y,y +kernelSize):
        for i in range(x,x+kernelSize):
            result.append(i + size * j)
    return result



def sortOutMultiplatedLinks(number,listOfIndexes):#must from the narrowest to the broadest
    tmp = number
    result = []
    for i in range(0,len(listOfIndexes)):
        result.append(tmp%listOfIndexes[i])
        tmp = (tmp - tmp%listOfIndexes[i])/listOfIndexes[i]
    return result

#print sortOutMultiplatedLinks(101,[2,3,4,5])
#for example the output of this is [1,2,0,4]
#it means 101 = 1*1 + 2*2 + 0*2*3 + 4*2*3*4