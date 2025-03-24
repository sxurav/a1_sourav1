#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Winter 2025
Program: assignment1.py
Author: "Sourav"
The python code in this file (assignment1.py) is original work written by
"Sourav". No code in this file is copied from any other source except those provided by the course instructor, including any person, textbook, or on-line resource. I have not shared this python script with anyone or anything except for submission for grading. I understand that the Academic Honesty Policy will be enforced and violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    '''
    Based on the algorithm by Tomohiko Sakamoto.
    Returns the day of the week for the given date (e.g., "sun", "mon", "tue").
    '''
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1: 0, 2: 3, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month] + date) % 7
    return days[num]

def mon_max(month: int, year: int) -> int:
    '''
    Returns the maximum number of days in a given month, considering leap years.
    '''
    # Days in each month for non-leap years, February will be adjusted based on leap year
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    # Adjust February for leap year
    if leap_year(year):
        days_in_month[2] = 29

    return days_in_month.get(month, 0)

def after(date: str) -> str:
    '''
    Returns the next day's date in YYYY-MM-DD format.
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # Move to the next day

    if tmp_day > mon_max(month, year):
        tmp_day = 1
        tmp_month = month + 1
    else:
        tmp_month = month

    if tmp_month > 12:
        tmp_month = 1
        year += 1

    next_date = f"{year}-{tmp_month:02}-{tmp_day:02}"
    return next_date

def usage():
    '''
    Print a usage message to the user when arguments are incorrect.
    '''
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD")
    sys.exit(1)

def leap_year(year: int) -> bool:
    '''
    Returns True if the year is a leap year.
    A year is a leap year if it is divisible by 4, but not by 100 unless also divisible by 400.
    '''
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def valid_date(date: str) -> bool:
    '''
    Checks if the given date is valid in the YYYY-MM-DD format.
    '''
    try:
        year, month, day = map(int, date.split('-'))
        if 1000 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= mon_max(month, year):
            return True
        return False
    except (ValueError, TypeError):
        return False

def day_count(start_date: str, stop_date: str) -> int:
    '''
    Loops through the date range, counting weekends (Saturdays and Sundays).
    '''
    weekend_count = 0
    while start_date <= stop_date:
        year, month, day = map(int, start_date.split('-'))
        if day_of_week(year, month, day) in {'sun', 'sat'}:
            weekend_count += 1

        if start_date == stop_date:
            break

        start_date = after(start_date)

    return weekend_count

if __name__ == "__main__":
    # Ensure the correct number of arguments are provided
    if len(sys.argv) != 3:
        usage()

    start_date, stop_date = sys.argv[1], sys.argv[2]

    # Validate the dates
    if not valid_date(start_date) or not valid_date(stop_date):
        usage()

    # Ensure start date is earlier than end date, swap if needed
    if start_date > stop_date:
        start_date, stop_date = stop_date, start_date

    # Count the weekend days in the date range
    weekend_days = day_count(start_date, stop_date)

    print(f"The period between {start_date} and {stop_date} includes {weekend_days} weekend days.")
