import sys
import os
import colorama
from colorama import *
init()

RookSymbol="R"

class Rook:
    def __init__ (self,symbol,status,color,x,y): #Status refers to dead or alive and is a bool. Color is 1 for white and 0 for black.
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

    def RookMain(self):
        #print("----Rook Test----")
        #Render(map)
        move =input("? ")
        move = move.lower()
        var = move[0]
        if(var == "x"):
            move = move.replace("x","")
            move = int(move)
            #if ((x +move) < 0 or (x+move) > 7): (WIP)
            #map[self.y][self.x] = "_"
            self.x += move
            #map[self.y][self.x] = player
                
        if (var == "y"):
            move = move.replace("y","")
            move = int(move)
            #if (y +move < 0 or y+move > 7): (WIP)
            #map[self.y][self.x] = "_"
            self.y += move
            #map[self.y][self.x]=player

        #os.system("cls")
        return self.x,self.y

    def RookUpdate(self):
        f = RookMain()
        self.x = f[0]
        print (self.x)
        self.y = f[1]
        print(self.y)

    def ReturnRookStatus(self) : #this returns the status of the piece and gives the user more flexability on how to treat the piece
        return self.status

#r1 = Rook(RookSymbol,True,1,0,0)
#r1.RookMain()
#print(r1.ReturnRookStatus())


