import os
import sys
import colorama
from colorama import *
init()

KingSymbol = "K"

class King:
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

    def KingMain(self):
        move = input("? ")
        move =move.lower()
        if (move == "w"):
            self.y += 1
            
        if (move == "s"):
            self.y -= 1
            
        if (move == "a"):
            self.x -= 1
            
        if (move == "d"):
            self.x +=1
            
        if (move == "aw"):#all of this is just based of wasd displacement or something like that.
            self.x -= 1
            self.y +=1
            
        if (move == "sd"):
            self.x +=1
            self.y -= 1
            
        if (move == "dw"):
            self.x += 1
            self.y += 1
            
        if (move == "sa"):
            self.x -= 1
            self.y -= 1

        if(self.x < 0):
            self.x = 0

        if(self.x > 7):
            self.x = 7

        if(self.y < 0):
            self.y = 0

        if(self.y > 7):
            self.y = 7

        return self.x,self.y

    def KingUpdate(self):
        f = KingMain()
        self.x = f[0]
        print (self.x)
        self.y = f[1]
        print(self.y)

    def ReturnKingStatus(self):
        return self.status

    #def FalseKing(self):
        #self.status = False
        
#q1 = King(KingSymbol,True,1,0,0)
#q1.FalseKing()
#f =q1.ReturnKingStatus()
#print(f)
        
            
            
