import os
import sys
import colorama
from colorama import *
init()

BishopSymbol = "B"

class Bishop:
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

    def BishopMain(self):
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
            
        return self.x,self.y

    def BishopUpdate(self):
        f = BishopMain()
        self.x = f[0]
        print (self.x)
        self.y = f[1]
        print(self.y)

    def ReturnBishopStatus(self):
        return self.status

#b1 = Bishop(BishopSymbol,True,1,0,0)
#b1.BishopMain()
#print(b1.ReturnBishopStatus())

        
