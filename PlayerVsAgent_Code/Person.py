from maze import *

class Person():
    def __init__(self, file):
        self.maze = Maze(file)
        self.finalReward = 0
        self.state= None
        self.moves = 0
        # self.reset()
    
    def reset(self):
        self.state= (0,0,'start')
        self.finalReward = 0
        self.moves = 0 
        
        
    def play(self):
        pass
        
    