<<<<<<< HEAD:pb_lotto_2018.py
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:42:49 2018 
Author: D. Plyler

SUMMARY: This project was conducted to strengthen my current Python skillset while building web scraping familiarity and is not designed to predict any winning lottery combinations.  Rather, it is designed to collect and observe data, looking for any trends out of mere curiosity.  This specific module calls on 'pb_winningNums' to determine the winning powerball lottery numbers from 2009 to 2018 in order of their frequency.  It then prints out the results, the total number of unique winning numbers captured and the date/time the program was executed.
   
"""
#imports and executes the module containing the class and supporting functions:
import pb_winningNums

pd.set_option('display.max_rows', 100)
print("This is the list of winning numbers by rank:\n",  (WinningNums.winners_sort()))
print()

print("Total numbers captured: ", len(WinningNums.winners_sort()))
print()

now = datetime.datetime.now()
print("Updated: ", (now.strftime("%Y-%m-%d %H:%M:%S")))

=======
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:42:49 2018 
Author: D. Plyler

SUMMARY: This project was conducted to strengthen my current Python skillset while building web scraping familiarity and is not designed to predict any winning lottery combinations.  Rather, it is designed to collect and observe data, looking for any trends out of mere curiosity.  This specific module calls on 'pb_winningNums' to determine the winning powerball lottery numbers from 2009 to 2018 in order of their frequency.  It then prints out the results, the total number of unique winning numbers captured and the date/time the program was executed.
   
"""
#imports and executes the module containing the class and supporting functions:
import pb_winningNums

pd.set_option('display.max_rows', 100)
print("This is the list of winning numbers by rank:\n",  (WinningNums.winners_sort()))
print()

print("Total numbers captured: ", len(WinningNums.winners_sort()))
print()

now = datetime.datetime.now()
print("Updated: ", (now.strftime("%Y-%m-%d %H:%M:%S")))

>>>>>>> c7e957b2707f8166e834567dafd84d15d5d253ee:pb_lotto_2018.py
