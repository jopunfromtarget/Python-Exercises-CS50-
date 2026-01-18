from emoji import emojize

data = []

text = input("Input: ").strip()
data.append(text.split())

for emoji in data:
    print("Output: ", emojize(text, language="alias"))
