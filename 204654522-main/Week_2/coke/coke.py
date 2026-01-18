price = 50

while price > 0:
    print("Amount due:", price)
    change = int(input("Insert coin:"))
    if change in [5, 10, 25, 50]:
        if change >= price:
            print("Change owed:", abs(price - change))
            break
        else:
            price -= change
    else:
        price = price - 0
