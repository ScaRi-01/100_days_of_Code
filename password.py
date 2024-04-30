import random
print("Welcome to PyPassword generator!")
letter = int(input("letters: "))
sym = int(input("symbols: "))
num = int(input("numbers: "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password1 = []
password2 = []
password3 = []

for i in range(0,letter):
    random.shuffle(letters)
    password1.append(str(letters[i]))

for i in range(0,num):
    random.shuffle(numbers)
    password2.append(numbers[i])

for i in range(0,sym):
    random.shuffle(symbols)
    password3.append(str(symbols[i]))

combined_pass = password1+password2+password3
combined_str = [str(item) for item in combined_pass]
result = ''.join(combined_str)

print(result)

