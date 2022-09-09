#Factorial Finder
def no_input():
    while True:
        try:
            n = int(input("Enter the number to find its factorial: "))
            if n>-1:
                return n
            else:
                print("Enter Only Positive Number. Try Again")
        except:
            print("Enter Only Positive Integer Value! Try Again")

print("FACTORIAL FINDER")
num=no_input()
f=1
if num == 0:
    print(f"Factorial of {num} is 1.")
else:
    for i in range(1,num+1):
        f=i*f
    print(f"Factorial of {num} is {f}.")