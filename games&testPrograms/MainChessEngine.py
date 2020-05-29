import sys
import os
import colorama
from colorama import *
import RookClass
from RookClass import *
import PawnClass
from PawnClass import *
import QueenClass
from QueenClass import *
import KingClass
from KingClass import *
import BishopClass
from BishopClass import *
#import KnightClass
import importlib
init()

pieces = ["P","R","N","B","K","Q"]
blackPieces = [0]
whitePieces = [0]
GameLoop = True
turn = 1 #white is 1 black is 0
menuInput = ""


board = [["_","_","_","_","_","_","_","_"],#1
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"],
       ["_","_","_","_","_","_","_","_"]]#8
        #1                          #8

def Render (x):#is limited to render 8x8
    m =["","","","","","","",""]
    for f in range(0,8):#These values are fixed based on array indexes
        for i in range(0,8):
                m[f] += x[f][i]
        print (m[f])

def ClearScrn():
    os.system("cls")

while (GameLoop == True):
    print("Welcome to Text Chess")
    print("1.Regular Chess(No timer)\n2.Exit Game")
    menuInput = input("? ")
    if (menuInput == "1"):
        print("White to play.")
        #Do this.
    if (menuInput == "2"):
        break;


