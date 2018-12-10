# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:42:49 2018 
Author: D. Plyler

SUMMARY: This project was conducted to strengthen my current Python skillset while building web scraping familiarity and is not designed to predict any winning lottery combinations.  Rather, it is designed to collect and observe data, looking for any trends out of mere curiosity.  This specific module calls on 'pbWinningNums' to determine the winning powerball lottery numbers from 2009 to 2018 in order of their frequency.  It then prints out the results, the total number of unique winning numbers captured (this should always be 69 as there are only 69 numbers used in the Powerball lottery) and the date/time the program was executed.   
"""
#imports and executes the module containing the class and supporting functions:
from pbWinningNums import WinningNums
import pandas as pd
import datetime

#ensure these actions only run explicitly, NOT when called by other modules:
def main():   
    pd.set_option('display.max_rows', 100)
    print('-' *10, ' BEGIN ', '-'*15,'\n')
    print("This is the list of winning numbers by rank: ", '\n')
    print(WinningNums.winners_sort(), '\n')
    print("Total numbers captured (this should always equal 69!): ", len(WinningNums.winners_sort()),'\n')
    now = datetime.datetime.now()
    print("-"*10, "EXECUTION COMPLETED AT", (now.strftime("%Y-%m-%d %H:%M:%S")))
        
main()
