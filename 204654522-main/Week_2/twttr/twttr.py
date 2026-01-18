word = ""

slang = input("Input: ").strip()

for let in slang:
    if let.lower() not in ["a", "i", "e", "o", "u"]:
        word += let

print("Output: ", word)
