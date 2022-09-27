import string
import pandas as pd
import matplotlib.pyplot as plt

alphabet = list(string.ascii_lowercase)

file = open("data.txt", "r")
data = file.read()
file.close()
data = data.lower()

# convert input to list
data_list = list(data)

# create a dataframe using pandas
df = pd.DataFrame({'Alphabet': data_list})

df = df[df['Alphabet'].isin(alphabet)].reset_index(drop=True)

df = df['Alphabet'].value_counts(normalize=True)


#plot my data
plt.bar(df.index, df, width=0.5, color='r')
plt.show()