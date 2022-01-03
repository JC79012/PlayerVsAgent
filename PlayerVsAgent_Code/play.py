import numpy as np
#import getpass
import msvcrt
from maze import *

class Player():
    def __init__(self, maze,space):
        self.maze = Maze(maze,space)
  
    def train(self):
        wins=0
        trainingCycles = 4500
        maxMoves = self.maze.columnSize*self.maze.rowSize
        print("\nAgent Started Learning")
        
        for cycle in range(trainingCycles):
            totalMoves = 0
            self.maze.reset()
            gameOver = False
            
            while not gameOver:
                action = self.maze.nextAction()
        
                oldX, oldY, mode = self.maze.player.state
                
                
                reward, status = self.maze.moves(action)
                
                if status == 'Winner':
                    wins+=1
                    gameOver=True
                elif status == 'Lose':
                    gameOver =True
                else:
                    gameOver = False
                
                newX, newY, newMode = self.maze.player.state 
                self.maze.player.qVal(oldX,oldY,newX, newY,action,reward)
                # self.maze.drawPosition()
                totalMoves+=1
                if totalMoves > maxMoves:
                    gameOver = True
            # print("Cycle: ", cycle,"/",trainingCycles,totalMoves, wins,status,self.maze.player.state,reward )    
        print("Learning Complete!\n")        
   
    def shortestPath(self):
        moves = 0
        print("Agent Start!")
        self.maze.reset()
        gameOver = False
        
        
        while not gameOver:
            validActions = self.maze.check_move()
            # print(validActions)
            if not validActions:
                break
            currX, currY, currMode = self.maze.player.state
            action = np.argmax(self.maze.player.qVals[currX,currY])
            
            reward, status = self.maze.moves(action)
            
            # self.maze.drawPosition()
            if status == 'Winner':
                gameOver = True
            elif status == 'Lose':
                gameOver = True
            else:
                gameOver =False
            
            self.maze.drawPosition()
            moves += 1
            
        # print("Final score:", self.maze.player.finalReward)
        return moves
    
    def human(self):
        moves = 0
        print("Human Start!")
        self.maze.reset()
        # self.maze.drawPosition()
        gameOver = False
        action = -1
        wAction = str()
       
        print("Make a move (0(LEFT), 1(UP), 2(RIGHT), 3(DOWN), 7(Quit)): ")
        # print("Make a move (a|w|s|d): ")
        while not gameOver:
            validActions = self.maze.check_move()
            
            if not validActions:
                break 
            while(action != 0  and action!= 1  and action != 2 and action != 3 and action!=7):
                try:    
                    #action = int(input())
                    action = int(msvcrt.getch())
                except ValueError:
                    print("Invalid Input: Try again...")
                    
 
            if action == 7:
                moves +=1000
                gameOver = True
                print("Quit Maze")
                break
            
            reward, status = self.maze.moves(action)
            moves+=1
            # print(self.maze.player.state)
            
            if status == 'Winner':
                gameOver = True
            elif status == 'Lose':
                gameOver = True
            else:
                gameOver = False
            
            self.maze.drawPosition()
            # moves+=1
            action = -1
            wAction = ''
        return moves
                                           

