months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ").replace("/", " ").title()
        month, day, year = date.split()
        if month in months:
            # Word format (October 27, 2006)
            if "," not in date:
                raise ValueError

            date = date.replace(",", " ")
            month, day, year = date.split()
            month_index = int(months.index(month).__str__()) + 1
            print(f"{int(year):03}-{int(month_index):02}-{int(day):02}")
        else:
            # YYYY/MM/DD Format
            print(f"{int(year)}-{int(month):02d}-{int(day):02}")
    except EOFError:
        # CTRL + D
        break
    except (NameError, ValueError):
        pass
