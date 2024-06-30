import random
i = input("Heads or Tails: ")
random_choice = random.randint(0,2)
if random_choice == 0:
    print("Heads!")
elif random_choice == 1:
    print("tails!")