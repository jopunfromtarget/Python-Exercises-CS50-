camel_case = input("camelCase: ").strip(" ")
camel = ""

for c in camel_case:
    if c.isupper():
        camel += "_" + c.lower()
    else:
        camel += c

print("snake_case:", camel)
