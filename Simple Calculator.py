#Calculator - A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

def operation(a,op):
    
    b=int(input("Enter Number: "))
    if op == '+':
        a=a+b
    elif op == '-':
        a=a-b
    elif op == '*':
        a=a*b
    elif op == '/':
        a=a/b
    else:
        print("Invalid Operator")
    return a
    
    

print("CALCULATOR")
print("TO EXIT PRESS 'Y'")
x = int(input("Enter 1st Number: "))
while True:
    op= input("Enter Operator (+,-,*,/,=,Y): ")
    if op=='Y':
        break
    elif op=='=':
        print(x)
    else:
        x=operation(x,op)
        print(x)
        
print("THANKYOU!")