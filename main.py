month_codes = {"January": 4, "February": 0, "March": 0, "April": 3,
               "May": 5, "June": 1, "July": 3, "August": 6,
               "September": 2, "October": 4, "November": 0,
               "December": 3}

century_codes = {1600: 0, 1700: 5, 1800: 3, 1900: 1, 2000: 0,
                 2100: 5, 2200: 3}

date = int(input("Enter the date:"))
month = input("Enter the month:")
century = int(input("Enter the century:"))
year = int(input("Enter the year:"))

if month == "January" or month == "February":
    day = (((year // 4) + year + 2 + month_codes[month] + century_codes[century] + date) % 7) - 1
    print(day, "of the week")

else:
    day = ((year // 4) + year + 2 + month_codes[month] + century_codes[century] + date) % 7
    print(day, "of the week")