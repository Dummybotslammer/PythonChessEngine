import os
import sys
import colorama
from colorama import *
init() #initializes colorama

PawnSymbol = "P"

class Pawn:
    def __init__ (self,symbol,status,color,x,y,FirstTurn,orientation):#FirstTurn is a bool and oreintation is 1 for white and -1 for black
        self.symbol = symbol
        self.status = status
        self.color = color
        self.x = x
        self.y = y
        self.FirstTurn = FirstTurn
        self.orientation = orientation
        if (self.color == 1):
            self.symbol = self.symbol

        if (self.color == 0):
            self.symbol = Fore.RED+self.symbol

        else:
            self.symbol = self.symbol


    def PawnMain(self):
        if(self.FirstTurn == True):
            move = input("? ")
            move = int(move)
            if (move >= 2):
                move = 2*self.orientation

            if(move <= 1):
                move = 1*self.orientation

            self.FirstTurn = False

        if (self.FirstTurn == False):
            move = 1*self.orientation

        self.y += move

        return self.y

    def ReturnPawnStatus():
        return self.status

         
