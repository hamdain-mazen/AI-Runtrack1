import re
import pandas as pd
import matplotlib.pyplot as plt

file = open("data.txt", "r")
data = file.read()
file.close()
data = data.lower()

res = re.findall(r"\w+", data)

lengths = [len(r) for r in res]

df = pd.DataFrame({'size': lengths})

df = df['size'].value_counts(normalize=True)

plt.bar(df.index, df, width=0.75, color='r')
plt.show()