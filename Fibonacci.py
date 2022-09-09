#fibonacci sequence
#Enter a number and have the program generate the Fibonacci sequence to that Nth number.

def no_input():
    while True:
        try:
            n = int(input("Enter number upto which you want FIBONACCI series: "))
            return n
        except:
            print("Invalid Output! Try Again")
            
fib=[0,1]
num = no_input()
for i in range(0,num-2):
    x=fib[i]+fib[i+1]
    fib.append(x)
print(fib)
