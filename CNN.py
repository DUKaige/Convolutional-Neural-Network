__author__ = 'liukaige'
import random
import math
import os
import numpy
from PIL import Image
import csv
from tools import *
from Classes import *

def inputOutputInArray():
    images  = os.listdir("handwritings")
    allInputs = []
    allOutputs = []
    for imageName in images:
        if imageName != ".DS_Store":
            image = Image.open("handwritings/"+imageName)
            imageArray = image.load()
            print imageName
            for x in range(0,imageArray.xsize,28):
                for y in range(0,imageArray.ysize,28):
                    small = []
                    notall0 = False
                    for i in range(0,28):
                        for j in range(0,28):
                            if imageArray[i + x,j + y] != 0:
                                notall0 = True
                            small.append(imageArray[i + x,j + y]/256.0)
                    if notall0:
                        allInputs.append(small)
                        ooo = [0,0,0,0,0,0,0,0,0,0]
                        ooo[eval(imageName[-5])] = 1.0
                        allOutputs.append(ooo)
    return (allInputs,allOutputs)

def inputOutputInNumber():
    images  = os.listdir("handwritings")
    allInputs = []
    allOutputs = []
    for imageName in images:
        if imageName != ".DS_Store":
            image = Image.open("handwritings/"+imageName)
            imageArray = image.load()
            print imageName
            for x in range(0,imageArray.xsize,28):
                for y in range(0,imageArray.ysize,28):
                    small = []
                    notall0 = False
                    for i in range(0,28):
                        for j in range(0,28):
                            if imageArray[i + x,j + y] != 0:
                                notall0 = True
                            small.append(imageArray[i + x,j + y]/256.0)
                    if notall0:
                        allInputs.append(small)
                        allOutputs.append(imageName[-5])
    return (allInputs,allOutputs)

def nearestNeighbor():
    pass







globalLayerNumber = 7



#how to check this thing:
#
def buildLeNet5():
    Nodes = [[],[],[],[],[],[],[],[]]
    emptyLink = Link(-1)
    emptyNode = Node(-1)
    #nodes
    #layer0
    for i in range(0,28):
        for j in range(0,28):
            newNode = Node(0)
            Nodes[0].append(newNode)
    #layer1
    for m in range(0,6):
        for i in range(0,24):
            for j in range(0,24):
                newNode = Node(0)
                Nodes[1].append(newNode)
    #layer2
    for m in range(0,6):
        for i in range(0,12):
            for j in range(0,12):
                newNode = Node(0)
                Nodes[2].append(newNode)
    #layer3
    for m in range(0,16):
        for i in range(0,8):
            for j in range(0,8):
                newNode = Node(0)
                Nodes[3].append(newNode)

    #layer4
    for m in range(0,16):
        for i in range(0,4):
            for j in range(0,4):
                newNode = Node(00)
                Nodes[4].append(newNode)

    #layer5
    for m in range(0,120):
        newNode = Node(0)
        Nodes[5].append(newNode)

    #layer6
    for m in range(0,84):
        newNode = Node(0)
        Nodes[6].append(newNode)

    #layer7
    for m in range(0,10):
        newNode = Node(0)
        Nodes[7].append(newNode)

    Links = [[],[],[],[],[],[],[]]

    #links
    #layer0-1
    for k in range(0,6):
        for i in range(0,25):
            Links[0].append(Link(0))
    for i in range(0,576):
        indexes = indexesForKernel(28,5,i)
        for j in range (0,25):
            for kernelNumber in range(0,6):
                Nodes[0][indexes[j]].post.append(Links[0][kernelNumber*25 + j])
                Nodes[1][i + kernelNumber * 24 * 24].pre.append(Links[0][kernelNumber*25 + j])
                Links[0][kernelNumber*25 + j].prePostTuples.append((Nodes[0][indexes[j]],Nodes[1][i + kernelNumber * 24 * 24]))

    #layer1-2
    for k in range(0,4):
        newLink = Link(1)
        Links[1].append(newLink)
    for i in range(0,6):
        for y in range(0,12):
            for x in range(0,12):
                indexes = [0,0,0,0]
                indexes[0] = 2*x + 48 * y
                indexes[1] = 2*x + 1 + 48*y
                indexes[2] = 2*x + 48*y + 24
                indexes[3] = 2*x + 48*y + 25
                for kernelNumber in range(0,6):
                    for k in range(0,4):
                        Nodes[1][kernelNumber*576 + indexes[k]].post.append(Links[1][k])
                        Nodes[2][kernelNumber*144 + y*12 + x].pre.append(Links[1][k])
                        Links[1][k].prePostTuples.append((Nodes[1][kernelNumber*576 + indexes[k]],Nodes[2][kernelNumber*144 + y*12 + x]))


    #layer 2-3
    for k in range(0,16):
        for i in range(0,25):
            Links[2].append(Link(2))
    combinationInstructions = [[0,1,2],[1,2,3],[2,3,4],[3,4,5],[4,5,0],[5,0,1],[0,1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,0],[4,5,0,1],[5,0,1,2],[0,1,3,4],[1,2,4,5],[0,2,3,5],[0,1,2,3,4,5]]
    for kernelNumber in range(0,16):
        for combinationI in combinationInstructions[kernelNumber]:
            for i in range(0,64):
                indexes = indexesForKernel(12,5,i)
                for j in range (0,25):
                    Nodes[2][indexes[j] + combinationI * 144].post.append(Links[2][kernelNumber*25 + j])
                    Nodes[3][i + 64*kernelNumber].pre.append(Links[2][kernelNumber*25 + j])
                    Links[2][kernelNumber*25 + j].prePostTuples.append((Nodes[2][indexes[j] + combinationI * 144],Nodes[3][i + 64*kernelNumber]))

    #layer3-4
    for k in range(0,4):
        newLink = Link(3)
        Links[3].append(newLink)
    for i in range(0,16):
        for y in range(0,4):
            for x in range(0,4):
                indexes = [0,0,0,0]
                indexes[0] = 2*x + 16 * y
                indexes[1] = 2*x + 1 + 16*y
                indexes[2] = 2*x + 16*y + 8
                indexes[3] = 2*x + 16*y + 9
                for kernelNumber in range(0,16):
                    for k in range(0,4):
                        Nodes[3][kernelNumber*64 + indexes[k]].post.append(Links[3][k])
                        Nodes[4][kernelNumber*16 + y*4 + x].pre.append(Links[3][k])
                        Links[3][k].prePostTuples.append((Nodes[3][kernelNumber*64 + indexes[k]],Nodes[4][kernelNumber*16 + y*4 + x]))

    #layer 4-5
    for i in range(0,16*16*120):
        newLink = Link(4)
        tmpList = sortOutMultiplatedLinks(i,[120,16,16])
        postNumber = tmpList[0]
        pixelNumber = tmpList[1]
        kernelNumber = tmpList[2]
        newLink.prePostTuples.append((Nodes[4][kernelNumber * 16 + pixelNumber],Nodes[5][postNumber]))
        Nodes[4][kernelNumber * 16 + pixelNumber].post.append(newLink)
        Nodes[5][postNumber].pre.append(newLink)
        Links[4].append(Link(4))

    #layer 5-6
    for i in range(0,120):
        for j in range(0,84):
            newLink = Link(5)
            Nodes[5][i].post.append(newLink)
            Nodes[6][j].pre.append(newLink)
            newLink.prePostTuples.append((Nodes[5][i],Nodes[6][j]))
            Links[5].append(newLink)

    #layer 6-7
    for i in range(0,84):
        for j in range(0,10):
            newLink = Link(6)
            Nodes[6][i].post.append(newLink)
            Nodes[7][j].pre.append(newLink)
            newLink.prePostTuples.append((Nodes[6][i],Nodes[7][j]))
            Links[6].append(newLink)



    return (Nodes,Links)





buildLeNet5()