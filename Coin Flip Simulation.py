#Coin Flip Simulation
#Write some code that simulates flipping a single coin however many times the user decides.
#The code should record the outcomes and count the number of tails and heads.
import random
def no_input():
    while True:
        try:
            n = int(input("How many times you want to flip a coin: "))
            if n>0:
                return n
            else:
                print("Enter a Number(>0). Try Again")
        except:
            print("Invalid Entry! Try Again")
            
print("COIN FLIPPING SIMULATION")
num=no_input()
outcome = []
for i in range(0,num):
    x=random.randint(0,1)
    if x==0:
        outcome.append("H")
    else:
        outcome.append("T")
HEADS = outcome.count("H")
TAILS = outcome.count("T")
print(f"The outcome of flipping the coin {num} times -")
print(outcome)
print(f"Heads: {HEADS}")
print(f"Tails: {TAILS}")