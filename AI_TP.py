import string
import math
import sys
import os

def main():
    filename = 'input.txt'
    rL,rW,numRobots,robotOneX,robotOneY,robotTwoX,robotTwoY,rendX,rendY,room = getInput(filename)
    #printRoom(room,rL,rW)

def printRoom(room,rL,rW):
    for i in range(rL):
        print()
        for j in range(rW):
            print(room[i][j],end='')

            
def getInput(filename):
    with open(filename) as fp:
        count = 1
        count2 = 0
        for line in fp:
            #print(count)
            if count == 1:
                words = line.split()
                rL = int(words[0])
                rW = int(words[1])
                room = [[0]*rW]*rL
            elif count == 2:
                words = line.split()
                numRobots = int(words[0])
            elif count == 3:
                words = line.split()
                robotOneX = int(words[0])
                robotOneY = int(words[1])
            elif count == 4:
                words = line.split()
                robotTwoX = int(words[0])
                robotTwoY = int(words[1])
            elif count == 5:
                words = line.split()
                rendX = int(words[0])
                rendY = int(words[1])
            else:
                row = line.split()
                room[count2] = row
                count2+=1
            count += 1
    return rL,rW,numRobots,robotOneX,robotOneY,robotTwoX,robotTwoY,rendX,rendY,room
