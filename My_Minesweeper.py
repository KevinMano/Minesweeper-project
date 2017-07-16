'''
Kevin Mano
24th June 2017
My_Minesweeper
This program implements a graphical version of the classic minesweeper game
'''

from Tkinter import *
import random
import time

#Minesweeper_board class, containing the methods and attributes for the board.
class Minesweeper_board:
    MineCount = 0

    #Initial screen, hit start to populate the board.
    def __init__(self, master, mines_no):
        Minesweeper_board.MineCount = mines_no
        State_array = []
        Main_frame = Frame(master, width=576, height=768)
        Main_frame.pack()
        self.button = Button(Main_frame, text='START', width=25, command = self.populate(State_array))
        self.button.pack()

    #create the mines and populate the state array, mines are given an X, the stuff around them need to be populated now too.
    def populate(self, State_array):
        State_array = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
        Mine_count_temp = Minesweeper_board.MineCount                      
        for each in range(0,9,1):
            mine_row = random.randint(0,8)
            mine_column = random.randint(0,8)
            State_array[mine_row][mine_column] = 1
            New_mine = Mine(mine_row+1, mine_column+1)
            Mine_count_temp = Mine_count_temp - 1
        print State_array
        
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
