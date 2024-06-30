print("Thank you for choosing Python Pizza, Which size would you prefer today?")
bill = 0

size = input("").lower()

if size == 's':
    bill += 100
    s_pepperoni = input("Do you want to add pepperoni? ").lower()
    if s_pepperoni == 'y':
        bill += 20
    s_Cheese = input("Extra cheese? ").lower()
    if s_Cheese == 'y':
        bill += 10
elif size == 'm':
    bill += 200
    m_pepperoni = input("Do you want to add pepperoni? ").lower()
    if m_pepperoni == 'y':
        bill += 30
    m_Cheese = input("Extra cheese? ").lower()
    if m_Cheese == 'y':
        bill += 10
elif size == 'l':
    bill += 200
    l_pepperoni = input("Do you want to add pepperoni? ").lower()
    if l_pepperoni == 'y':
        bill += 40
    l_Cheese = input("Extra cheese? ").lower()
    if l_Cheese == 'y':
        bill += 10

print(f"Your Bill is {bill}$")



