import calendar

# Function to print the calendar with holidays
def print_calendar(year):
    # Create a TextCalendar instance
    cal = calendar.TextCalendar()

    # Define holidays
    holidays = {
        "01-01": "New Year's Day",
        "26-01": "Republic Day",
        "08-03": "Holi",
        "25-03": "Good Friday",
        "01-05": "Labour Day",
        "15-08": "Independence Day",
        "02-10": "Gandhi Jayanti",
        "25-12": "Christmas",
    }

    print(f"\nCalendar for the Year {year}\n")
    
    # Loop through each month
    for month in range(1, 13):
        # Print the month
        print(cal.formatmonth(year, month))

        # Check if any holidays fall in the current month
        month_days = calendar.monthcalendar(year, month)
        for week in month_days:
            for day in week:
                if day != 0:  # day is not a placeholder (0 means no day)
                    date_str = f"{day:02d}-{month:02d}"
                    if date_str in holidays:
                        print(f"Holiday: {holidays[date_str]} on {date_str}")

# Run the calendar function for the year 2024
print_calendar(2024)
