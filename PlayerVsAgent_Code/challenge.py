from play import *
from graphics import *


def play():               
    #play = Player('outline.txt',25)
    # play = Player('maze2.txt',10)
    # play = Player('maze3.txt',10)
    play = Player('maze4.txt',30)
    humanMoves = play.human()
    print("\nAgent's turn!")
    play.train()
    agentMoves = play.shortestPath()
        
    winner = None 
    if agentMoves == humanMoves:
        winner = "Tie!"
    elif agentMoves < humanMoves:
        winner = "Agent Won!"
        
    elif agentMoves > humanMoves:
        winner = "You Won!"


    result = Text(Point(350,350),winner)
    result.setTextColor("white")
    result.setSize(30)
    result.setStyle("bold italic")
    result.draw(play.maze.win)
    play.maze.win.getMouse()
    play.maze.win.close()
        
play()