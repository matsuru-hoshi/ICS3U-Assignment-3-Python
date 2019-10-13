#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program gives user number of days in a month based on month given


# lists for month with 31 and 30 days    elif month == "april"

days_with_31 = ["january", "march", "may", "july", "august", "october",
                "december"]
days_with_30 = ["april", "june", "september", "november"]


def main():
    # funciton gives user number of days in month

    # Welcome statement
    print("Welcome, I will tell you the number of days in a month.\n*Leap"
          " years work as well.")
    input("Press Enter to continue.\n")

    # input
    month = input("What month is it:")
    year = int(input("What year is it:"))

    # makes sure anything the user inputs is formated to lower case
    # This way it doesn't matter if they type first letter capital or something
    month = month.lower()

    days = 0
    # process
    if month in days_with_31:
        days = 31
    elif month in days_with_30:
        days = 30
    # deal with february
    elif month == "february":
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400:
                    days == 29
            else:
                days = 29
    else:
        print("Invalid input.")

    print("\n" + str(month.capitalize()) + " of " + str(year) + " has " +
          str(days) + " days.")
    # output


if __name__ == "__main__":
    main()