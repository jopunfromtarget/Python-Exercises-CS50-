import inflect
p = inflect.engine()

names = []

while True:

    try:
        name = input().strip()
        names.append(name)
        song = p.join(names).strip()
    except EOFError:
        print("Adieu, adieu, to", song)
        break
