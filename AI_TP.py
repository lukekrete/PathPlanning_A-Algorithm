import string
import math
import sys
import os
from queue import PriorityQueue

def main():
    filename = 'input.txt'
    rL,rW,numRobots,robotArray,rend,room = getInput(filename)
    #printRoom(room,rL,rW)
    #print(type(robotArray[0]))
    for robot in robotArray:
        path = Astar(room,robot,rend,rL,rW)

def Astar(room,start, goal, rL, rW):
    frontier = PriorityQueue()
    frontier.put(start,0)
    previous = {}
    current_cost = {}
    previous[start] = None
    current_cost[start] = 0

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        neighbors = getNeighbors(current,rL,rW)
        for element in neighbors:
            new_cost = current_cost[current] + cost(current,element)
            if element not in current_cost or new_cost < current_cost[element]:
                current_cost[element] = new_cost
                priority = new_cost + cost(goal,element)
                frontier.put(element, priority)
                previous[element] = current
                

def cost(current, nextNode):
    cost1 = (current[0]**2 - nextNode[0]**2)
    cost2 = (current[1]**2 - nextNode[0]**2)
    final_cost = (cost1 + cost2)**0.5
    return final_cost

    
def getNeighbors(current):
    neighbors = []
    if current[0] > 0 and current[1] > 0 and current[1] < rL and current[0] < rW:
        
        
    
def printRoom(room,rL,rW):
    for i in range(rL):
        print()
        for j in range(rW):
            print(room[i][j],end='')

            
def getInput(filename):
    with open(filename) as fp:
        line = fp.readline()
        words = line.split()
        rL = int(words[0])
        rW = int(words[1])
        room = [[0]*rW]*rL

        line=fp.readline()
        words = line.split()
        numRobots = int(words[0])

        robotArray = []
        for i in range(numRobots):
            line = fp.readline()
            words = line.split()
            robotArray.append((int(words[0]),int(words[1])))

        line = fp.readline()
        words = line.split()
        rend = ((int(words[0]),int(words[1])))
        #rendX = words[0]
        #rendY = words[1]
        for i in range(rL):
            line=fp.readline()
            row = line.split()
            room[i] = row
          
    return rL,rW,numRobots,robotArray,rend,room
