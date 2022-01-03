from numpy.random.mtrand import poisson
from graphics import *

space = 30

class Demo():
    def __init__(self, file):
        self.row = 0 
        self.column = 0 
        self.mazeOutline = [] 
        
        self.window = GraphWin("My demo", 700,700)
        self.window.setBackground("black")
        
        self.makeOutline(file)
        self.createMaze()
        self.createRunner()
        
        self.window.getMouse()
        self.window.close()
        
    def makeOutline(self, file):
        rows, columns = 0,0

        outlineFile = open(file,'r')

        while True:
            r=outlineFile.readline()
            fileLine= []
            if r =='':
                break
            
            for i in r:
                if not(i=='\n'):
                    fileLine.append(i)

            rows+=1
            columns = len(fileLine)
            self.mazeOutline.append(fileLine)
        
        self.row = rows
        self.column = columns    
        outlineFile.close()
        
    def createMaze(self):
        for row in range(self.row):
            for column in range(self.column):
                rectangle = Rectangle(Point(column*space, row*space), Point(column*space+space, row*space+space))
                if self.mazeOutline[row][column] == "#":
                    rectangle.setFill("green")
                    rectangle.draw(self.window)  
                elif self.mazeOutline[row][column] == " ":
                    rectangle.setFill("black")
                    rectangle.draw(self.window)
                    
    def createRunner(self):
        runner = Oval(Point(0*space, 0*space), Point(0*space+space, 0*space+space))
        runner.setFill("white")
        
        goal = Oval(Point((self.column-2)*space, (self.row-2)*space),Point((self.column-2)*space+space, (self.row-2)*space+space))
        goal.setFill("orange")
        
        runner.draw(self.window)
        goal.draw(self.window)
        

trial = Demo('maze4.txt')






# oval = Oval(Point(250,250), Point(450,450))

# oval.setFill("white")

# oval.draw(window)



    # rectangle = Rectangle(Point(250,250),Point(550,450))
    
    # rectangle.setFill("green")
    
    # rectangle.draw(window)
    
    
    
    # text = Text(Point(350,350), "Hello World!")
    
    # text.setTextColor("Blue")
    
    # text.setSize(35)

    # text.setStyle("bold italic")
    
    # text.draw(window)
    
    
# def makeOutline(file, mazeOutline):
#         rows, columns = 0,0

#     outlineFile = open(file,'r')

#     while True:
#         r=outlineFile.readline()
#         fileLine= []
#         if r =='':
#             break
        
#         for i in r:
#             if not(i=='\n'):
#                 fileLine.append(i)

#         rows+=1
#         columns = len(fileLine)
#         mazeOutline.append(fileLine)
        
        
#     outlineFile.close()
    
#     return rows, columns, mazeOutline

    
    
# def createMaze(mazeOutline, rows, columns, window):
#     for row in range(rows):
#         for column in range(columns):
#             rectangle = Rectangle(Point(column*space, row*space), Point(column*space+space, row*space+space))
#             if mazeOutline[row][column] == "#":
#                 rectangle.setFill("green")
#                 rectangle.draw(window)  
#             elif mazeOutline[row][column] == " ":
#                 rectangle.setFill("black")
#                 rectangle.draw(window)

# def createRunner(window, row, column):
#     runner = Oval(Point(0*space, 0*space), Point(0*space+space, 0*space+space))
#     runner.setFill("white")
    
#     goal = Oval(Point((column-2)*space, (row-2)*space),Point((column-2)*space+space, (row-2)*space+space))
#     goal.setFill("orange")
    
#     runner.draw(window)
#     goal.draw(window)
    
    
# def main():
#     window =  GraphWin("Any name here", 700,700,autoflush=False)
#     mazeOutline = []
    
#     rows, columns, mazeOutline = makeOutline("outline.txt", mazeOutline)
    
    
#     createMaze(mazeOutline, rows, columns, window)
#     createRunner(window, rows, columns)
#     # print(mazeOutline)
    

    
#     window.getMouse()
#     window.close()

# main()