 # -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 02:17:44 2018
Author: D. Plyler 

SUMMARY: This module scrapes the www.flalottery.com website for all winning powerball lottery number sets from 7 Jan 2009 to 24 October 2018.  It captures the base html, then parses out each of the lottery numbers from their surrounding data (dates, descriptions, etc.), then sorts them by their frequency.  Finally, the results are saved to a text file for reference.  As this was a project purely for learning about web scraping and honing my python skills, I referenced www.realpython.com to get started.
"""

import requests   #using 'requests' for handling HTTP
from bs4 import BeautifulSoup   #bs4 for parsing the html
import pandas as pd   #pandas used with Series (pd.Series) to rank all results
import datetime   #used for formatting datetime

#create global datetime variable:
now = datetime.datetime.now()

#create WinningNums Class, containing the base URL:
class WinningNums:
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

    #create Method for parsing the first number of each winning number (this is needed because the raw html output combines the dates and the first number into one string inside a list):
    def first_num():       
        html = WinningNums.get_html(WinningNums.BASE_URL)
        first_num = []        
        #if the html is valid, find the numbers separated by '-', then by '/', then by spaces:        
        if html:
            for tbody in html.find_all('tbody'):
                div = tbody.text.split('-')
                div = ' '.join(div)
                div = div.split('/')               
                div = ' '.join(div)
                div = div.split(' ')                
                #capture only the last 2 numbers in strings of certain lengths:
                for x in div:
                    if len(x) in range(5, 7):
                        first_num.append(x[4:6])
                        #strip out leading zeroes to ensure only 69 results:
                        first_num = [s.lstrip("0") for s in first_num]                                      
                return (first_num)

    #create Method for parsing the middle numbers from the provided url:
    def mid_nums():        
        html = WinningNums.get_html(WinningNums.BASE_URL)
        mid_nums = []        
        if html:
            for tbody in html.find_all('tbody'):
                div = tbody.text.split('-')
                div = ' '.join(div)
                div = div.split()                
                #ensure we only capture numbers and exclude any digits that are sometimes captured in this set of numbers
                for x in div:
                    if x.isdigit():
                        mid_nums.append(x)
                        mid_nums = [s.lstrip("0") for s in mid_nums]                
                return mid_nums 

    #create Method for parsing the last number from the provided url                (again, this is needed because the raw html output combines the last number with the PB number and remaining text):
    def last_num():
        html = WinningNums.get_html(WinningNums.BASE_URL)
        last_num = []        
        if html:
            for tbody in html.find_all('tbody'):
                div = tbody.text.split('-')
                for x in div:
                    if 'PB' in x:
                        x = x[1:4]
                        x = x.split()
                        x = ' '.join(x)
                        last_num.append(x)
                        last_num = [s.lstrip("0") for s in last_num]                
                return (last_num)            
    
    #create Method for parsing the PB number from the provided url:
    def pb_num():
        html = WinningNums.get_html(WinningNums.BASE_URL)
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
                return (pb_num)            
            
    #create Method for combining all the numbers into one list, then sort them by frequency of occurrence using panda Series:
    def winners():
        winners = WinningNums.first_num() + WinningNums.mid_nums() + WinningNums.last_num() + WinningNums.pb_num()
        return winners
        #print(pd.Series(winners).value_counts()
        
    def winners_sort():
        winners_sort = WinningNums.first_num() + WinningNums.mid_nums() + WinningNums.last_num() + WinningNums.pb_num()        
        return pd.Series(winners_sort).value_counts()
    
#execute these actions ONLY when this module is run (NOT when called by other modules):
if __name__ == "__main__":
    
    #ensure all pandas results are captured: 
    pd.set_option('display.max_rows', 100)
    print("This is the list of winning numbers by rank: ")
    print()
    print(WinningNums.winners_sort())
    print()
    print("Total unique numbers captured: ", len(WinningNums.winners_sort()))
    #write results to file:
    with open('winning.txt', 'w') as f:
        f.write(str(WinningNums.winners_sort()))
        f.write(str(now))
    print()
    print("Program finished at", (now.strftime("%Y-%m-%d %H:%M:%S")))


###             Debugging              ###      
     
#print("These are the first numbers: ", WinningNums.first_num())
#print(len(WinningNums.first_num()))
#print()
#print("These are the middle numbers: ", WinningNums.mid_nums())
#print(len(WinningNums.mid_nums()))
#print()
#print("These are the last numbers: ", WinningNums.last_num())
#print(len(WinningNums.last_num()))
#print()
#print("These are the powerball numbers: ", WinningNums.pb_num())
#print(len(WinningNums.pb_num()))
#print()

###             Debugging              ###   
    
    
