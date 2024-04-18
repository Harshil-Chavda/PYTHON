import datetime
def print_sundays(year):
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    while start_date <= end_date:
        if start_date.weekday() == 6: # 6 represents Sunday
            print(start_date)
        start_date += datetime.timedelta(days=1)
print("Welcome to the Sunday dates printer!")
year = int(input("Enter the year you want to print Sunday dates for: "))
if year < 1:
    print("Invalid input. Please enter a year greater than 0.")
else:
    print_sundays(year)