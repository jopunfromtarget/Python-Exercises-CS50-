def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip("$"))
    percent = percent_to_float(input("What percentage would you like to tip? ").strip("%"))
    tip = tip_conversion(float(dollars * percent))
    print(f"Leave ${tip:.2f}")

def dollars_to_float(dollars):
    return float(dollars)

def percent_to_float(percent):
    return float(percent) * 0.01

def tip_conversion(tip):
    return float(tip)

main()
