import random

upper = input("Level: ").strip()
rand_int = random.randint(1, int(upper))

while True:
    try:
        guess = int(input("Guess: ").strip())
        if 0 < guess < rand_int:
            print("Too small!")
            pass
        elif guess > rand_int:
            print("Too large!")
            pass
        elif guess == rand_int:
            print("Just right!")
            break
        elif guess < 0:
            pass
    except ValueError:
        pass
