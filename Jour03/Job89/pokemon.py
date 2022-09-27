
import numpy as np
import pandas as pd

# Define path
#from kaggle I downloaded the pokemon names csv file and then compare with my data file
#to see if there is a pokemon hidden somewhere

file = open("data.txt", "r")
data = file.read()
file.close()

pokemon = pd.read_csv('pokemon.csv', sep=',', encoding = "ISO-8859-1")

pokemon_list = np.unique(pokemon['name'])

for p in pokemon_list:
    if p in data:
        print('The wanted Pokemon name is.')
        print(p)