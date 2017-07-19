'''
Kevin Mano
24th June 2017
My_Minesweeper
This program implements a graphical version of the classic minesweeper game
'''

from Tkinter import *
import random
import time

'''
State_array encodes the states of the board for the presence of mines. 
There are 2 states for State_array: Mine or No Mine.

Besides that, we also have the button array, which encodes the buttons in a grid.
This array has three states: flagged, open or closed.

To capture the logic of each cell, consider below:
IF(OPENED && CONTAINS_MINE) --> BOOOOOOMMMMMM!!!! 
IF(OPENED && !(CONTAINS_MINE)) --> Evaluate neighbours, and place the number
of mines contained in neighbours in the cell.

IF(CLOSED && CONTAINS_MINE) --> NOTHING
IF(CLOSED && !(CONTAINS_MINE)) --> NOTHING

IF(FLAGGED && CONTAINS_MINE) -->
IF(FLAGGED && !(CONTAINS_MINE)) -->

So we need to encode this using both the arrays.
Basically, this means to reference both arrays, and return the appropriate result.
'''


#Minesweeper_board class, containing the methods and attributes for the board.
class Minesweeper_board:
    MineCount = 0
    MoveCount = 0 

    #Initial screen, hit start to populate the board.
    def __init__(self, master, mines_no):
        Minesweeper_board.MineCount = mines_no
        State_array = []
        Main_frame = Frame(master, width=576, height=768)
        Main_frame.pack()
        self.start_button = Button(Main_frame, text='START', width=25, command = lambda: self.draw(Main_window,State_array))
        self.start_button.pack()

    #In the first button press in minesweeper, there are no mines yet, so populate only happens after the first click on the board.
    #This function simply sets up the whole board, starts the timer. After the first press, the populate function occurs.
    #After that, this function continues with the populate. 
    def draw(self,master,State_array):
        self.start_button.destroy()
        if self.MoveCount < 1:
            State_array = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
            self.button = [[0 for columns in range(8)] for rows in range(8)]
            for rows in range(0,8):
                for columns in range(0,8):
                    self.button[rows][columns] = Button(Main_window, text="", width=5, command=lambda i=rows, j=columns: self.populate(Main_window,State_array,i,j))
                    self.button[rows][columns].grid(row=rows, column=columns)
            self.MoveCount += 1
            print self.MoveCount
        else:
            print "We made it here instead, still really good!"
            self.MoveCount += 1
            print self.MoveCount
    
    #create the mines and populate the state array, mines are given an X, the cells around the mines need to be populated now too.
    #Remember, the first cell that is clicked cannot have a mine.
    def populate(self, master, State_array,row,column):
        self.button[row][column].config(relief = SUNKEN)
        Mine_count_temp = Minesweeper_board.MineCount                      
        for each in range(0,9,1):
            mine_row = random.randint(0,8)
            mine_column = random.randint(0,8)
            State_array[mine_row][mine_column] = 1
            New_mine = Mine(mine_row+1, mine_column+1)
            Mine_count_temp = Mine_count_temp - 1
        print State_array
        self.button[row][column].set()

    #Uncover the button, and do the check based on the logic above.
    def Uncover(self, State_array, row, column):
        print "We made it here!"

        
#Mine class
class Mine:
    def __init__(self, coords_row, coords_column):
        print "Mine created, at tile %i,%i" %(coords_row, coords_column) 

Main_window = Tk()
Main_window.title("Minesweeper")
Main_window.geometry("600x700")
Main_window.configure(background = 'grey')
New_Game = Minesweeper_board(Main_window, 10)        
Main_window.mainloop()    
