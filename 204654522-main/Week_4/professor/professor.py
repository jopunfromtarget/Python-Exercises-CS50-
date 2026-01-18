import random

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for attempt in range(3):
            ans = int(input(f"{x} + {y} = "))
            if x + y == int(ans):
                score += 1
                break
            else:
                print("EEE")
        else:
            print(f"Answer: {x + y}")

    print(f'Score: {score}')

def get_level():
    while True:
        try:
            level = int(input("Level: ").strip())
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass



def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
