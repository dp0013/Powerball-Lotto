# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 02:17:44 2018
Author: D. Plyler 

SUMMARY: This module scrapes the www.flalottery.com website for just the winning Powerball numbers from 7 Jan 2009 to 24 October 2018.  This is done because only the order of the Powerball number counts in this particular lottery.  It captures the base html, then parses out each of the winning PB numbers from their surrounding data (dates, descriptions, and other numbers), then sorts them by their frequency.  Finally, the results are saved to a text file for reference.
"""

import requests   #using 'requests' for handling HTTP
from bs4 import BeautifulSoup   #bs4 for parsing the html
import pandas as pd   #pandas used with Series (pd.Series) to rank all results
import csv   #used to export results to an easily readable csv file 
import datetime   #used for formatting datetime

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
        html = BeautifulSoup(fl_lottery.text, 'lxml')
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
    
#print(WinningNums.pb_num())
pd.set_option('display.max_rows', 100)
#print("This is the list of pb numbers by rank:\n",  (pbNumRanks.rankings()))
#print()
#print("Total unique numbers captured: ", len(pbNumRanks.rankings()))
#print()
#print("Total pb numbers: ", len(pbNumRanks.pb_num()))

now = datetime.datetime.now()
#print("Updated: ", (now.strftime("%Y-%m-%d %H:%M:%S")))


#create "pb_ranks.txt" file and append results to the file:
with open('pb_ranks.txt', 'w') as f:
    f.write(str(pbNumRanks.rankings()))
    f.write(str(now))


###             Debugging              ###      
  
#print("These are the powerball numbers: ", pbNumRanks.pb_num())
#print()

###             Debugging              ###   
    
    
