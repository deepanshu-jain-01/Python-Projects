#Check if Palindrome - Checks if the string entered by the user is a palindrome. 
my_str = input("Please enter a string to check if it is palindrome : ")
rev = my_str[::-1]
if my_str.lower() == rev.lower():
    print("It is Palindrome.")
else:
    print("It is not Palindrome.")
