
def main():
    answer = input("Input: ").strip()
    print(shorten(answer))

def shorten(answer):

    word = ""

    for let in answer:
        if let.lower() not in ["a", "i", "e", "o", "u"]:
            word += let

    return word

if __name__ == "__main__":
    main()
