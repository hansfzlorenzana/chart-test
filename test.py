import pandas as pd

df = pd.read_csv('coordinates_logs.csv', delimiter=',')

df

list_of_csv = [list(row) for row in df.values]

print(list_of_csv)