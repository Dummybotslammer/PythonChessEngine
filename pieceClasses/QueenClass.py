import os
import sys
import colorama
from colorama import *
init()

QueenSymbol = "Q"

class Queen:
    def __init__(self,symbol,status,color,x,y):
        self.symbol = symbol
        self.status = status
        self.color = color
        self.x = x
        self.y = y

        if (self.color == 1):
            self.symbol = self.symbol

        if (self.color == 0):
            self.symbol = Fore.RED+self.symbol

        else:
            self.symbol = self.symbol

    def QueenMain(self):
        move =input("? ")
        move = move.lower()
        var = move[0]
        if(var == "<"):
            move = move.replace("<","")
            move = int(move)
            self.x += move*(-1)
            self.y += move 
                
        if (var == ">"):
            move = move.replace(">","")
            move = int(move)
            self.x += move
            self.y += move
        
        if(var == "x"):
            move = move.replace("x","")
            move = int(move)
            self.x += move
                
        if (var == "y"):
            move = move.replace("y","")
            move = int(move)
            self.y += move
            
        return self.x,self.y

    def QueenUpdate(self):
        f= QueenMain()
        self.x = f[0]
        print(self.x)
        self.y = f[1]
        print (self.x)

    def ReturnQueenStatus(self):
        return self.status

    
        
