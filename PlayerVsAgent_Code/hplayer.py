import numpy as np

class hplayer():
    def __init__(self, row, column):
        self.state = None
        self.finalReward = 0
        self.visited=set()
        self.actions=[]
        self.epsilon = 0.7
        self.learningRate= 0.7
        self.discount = 0.9
        self.qVals=np.zeros((row+1, column+1,4))
        
    def qVal(self, oldX, oldY, newX, newY,action, reward):
        oldVal = self.qVals[oldX, oldY, action]
        temp = reward +(self.discount*np.max(self.qVals[newX,newY])) - oldVal
        newQVal = oldVal + (self.learningRate * temp)
        self.qVals[oldX,oldY, action] = newQVal
            
    
          
            
            
    
    
        
        
            
        
        
        
        