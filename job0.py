print("Hello world!")

import re

life = "The rain in Spain"
x = re.search("^The.*Spain$", life)
print(x)