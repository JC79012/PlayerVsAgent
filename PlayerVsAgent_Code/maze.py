from numpy.core.numeric import outer

from graphics import *

import random
import numpy as np 
from hplayer import *


time = 5
class Maze(object):
    def __init__(self, mazeFile,space):
        # stops the window from auto updatting
        self.space = space
        self.win = GraphWin("My Maze", 700,700,autoflush=False)
        self.win.setBackground("black")
        
        self.rowSize = 0
        self.columnSize = 0
        self.outline = []
        self.makeOutline(mazeFile)
        
        self.goal = (self.rowSize-2, self.columnSize-2)
        
        self.player = hplayer(self.rowSize-1, self.columnSize-1)
        self.reset()
        self.createMaze()
        self.createRunner()
        
    def reset(self):
        self.player.visited.clear()
        self.player.actions.clear()
        self.minReward = -.3*self.columnSize*self.rowSize
        self.player.state = (0,0,'start')
        self.player.finalReward = 0

    def makeOutline(self, file) :
        rowSize = 0
        columnSize = 0
        outlineFile = open(file,'r')

        while True:
            r=outlineFile.readline()
            fileLine= []
            if r =='':
                break
            
            for i in r:
                if not(i=='\n'):
                    fileLine.append(i)
            rowSize+=1
            columnSize = len(fileLine)
            self.outline.append(fileLine)

        self.rowSize = rowSize
        self.columnSize = columnSize
        
        outlineFile.close()
        
    def createMaze(self):
        for row in range(self.rowSize):
            for column in range(self.columnSize):
                line = Rectangle(Point(column*self.space, row*self.space), Point(column*self.space+self.space, row*self.space+self.space))
                if self.outline[row][column] == "#":
                   line.setFill("green")
                   line.draw(self.win)
                else:
                    line.setFill("black")
                    line.draw(self.win)
    
    def createRunner(self):
        runnerX, runnerY,mode = self.player.state
        goalX, goalY = self.rowSize-2,self.columnSize-2
        self.player.object = Oval(Point(runnerY*self.space,runnerX*self.space),Point(runnerY*self.space+self.space, runnerX*self.space+self.space))   
        self.player.object.setFill("white")
        
        self.goal=Oval(Point(goalY*self.space, goalX*self.space), Point(goalY*self.space+self.space, goalX*self.space+self.space))
        self.goal.setFill("red")
        
        

        self.player.object.draw(self.win)
        self.goal.draw(self.win)
        update(1)
        
    def check_move(self):
        currX, currY,mode = self.player.state
        
        #left,up,right,down     
        valid_moves = [0,1,2,3]
            
        #currX is the Y axis and vise versa 
        if currX == 0:
            valid_moves.remove(1)
        elif currX == self.rowSize-1:
            valid_moves.remove(3)
        if currY == 0:
            valid_moves.remove(0)
        elif currY == self.columnSize-1:
            valid_moves.remove(2)
            
        if currX > 0 and self.outline[currX-1][currY] == '#':
            valid_moves.remove(1)
        if currX<self.rowSize-1 and self.outline[currX+1][currY] == '#':
            valid_moves.remove(3)
        if currY > 0 and self.outline[currX][currY-1] == '#':
            valid_moves.remove(0)
        if currY < self.columnSize-1 and self.outline[currX][currY+1] == '#':
            valid_moves.remove(2)
        
        return valid_moves
    
    def isOver(self):
        if self.player.finalReward < self.minReward:
            return 'Lost'
        
        currX, currY,mode = self.player.state
        if currX == self.rowSize-2 and currY==self.columnSize-2:
            return 'Winner'
        
        return 'Playing'
    
    def moveSquare(self,move):
        newX, newY,newMode = self.player.state
        if self.outline[newX][newY] != '#':
            self.player.visited.add((newX,newY))
            
        isValid = self.check_move()
        
        if not isValid:
            newMode = 'Wall!'
        elif move in isValid:
            newMode = 'running'
            if move == 0:
                newY -=1
            elif move == 1:
                newX -=1 
            elif move == 2:
                newY+=1
            elif move == 3:
                newX += 1
        else:
            newMode = 'stuck'
        # print(newMode)
        self.player.state = (newX,newY, newMode)
        # print(self.player.state)
        
    def moves(self, decision):
        self.moveSquare(decision)
        score = self.reward()
        self.player.finalReward = self.player.finalReward + score
        isOver = self.isOver()
        return score, isOver
        
    def drawPosition(self):
        playerX, playerY, playerMode = self.player.state
        self.player.object.undraw()
        self.player.object=Oval(Point(playerY*self.space, playerX*self.space),Point(playerY*self.space+self.space,playerX*self.space+self.space))
        self.player.object.setFill("white")
        
        self.player.object.draw(self.win)
        update(time)
    
    def reward(self):
        playerX, playerY, mode = self.player.state
        
        if playerX == self.rowSize-2 and playerY==self.columnSize-2:
            return 5.00
        if mode == 'Wall!':
            return -.60
        elif mode == 'running':
            return -0.1
        elif mode == 'stuck':
            return -0.25
        if (playerX,playerY) in self.player.visited:
            return -0.20
        
    def nextAction(self):
        if np.random.rand() > self.player.epsilon:
            availableActions = self.check_move()
            actions = random.choice(availableActions)
            
        else:
            runnerX, runnerY, runnerMode = self.player.state
            actions = np.argmax(self.player.qVals[runnerX, runnerY])
            
        return actions
            
       


    