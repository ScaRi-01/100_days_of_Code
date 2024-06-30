# my_list = []
# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row[1])

import pandas as pd

df = pd.read_csv("weather_data.csv")

# temp_list = df["temp"].to_list()
# print(df['temp'].max())

print(df[df['day'] == 'Monday'])
print(df[df.temp == df.temp.max()])
my_list = df.temp.to_list()

print(my_list)

print(list(map(lambda x:x**2, df.temp.to_list())))