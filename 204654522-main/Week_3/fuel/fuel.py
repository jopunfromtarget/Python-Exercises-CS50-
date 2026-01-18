def main():
    while True:
        try:
            num, dem = input("Fraction: ").split("/")
            perc = (int(num)/int(dem)) * 100
            if 99 <= perc <= 100:
                print("F")
            elif 0 <= perc <= 1:
                print("E")
            elif perc < 0:
                err = perc / 0
            elif perc > 100:
                err_2 = perc / 0
            else:
                new = round(perc).__str__() + "%"
                print(new)
            return False
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
main()
