import pandas as pd

# Reading a CSV file
df = pd.read_csv('file.csv')
print(df.head())


# Reading a text file with a delimiter (e.g., tab-separated values)
df = pd.read_csv('file.txt', delimiter='\t')
print(df.head())

#With numpy 

import numpy as np

# Reading a CSV file
data = np.genfromtxt('file.csv', delimiter=',', skip_header=1)
print(data)

# Reading a text file with a delimiter (e.g., tab-separated values)
data = np.genfromtxt('file.txt', delimiter='\t', skip_header=1)
print(data)
