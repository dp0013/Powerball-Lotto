# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 02:17:44 2018
Author: D. Plyler 

SUMMARY: This module scrapes the www.flalottery.com website for just the winning Powerball numbers from 7 Jan 2009 to 24 October 2018.  This is done because only the order of the Powerball number matters in this particular lottery.  It captures the base html, then parses out each of the winning PB numbers from their surrounding data (dates, descriptions, and other numbers), then sorts them by their frequency.  If this moduel is called explicitly, it will print out all winning PB numbers, their count, the unique numbers with their respective frequencies, and their count.  Finally, the results are saved to a text file for reference and the last console output diplays the time the program completed execution of all explicit commands.
"""

import requests   #using 'requests' for handling HTTP
from bs4 import BeautifulSoup   #bs4 for parsing the html
import pandas as pd   #pandas used with Series (pd.Series) to rank all results
import datetime   #used for formatting datetime

#create global datetime variable:
now = datetime.datetime.now()

#create WinningNums Class, containing the base URL:
class pbNumRanks:
    BASE_URL = 'http://www.flalottery.com/site/winningNumberSearch?searchTypeIn=range&gameNameIn=POWERBALL&singleDateIn=&fromDateIn=01%2F07%2F2009&toDateIn=10%2F24%2F2018&n1In=&n2In=&n3In=&n4In=&n5In=&n6In=&pbIn=&mbIn=&lbIn=&pnIn=&cbIn=&submitForm=Submit'   
    #create Method for getting the html from the provided url:
    def get_html(url):
        """
        Get the FL Lottery html
        :return:
        """
        fl_lottery = requests.get(url)
        html = BeautifulSoup(fl_lottery.text, 'html.parser')
        return html

  #create Method for parsing the PB number from the provided url:
    def pb_num():
        html = pbNumRanks.get_html(pbNumRanks.BASE_URL)
        pb_num = []        
        if html:
            for tbody in html.find_all('tbody'):
                div = tbody.text.split('-')
                for x in div:
                    if 'PB' in x:
                        x= x[7:9]
                        x = x.split()
                        x = ''.join(x)
                        pb_num.append(x)
                        pb_num = [s.lstrip("0") for s in pb_num]                
                return pb_num

    #create Method for combining all the numbers into one list, then sort them by frequency of occurrence using panda Series:
    def rankings():
        pb_ranks = pbNumRanks.pb_num()
        #print(pd.Series(winners).value_counts()
        pb_series = pd.Series(pb_ranks).value_counts()
        return pb_series     
    
#conduct these actions ONLY when this module is run (NOT when called by other modules):
if __name__ == "__main__":        
    print("This is a list of all winning PB numbers: ")
    print()
    print(pbNumRanks.pb_num())
    print()
    print("Total PB numbers during timeframe: ", len(pbNumRanks.pb_num()))
    print()
    #ensure all captured pandas data can be displayed:
    pd.set_option('display.max_rows', 100)
    print("This is the list of unique PB numbers by rank: ")
    print()
    print(pbNumRanks.rankings())
    print()
    print("Total unique PB numbers captured: ", len(pbNumRanks.rankings()))
    #write results to file:        
    with open('pb_ranks.txt', 'w') as f:
        f.write(str(pbNumRanks.rankings()))
        f.write(str(now))
    print()
    print("Program finished at", (now.strftime("%Y-%m-%d %H:%M:%S")))
    

###             Debugging              ###      
  
#print("These are the powerball numbers: ", pbNumRanks.pb_num())
#print()

###             Debugging              ###   
    
    
