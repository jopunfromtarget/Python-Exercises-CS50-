def main():
    greeting = input("Greeting: ").lower()
    print(value(greeting))

def value(greeting):

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    elif greeting.startswith("h", 7, 9):
        return 20
    elif greeting:
        return 100


if __name__ == "__main__":
    main()
