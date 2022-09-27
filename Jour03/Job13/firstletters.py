import os
import re
import pandas as pd
import matplotlib.pyplot as plt


file = open("data.txt", "r")
data = file.read()
file.close()
data = data.lower()

res = re.findall(r"\w+", data)
    
first_letters = [w[0] for w in res]

df = pd.DataFrame({'Occurence': first_letters})

df = df['Occurence'].value_counts(normalize=True)



freqs = {}
text=  open('data.txt') 
for line in text:
        for letter in line:
            if letter in freqs:
                freqs[letter] += 1
            else:
                freqs[letter] = 1

print(freqs)




plt.bar(df.index, df, width=0.75, color='r')
plt.title("Occurences of first letters")
plt.ylabel("Number of occurence")
plt.xlabel("Lettres")
plt.show()



