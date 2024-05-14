n = int(input("Number: "))
is_prime = True 

def prime_checker(num = n):
    for i in range(2,100):
        if num % i == 0:
            is_prime = False
    if is_prime:
        print("It's Prime")
    else:
        print("Not Prime")

prime_checker()



