__author__ = 'liukaige'
from tools import *
class Node:
    def __init__(self,layerNumber):
        self.pre = []#type list of links
        self.post = []#type list of links
        self.layerNumber = layerNumber
        self.delta = 0.0
        self.value = 0.0            self.value = 0.0;

    def forPropSigmoid(self):
        if self.layerNumber != 0:
            for eachPre in self.pre:
                self.value += eachPre.value * eachPre.pre.value
            self.value = sigmoid(self.value)

    def forPropLinear(self):
        if self.layerNumber != 0:
            self.value = 0.0;
            for eachPre in self.pre:
                self.value += eachPre.value * eachPre.pre.value



class Link:
    def __init__(self,layerNumber):
        self.prePostTuples = []#type list of nodes
        self.layerNumber = layerNumber
        self.value = 0.0
    def backProp(self):
        pass