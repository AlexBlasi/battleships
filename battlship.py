from tkinter import *
import random
import math

#this version lets users set small ships locations
 
global p2Board
p2Board = [["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"]]

global p1Board
p1Board = [["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"],["*","*","*","*","*"]]

print("Please select the location of your first ship")

global p1ShipOne
p1ShipOne = "false"

global p2ShipOne
p2ShipOne = "false"

global shipPlaced
shipPlaced = ["false"   , "false"   , "false"   ,"false"]
#            [p1shipone , p2shipone , p1shiptwo , p2ship two ]

def buttonClicked(coords, windowTitle):
    global p1Board
    global p2Board
    
    #print(coords, windowTitle)

    # coords[0] is x axis and coords[1] is y axis

    
    #print (int(coords[0]))
    #print (int(coords[1]))



    placeShips(coords, windowTitle)

def placeShips(coords, windowTitle):
    
    global p1Board
    global p2Board
    global shipPlaced
    
    #p1ship small is shipPlaced[0]    p2ship small is shipPlaced[1]
    #p1ship medium is shipPlaced[2]  p2ship medium is shipPlaced[3]
    
    if (shipPlaced[0] == "true") and (shipPlaced[1] == "true"):
     
        print("Both small Ships have been set. Please select the location of your medium ships")

        if (shipPlaced[2] == "true") and (shipPlaced[3] == "true"):
            print("Both medium Ships have been set. Please select the location of your large ships")


        elif (windowTitle == "one") and (shipPlaced[2] == "true"):
            print("P2, please click")
        
        elif (windowTitle == "two") and (shipPlaced[3] == "true"):
            print("P1, please click")

        else:
            if (windowTitle == "one"):
                p1Board[int(coords[0])] [int(coords[1])] = "M"
                print(p1Board[0], "\n", p1Board[1], "\n", p1Board[2], "\n", p1Board[3], "\n", p1Board[4], "\n")
                shipPlaced[2] = "true"
            
            if (windowTitle == "two"):
                p2Board[int(coords[0])] [int(coords[1])] = "M"
                print(p2Board[0], "\n", p2Board[1], "\n", p2Board[2], "\n", p2Board[3], "\n", p2Board[4], "\n")
                shipPlaced[3] = "true"            

        
        
    elif (windowTitle == "one") and (shipPlaced[0] == "true"):
        print("P2, please click")
        
    elif (windowTitle == "two") and (shipPlaced[1] == "true"):
        print("P1, please click")
        
    else:
        if (windowTitle == "one"):
                p1Board[int(coords[0])] [int(coords[1])] = "S"
                print(p1Board[0], "\n", p1Board[1], "\n", p1Board[2], "\n", p1Board[3], "\n", p1Board[4], "\n")
                shipPlaced[0] = "true"
            
        if (windowTitle == "two"):
                p2Board[int(coords[0])] [int(coords[1])] = "S"
                print(p2Board[0], "\n", p2Board[1], "\n", p2Board[2], "\n", p2Board[3], "\n", p2Board[4], "\n")
                shipPlaced[1] = "true"

        

        
    


def windowOpener(window, windowTitle):
    canvas = Canvas(window)
    window.wm_geometry("794x370")
    window.title('BattleShips Player: ' + windowTitle)
            
    btn = Button(window, text="A1", command=lambda: buttonClicked("00", windowTitle))
    btn.grid(row=1, column=0)

    btn = Button(window, text="A2", command=lambda: buttonClicked("01", windowTitle))
    btn.grid(row=1, column=1)

    btn = Button(window, text="A3", command=lambda: buttonClicked("02", windowTitle))
    btn.grid(row=1, column=2)

    btn = Button(window, text="A4", command=lambda: buttonClicked("03", windowTitle))
    btn.grid(row=1, column=3)

    btn = Button(window, text="A5", command=lambda: buttonClicked("04", windowTitle))
    btn.grid(row=1, column=4)


    btn = Button(window, text="B1", command=lambda: buttonClicked("10", windowTitle))
    btn.grid(row=2, column=0)

    btn = Button(window, text="B2", command=lambda: buttonClicked("11", windowTitle))
    btn.grid(row=2, column=1)

    btn = Button(window, text="B3", command=lambda: buttonClicked("12", windowTitle))
    btn.grid(row=2, column=2)

    btn = Button(window, text="B4", command=lambda: buttonClicked("13", windowTitle))
    btn.grid(row=2, column=3)

    btn = Button(window, text="B5", command=lambda: buttonClicked("14", windowTitle))
    btn.grid(row=2, column=4)


    btn = Button(window, text="C1", command=lambda: buttonClicked("20", windowTitle))
    btn.grid(row=3, column=0)

    btn = Button(window, text="C2", command=lambda: buttonClicked("21", windowTitle))
    btn.grid(row=3, column=1)

    btn = Button(window, text="C3", command=lambda: buttonClicked("22", windowTitle))
    btn.grid(row=3, column=2)

    btn = Button(window, text="C4", command=lambda: buttonClicked("23", windowTitle))
    btn.grid(row=3, column=3)

    btn = Button(window, text="C5", command=lambda: buttonClicked("24", windowTitle))
    btn.grid(row=3, column=4)


    btn = Button(window, text="D1", command=lambda: buttonClicked("30", windowTitle))
    btn.grid(row=4, column=0)

    btn = Button(window, text="D2", command=lambda: buttonClicked("31", windowTitle))
    btn.grid(row=4, column=1)

    btn = Button(window, text="D3", command=lambda: buttonClicked("32", windowTitle))
    btn.grid(row=4, column=2)


    btn = Button(window, text="D4", command=lambda: buttonClicked("33", windowTitle))
    btn.grid(row=4, column=3)

    btn = Button(window, text="D5", command=lambda: buttonClicked("34", windowTitle))
    btn.grid(row=4, column=4)


    btn = Button(window, text="E1", command=lambda: buttonClicked("40", windowTitle))
    btn.grid(row=5, column=0)

    btn = Button(window, text="E2", command=lambda: buttonClicked("41", windowTitle))
    btn.grid(row=5, column=1)

    btn = Button(window, text="E3", command=lambda: buttonClicked("42", windowTitle))
    btn.grid(row=5, column=2)

    btn = Button(window, text="E4", command=lambda: buttonClicked("43", windowTitle))
    btn.grid(row=5, column=3)

    btn = Button(window, text="E5", command=lambda: buttonClicked("44", windowTitle))
    btn.grid(row=5, column=4)


    

playerOneWindow = Tk()
playerTwoWindow = Tk()

windowOpener(playerOneWindow, "one")
windowOpener(playerTwoWindow, "two")
