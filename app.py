

print("Enter the number: ")
x = int(input())
print("Enter the operator: ")
calculus_operator = input()
print("Enter the second number: ")
y = int(input())

def calculator():
    if calculus_operator == '+':
        a = x + y
        print(a)
    elif calculus_operator == '-':
        a = x - y
        print(a)
    elif calculus_operator == '*':
        a = x * y
        print(a)
    elif calculus_operator == '/':
        a = x / y
        print(a)

    else:
        print("Invalid syntax")

calculator()
