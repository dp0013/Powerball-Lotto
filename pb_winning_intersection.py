# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 17:19:59 2018 
Author: D. Plyler 

SUMMARY: This module imports the results of the 'pb_winningNums' and 'pb_num_prob' modules and finds their intersection.  This identifies and ranks the most frequently drawn powerball numbers ranked among the most frequently drawn winning numbers in general.  Although the first 4 of the 39 numbers are the same as the general winning number set, the rankings change after that, which is helpful to determine the most likely powerball numbers to be drawn in order of their frequency among the most frequently drawn winning numbers over the past ten years.  The results are output to a text file for reference.
"""

import pandas as pd
import datetime
from pb_winningNums import WinningNums
from pb_num_prob import pbNumRanks
import matplotlib.pyplot as plt

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
        intersect_series = pd.Series(intersect_ranked).value_counts()
        return intersect_series  

print("The ranking of intersecting winning numbers with powerball numbers is:")
print()
print(intersect.ranking())
print()
print(len(intersect.ranking()), "numbers of 69 intersect.")

now = datetime.datetime.now()

with open('intersections_ranked.txt', 'w') as f:
    f.write(str(intersect.ranking()))
    f.write(str('\n'))
    f.write(str(now))
    
      
