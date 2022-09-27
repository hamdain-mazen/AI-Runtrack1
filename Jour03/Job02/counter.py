

import re

# initialize text
txt = open("data.txt", "r")
words = txt.read()
# using the re findall
result = len(re.findall(r'\w+', words))

print("There are " + str(result) + " words.")
