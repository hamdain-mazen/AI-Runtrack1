import re

number = int(input("Please gimme a number : "))
file = open("data.txt", "r")
content = file.read()
file.close()
content = content.lower()
res = re.findall(r"\w+", content)

length = [len(r) for r in res]

filtered_lengths = [l for l in length if l == number]

print('Number of words having the  {0} lettres : {1}.'.format(number, len(filtered_lengths)))