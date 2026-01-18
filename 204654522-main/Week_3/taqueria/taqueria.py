menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    total = 0
    while True:
        try:
            item = input("Item: ").title().strip()
            if item in menu:
                total += menu[item]
                tot_a = format(total, ".2f")
                tot_af = "$" + tot_a.__str__()
                print("Total: ", tot_af)
                pass
            else:
                pass
        except (ValueError, KeyError, NameError):
            pass
        except EOFError:
            return False

main()
