# -*- coding: utf-8 -*-
"""
Author: D. Plyler

SUMMARY: This project was conducted to strengthen my current Python skillset while building web scraping familiarity and is not designed to predict any winning lottery combinations.  Rather, it is designed to collect and observe data, looking for any trends out of mere curiosity.  This specific module calls on 'pbWinningNums' to determine the winning powerball lottery numbers from 2009 to 2018 in order of their frequency.  It then prints out the results, the total number of unique winning numbers captured (this should always be 69 as there are only 69 numbers used in the Powerball lottery) and the date/time the program was executed.   
"""
#imports and executes the module containing the class and supporting functions:
import pbWinningNums

#ensure these actions only run explicitly, NOT when called by other modules:
def main():
    pass

if __name__ == "__main__":
    
    pd.set_option('display.max_rows', 100)
    print("This is the list of winning numbers by rank: ")
    print()
    print(WinningNums.winners_sort())
    print()
    print("Total numbers captured: ", len(WinningNums.winners_sort()))
    print()
    now = datetime.datetime.now()
    print("Execution completed at ", (now.strftime("%Y-%m-%d %H:%M:%S")))
    
    main()
