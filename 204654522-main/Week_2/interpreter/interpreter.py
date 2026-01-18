x, y, z = input("Expression: ").split(" ")

if float(x) and float(z) and y == "+":
    print(float(x) + float(z))
elif float(x) and float(z) and y == "-":
    print(float(x) - float(z))
elif float(x) and float(z) and y == "*":
    print(float(x) * float(z))
else:
    print(float(x) / float(z))
