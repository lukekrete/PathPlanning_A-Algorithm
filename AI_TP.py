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
        print("path for robot({}):{}".format(robot, path))
    
    addPoints(room, robotArray, rend)
    printRoom(room, rL, rW)
    print("finished.")

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
            print("current is goal:",current)
            break
        neighbors = getNeighbors(current,rL-1,rW-1, room)
        for element in neighbors:
            new_cost = current_cost[current] + cost(current,element)
            # print(new_cost)
            if element not in current_cost or new_cost< current_cost[element]:
                current_cost[element] = new_cost
                priority = new_cost + cost(goal,element)
                frontier.put(element, priority)
                previous[element] = current
    room = updateRoom(previous, room)
    stepsTaken = []
    # print(previous)
    # print("previous goal:", previous[goal])
    for key in previous.keys():
        # print(key,previous[key])
        stepsTaken.append(key)
    return stepsTaken

def updateRoom(previous, room):
    for key in previous.keys():
        if(previous[key] is not None):
            if(len(previous[key]) == 2):
                node = previous[key]
                room[node[1]][node[0]] = 'X'
                print(room)
    return room

def addPoints(room, robotArray,rend):
    x = 'A'
    i = 0
    for robot in robotArray:
        room[robot[1]][robot[0]] = "{}".format(chr(ord(x)+i))
        i+=1
    room[rend[1]][rend[0]] = "R"


def cost(current, nextNode):
    # print("CURRENT:",current,"nextNode:", nextNode)
    cost1 = abs(current[0]**2 - nextNode[0]**2)
    cost2 = abs(current[1]**2 - nextNode[0]**2)
    final_cost = (cost1 + cost2)**0.5
    return float(final_cost)

    
def getNeighbors(current, rL, rW, room):
    #returns an array of tuples of (ROW x COL)
    neighbors = []
    if current[0] > 0:
        #can move left, check if space is occupiable
        if(room[current[1]][current[0]-1]) != 1:
            neighbors.append((current[0]-1,current[1]))
    if current[1] > 0:
        #can move up, check if space is occupiable
        
        if(room[current[1]-1][current[0]]) != 1:
            neighbors.append((current[0],current[1]-1))
    if current[1] < rL:
        #can move down, check if space is occupiable
        if(room[current[1]+1][current[0]]) != 1:
            neighbors.append((current[0],current[1]+1))
    if current[0] < rW:
        #can move right, check if space is occupiable
        if(room[current[1]][current[0]+1]) != 1:
            neighbors.append((current[0]+1,current[1]))

    return neighbors
    
def printRoom(room,rL,rW):
    for i in range(rL):
        print()
        for j in range(rW):
            print(room[i][j],end='')
    print()

            
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


if __name__ == '__main__':
    main()