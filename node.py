import math

class Node:
    def __init__(self, successor, cost):
        self.ubication = successor
        self.g = cost
        self.h = 0
        self.f = 0
    

    def calculateHeuristicFunction(self, goalState):
        self.h = math.sqrt((self.ubication[0] - goalState[0])**2 + (self.ubication[1] - goalState[1])**2)

    def calculateF(self):
        self.f = self.g + self.h
  
    def getF(self):
        return self.f
