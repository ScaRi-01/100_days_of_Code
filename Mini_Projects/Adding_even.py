x = int(input("Write a number between 1-1000: "))
result = 0

for i in range(1, x+1):
    if i%2 == 0:
        result += i

print(result)