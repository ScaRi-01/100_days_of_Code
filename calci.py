while True:
    input1 = input("Enter first digit: ")
    if input1.isdigit():
        a = int(input1)
        break
    else:
        print("Invalid")
while True:
    o = input("Operator: ")
    if o in ["+" , "-" , "/" , "*"]:
        operator = o
        break
    else:
        print("Invalid")
while True:
    input2 = input("Enter second digit: ")
    if input2.isdigit():
        b = int(input2)
        break
    else:
        print("Invalid")

if operator == "+":
    print("a+b = ", a+b)
elif 0 == "-":
    print("a-b = ", a-b)
elif o == "*":
    print("a*b = ", a*b)
elif o == "/":
    print("a/b = ", a/b)