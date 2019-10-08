 # -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 02:17:44 2018
Author: dp

SUMMARY: This module scrapes the www.flalottery.com website for all winning powerball lottery number sets from 7 Jan 2009 to 24 October 2018.  It captures the base html, then parses out each of the lottery numbers from their surrounding data (dates, descriptions, etc.), then sorts them by their frequency.  Finally, the results are exported to a csv file for reference, if desired, through a tkinter window.  As this was a project purely for learning about web scraping and honing my python skills, I referenced www.realpython.com to get started.
"""
import requests   #using 'requests' for handling HTTP
from bs4 import BeautifulSoup   #bs4 for parsing the html
from pandas import DataFrame   #for creating a dataframe (df)
from pandas import set_option   #pandas used with Series (pd.Series) to rank all results
from pandas import Series #pandas used with Series (pd.Series) to rank all results
import datetime   #used for formatting datetime
import re  #use regular expressions to help parse data
import tkinter as tk #for 'file save as' window
from tkinter import filedialog #for 'file save as' window

#create global datetime variable:
now = datetime.datetime.now()

#create WinningNums Class, containing the base URL:
url = 'http://www.flalottery.com/site/winningNumberSearch?searchTypeIn=range&gameNameIn=POWERBALL&singleDateIn=&fromDateIn=01%2F07%2F2009&toDateIn=10%2F24%2F2018&n1In=&n2In=&n3In=&n4In=&n5In=&n6In=&pbIn=&mbIn=&lbIn=&pnIn=&cbIn=&submitForm=Submit'
       
fl_lottery = requests.get(url) #store raw url data as fl_lottery
html = BeautifulSoup(fl_lottery.text, 'html.parser') #parse url data
dataSet = [] #create empty container for our data
for raw_data in html.findAll('table', attrs={"class": "style1 games"}):
    raw_data = raw_data.text
    dataSet.append(raw_data) #dataSet is list of all numbers

dataString = ''.join(dataSet) #convert list to strings

#define patterns for the numbers and dates
PBnums = re.compile(r'(\d{1,6}\s-\s\d{1,2}\s-\s\d{1,2}\s-\s\d{1,2}\s-\s\d{1,2}\sPB\s\d{1,2})')  #define winning number pattern
PBdates = re.compile(r'(\d{1,2}.\d{1,2}.\d{4})')  #define winning date pattern

dateMatch = PBdates.finditer(dataString) #find all winning dates in PBdates
numMatch = PBnums.finditer(dataString) #find all winning numbers in PBnums

nums = []
for match in numMatch: #print all winning number sets
    numbers = match.group(1)[4:]
    nums.append(numbers)

dates = []
for match in dateMatch: #print all winning date sets
    date = match.group(1)
    dates.append(date)

#create winning date, number pairs:
data_pairs = {'Dates' : dates, 'Numbers' : nums} #first, create a dictionary
df = DataFrame(data_pairs, columns = ['Dates', 'Numbers'])

class WinningNums(): #create overall class for winning numbers
    #create method to parse out first five PB numbers into one list:
    def firstFive():
        firstFive = re.compile(r'(\d{1,2})\s-\s(\d{1,2})\s-\s(\d{1,2})\s-\s(\d{1,2})\s-\s(\d{1,2})')
        div = '  '.join(nums)
        numMatch = firstFive.finditer(div) #find all winning numbers in PBnums
        first_nums = []
        for match in numMatch: #print all winning number sets
            first = match.group(1)
            sec = match.group(2)
            third = match.group(3)
            fourth = match.group(4)
            fifth = match.group(5)
            first_nums.append(first)
            first_nums.append(sec)
            first_nums.append(third)
            first_nums.append(fourth)
            first_nums.append(fifth)            
        return (first_nums)
    
    #create method for parsing the PB number from the provided url:
    def pb_nums():
        pbNums = re.compile(r'(PB\s\d{1,2})') 
        div = '  '.join(nums)
        numMatch = pbNums.finditer(div) #find all winning numbers in PBnums
        pb_nums = []
        for match in numMatch: #print all winning number sets
            numbers = match.group(1)[2:]
            pb_nums.append(numbers)
            pb_nums = [s.lstrip(" ") for s in pb_nums]
        return (pb_nums)
    
    def winners(): #create method for returning all winning numbers
       winners = WinningNums.firstFive() + WinningNums.pb_nums()
       return winners
   
    def winners_sort(): #create method for sorting unique winning numbers
       winners_sort = WinningNums.firstFive() + WinningNums.pb_nums()        
       return Series(winners_sort).value_counts()
            
           

if __name__ == "__main__":
    #ensure all pandas results are captured: 
    set_option('display.max_rows', 100)
    print('-' *10, ' BEGIN ', '-'*15,'\n')
    print("These are the first five winning numbers: ", '\n')
    print(WinningNums.firstFive(), '\n')        
    print("These are the PB numbers: ", '\n')
    print(WinningNums.pb_nums(), '\n')
    print("This is the list of all unique winning numbers sorted by frequency: ", '\n')
    print(WinningNums.winners_sort(), '\n')
    print("Total unique numbers captured (should ALWAYS be 69!): ", len(WinningNums.winners_sort()))
    print("Total number of PBs is: ", len(WinningNums.pb_nums()))
    print("Total number of first five winning numbers is: ", len(WinningNums.firstFive()))
    print("Total number of all winning numbers (including duplicates) is: ", len(WinningNums.winners()),'\n')
    print("-"*10, "PROGRAM FINISHED AT", (now.strftime("%Y-%m-%d %H:%M:%S")))
    #write pandas data to csv file using tkinter
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 200, height = 100, bg = 'lightsteelblue2', relief = 'raised')
    canvas1.pack()
    def exportCSV ():
        global df
        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv (export_file_path, index = None, header=True)
    saveAsButton_CSV = tk.Button(text='Export to CSV file', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(100, 50, window=saveAsButton_CSV)
    root.mainloop()





###             Debugging              ###      
     

###             Debugging              ###   
    
    
