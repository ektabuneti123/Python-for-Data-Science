import calendar

print("Ekta S078")
print("-------------------------------------------------------------------------")

def show_full_year_calendar(year):
    print("\nFull Calendar for", year, ":\n")
    print(calendar.calendar(year))

def show_month_calendar(year, month):
    print("\nCalendar for", calendar.month_name[month], year, ":\n")
    print(calendar.month(year, month))

def is_leap_year(year):
    if calendar.isleap(year):
        print("\n", year, "is a leap year.")
    else:
        print("\n", year, "is not a leap year.")

print("Calendar Module")

# Ask user for year
year = int(input("Enter the year: "))

# Display full year calendar
show_full_year_calendar(2027)

# Ask user for month
month = int(input("\nEnter the month number (1-12) to view that month's calendar: "))

# Display month calendar
show_month_calendar(2027, month)

# Check leap year
is_leap_year(2027)
