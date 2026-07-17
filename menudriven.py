import math

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b

while True:
    print("Menu: 1.Add 2.Subtract 3.Multiply 4.Divide 5.Sqrt 6.Exit")
    ch = int(input("Enter your choice: "))

    if ch == 6:
        break

    if ch == 5:
        x = int(input("Enter a number:"))
        print("Square root=", math.sqrt(x))

    else:
        a = int(input("Enter first number:"))
        b = int(input("Enter second number:"))

        if ch == 1: print("Sum =", add(a,b))
        elif ch == 2: print("Difference =", sub(a,b))
        elif ch == 3: print("product =", mul(a,b))
        elif ch == 4: print("Quotient =", div(a,b))

