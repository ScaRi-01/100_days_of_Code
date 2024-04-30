print("The love calculator is calculating your score......")
a = input("Your Name: ").lower()
b = input("Your Partners Name: ").lower()

a = list(a)
b = list(b)
score1 = 0
score2 = 0
for i in a:
    if i in ('t','r','u','e','l','o','v','e'):
        score1 +=1
for j in b:
    if j in ('t','r','u','e','l','o','v','e'):
        score2 +=1
print(f"Your score is {score1}{score2}")
