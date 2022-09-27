"""txt = open("domains.xml", "r")
words = txt.read()

import re
result = re.findall("\.com", words)
nb_words = len(words)
print(result)
print(nb_words)"""


import os
import re

file = open("domains.xml", "r")
content = file.read()
file.close()
res = re.findall(r"\.[a-z]{2,4}[<|/|\n]", content)

print('Number of extensions in the file is  : {}.'.format(len(res)))
