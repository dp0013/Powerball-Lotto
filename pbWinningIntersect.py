# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:19:59 2018 
Author: D. Plyler 

SUMMARY: This module imports the results of the 'pbWinningNums' and 'pbNumRanks' modules and finds their intersection.  This identifies and ranks the most frequently drawn powerball numbers ranked among the most frequently drawn winning numbers in general.  Although the first 4 of the 39 numbers are the same as the general winning number set, the rankings change after that, which is helpful to determine the most likely powerball numbers to be drawn in order of their frequency among the most frequently drawn winning numbers over the past ten years.  The results are output to a text file for reference via a tkinter interface.
"""

from pandas import Series  #for data processing
import datetime
from pbWinningNums import WinningNums
from pbNumRanks import pbNumRanks
#import matplotlib.pyplot as plt
from tkinter import *  #for Tkinter functionality

#create global variable 'now' for datetime use:
now = datetime.datetime.now()

class intersect:           
    
    def intersection(lst1, lst2):        
        #create list to store the intersection of two other lists:
        lst3 = [value for value in lst1 if value in lst2] 
        return lst3 
    
    def ranking():        
        #create variables for the two imported lists:
        lst1 = WinningNums.winners() 
        lst2 = pbNumRanks.pb_num() 
        
        #create variable for sorting intersecting lists:
        intersect_ranked = intersect.intersection(lst1, lst2)
        
        #sort intersecting numbers by frequency via Panda Series:
        intersect_series = Series(intersect_ranked).value_counts()
        return intersect_series  

#this is being used to ensure dependent modules (e.g., tkinter) don't run everything in this module if imported unless explicitly called: 
#if __name__ == "__main__":              
#    print('-' *10, ' BEGIN ', '-'*15,'\n')
#    print("The ranking of all winning numbers intersecting with winning Powerball numbers is:", '\n')
#    print(intersect.ranking(),'\n')
#    print(len(intersect.ranking()), "numbers of 69 intersect.", '\n')
#    #write to file:
#    with open('intersections_ranked.txt', 'w') as f:
#        f.write(str(intersect.ranking()))
#        f.write('\n')
#        f.write('\n')
#        f.write("Last updated: ")
#        f.write(str(now))
#    print("Results have been written to 'intersections_ranked.txt'.", '\n')
#    print("-"*10, "PROGRAM FINISHED AT", (now.strftime("%Y-%m-%d %H:%M:%S")), '\n')
        
        
#''' Use the below code for tkinter functionality:
    
panel = Tk() #create base panel

#create title for base panel
panel.title("Most Frequent Winning Powerball Numbers, Ranked ")

panel.configure(background = "black") #change panel bg color

def button1Fx(event): #create left button functions
    print("The ranking of intersecting winning numbers with powerball numbers is:", '\n')
    print(intersect.ranking(), '\n')
    print("DONE.", '\n')
    
def button2Fx(event): #create middle button functions
    print(len(intersect.ranking()), "numbers of 69 intersect.", '\n')
    print("DONE.", '\n')
    
def button3Fx(event): #create right button functions
    with open('intersections_ranked.txt', 'w') as f:
            f.write(str(intersect.ranking()))
            f.write('\n')
            f.write('\n')
            f.write("Last updated: ")
            f.write(str(now))
    print("Results have been written to 'intersections_ranked.txt'.", '\n')
    print("DONE.", '\n')

#bind left button to all functions:
button1 = Button(panel, height = 2, text = "Print Ranking Numbers", fg = 'red')  #fg = text or foreground color
button1.bind("<Button-1>", button1Fx)
#bind middle button to all functions:
button2 = Button(panel, height = 2, text = "Number of Intersects", fg = 'orange')
button2.bind("<Button-1>", button2Fx)
#bind right button to all functions:
button3 = Button(panel, height = 2, text = "Write to File", fg = 'blue')
button3.bind("<Button-1>", button3Fx)
#position buttons with 'pack' parameters:  
button1.pack(side = LEFT) 
button2.pack(side = LEFT) 
button3.pack(side = LEFT) 
#ensure panel stays open until user closes manually:
panel.mainloop()
#'''
