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
        Main_frame = Frame(master, width=405, height=300)
        Main_frame.pack()
        self.start_button = Button(Main_frame, text='START', width=25, command = lambda: self.draw(Main_window,State_array))
        self.start_button.pack()

    #In the first button press in minesweeper, there are no mines yet, so populate only happens after the first click on the board.
    #This function simply sets up the whole board, starts the timer. After the first press, the populate function occurs.
    #After that, this function continues with the populate. 
    def draw(self,master,State_array):
        self.start_button.forget()
        if Minesweeper_board.MoveCount < 1:
            State_array = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
            self.button = [[0 for columns in range(9)] for rows in range(9)]
            for rows in range(1,10):
                for columns in range(1,10):
                    self.button[rows-1][columns-1] = Button(Main_window, width=5, command=lambda i=rows-1, j=columns-1: self.populate(Main_window,State_array,i,j) )
                    self.button[rows-1][columns-1].grid(row=rows-1, column=columns-1)
            Minesweeper_board.MoveCount += 1
            print Minesweeper_board.MoveCount
        else:
            print "We made it here instead, still really good!"
            #self.uncover(State_array, )
            Minesweeper_board.MoveCount += 1
            print Minesweeper_board.MoveCount
    
    '''create the mines and populate the state array, mines are given an X, the cells around the mines need to be populated now too.
    Remember, the first cell that is clicked cannot have a mine.
    We shall make the State_array contain which cells contain mines, and which ones have the mine.
    So mines shall be given the integer vaariable 99 in State_array. 
    '''        
    def populate(self, master, State_array,row,column):
        cell_status = IntVar()
        cell_status.set(0)
        self.button[row][column].config(relief = SUNKEN, state = DISABLED, textvariable = cell_status)
        Mine_count_temp = Minesweeper_board.MineCount
        iter_count = 1
        while (iter_count < 10):
            mine_row = random.randint(0,8)
            mine_column = random.randint(0,8)
            if(mine_row != row | mine_column != column):
                State_array[mine_row][mine_column] = 99      
                New_mine = Mine(mine_row+1, mine_column+1)
                neighbouring_cells = [[row-1,column-1],[row-1,column],[row-1,column+1],[row, column-1],[row,column+1],[row+1,column-1],[row+1,column],[row+1,column+1]]
                for iter2 in range(0,8):
                    State_array[x_coord][y_coord] += 1
                Mine_count_temp = Mine_count_temp - 1
                iter_count += 1
        print State_array
        #Now we have to visit all the neighbours of the cell containing mines, and update them. Just visit all the neighbours, and add 1 to their State_array values.
        #We create an array, populate it with the neighbours, and run a for loop and increment them by 1.

    #Uncover the button, and do the check based on the logic above.
    def uncover(self, State_array, row, column):
        self.button[row][column].config(relief = SUNKEN, state = DISABLED, textvariable = cell_status)
        if(State_array[row][column] == 99):
            print "KABOOM!"
        
#Mine class
class Mine:
    def __init__(self, coords_row, coords_column):
        print "Mine created, at tile %i,%i" %(coords_row, coords_column) 

Main_window = Tk()
Main_window.title("Minesweeper")
Main_window.geometry("405x300")
Main_window.configure(background = 'grey')
New_Game = Minesweeper_board(Main_window, 10)        
Main_window.mainloop()    
