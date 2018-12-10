# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 02:17:44 2018
Author: D. Plyler 

SUMMARY: This module scrapes the www.flalottery.com website for just the winning Powerball numbers from 7 Jan 2009 to 24 October 2018.  This is done because only the order of the Powerball number matters in this particular lottery.  It captures the base html, then parses out each of the winning PB numbers from their surrounding data (dates, descriptions, and other numbers), then sorts them by their frequency.  If this moduel is called explicitly, it will print out all winning PB numbers, their count, the unique numbers with their respective frequencies, and their count.  Finally, the results are saved to a text file for reference and the last console output diplays the time the program completed execution of all explicit commands.
"""
from pandas import set_option   #pandas used with Series (pd.Series) to rank all results
from pandas import Series #pandas used with Series (pd.Series) to rank all results
import datetime   #used for formatting datetime
from pbWinningNums import WinningNums
#create global datetime variable:
now = datetime.datetime.now()

#create WinningNums Class, containing the base URL:
class pbNumRanks:
    def pb_num():
        pb_num = WinningNums.pb_nums()
        return pb_num

    #create method for sorting all winning PB numbers by frequency using panda Series:
    def rankings():
        pb_ranks = pbNumRanks.pb_num()
        #print(pd.Series(winners).value_counts()
        pb_series = Series(pb_ranks).value_counts()
        return pb_series     
    
#conduct these actions ONLY when this module is run (NOT when called by other modules):
if __name__ == "__main__":
    print('-' *10, ' BEGIN ', '-'*15,'\n')
    print("This is a list of all winning PB numbers: ", '\n')
    print(pbNumRanks.pb_num(), '\n')
    print("Total PB numbers during timeframe: ", len(pbNumRanks.pb_num()),'\n')
    #ensure all captured pandas data can be displayed:
    set_option('display.max_rows', 100)
    print("This is the list of unique PB numbers by rank: ", '\n')
    print(pbNumRanks.rankings(), '\n')
    print("Total unique PB numbers captured: ", len(pbNumRanks.rankings()), '\n')
    #write results to file:        
    with open('pb_ranks.txt', 'w') as f:
        f.write(str(pbNumRanks.rankings()))
        f.write(str(now))
    print("-"*10, "PROGRAM FINISHED AT", (now.strftime("%Y-%m-%d %H:%M:%S")))
    

###             Debugging              ###      
  
#print("These are the powerball numbers: ", pbNumRanks.pb_num())
#print()

###             Debugging              ###   
    
    
