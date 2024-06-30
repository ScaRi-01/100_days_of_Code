import pandas as pd

# Define the file path
file_path = "nato_phonetic_alphabet.csv"

# Load the CSV file into a DataFrame
df = pd.read_csv(file_path)

data_dict = {row.letter:row.code for index, row in df.iterrows()}


user_input = input("name: ").upper()
lst = [char for char in user_input]

output = [data_dict[letter] for letter in lst]
print(output)


