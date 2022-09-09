#Collatz Conjecture
#Start with a number n > 1. Find the number of steps it takes to reach one using the following process: 
#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

def no_input():
    while True:
        try:
            n = int(input("Enter a number greater than 1: "))
            if n>1:
                return n
            else:
                print("Number should be greater than 1. Try Again")
        except:
            print("Invalid Entry! Try Again")
print("Collatz Conjecture Algorithm")
num=no_input()
count = 0
while num!=1:
    if num%2 == 0:
        num=num/2
    else:
        num=(num*3)+1
    count=count+1
print(f"No. of steps taken to reach 1 by Collatz Conjecture algo. are : {count}")