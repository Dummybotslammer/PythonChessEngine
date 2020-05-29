import os
import sys
import colorama
from colorama import *
init()

KnightSymbol = "N"

class Knight:
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

    #def KnightMain(self):
        
