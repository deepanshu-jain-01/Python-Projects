#Count Vowels - Enter a string and the program counts the number of vowels in the text. 
#For added complexity have it report a sum of each vowel found

my_str = input("Please enter a string : ")
a_count = my_str.upper().count("A")
e_count = my_str.upper().count("E")
i_count = my_str.upper().count("I")
o_count = my_str.upper().count("O")
u_count = my_str.upper().count("U")

print(f"Total No. of Vowels Found: {a_count+e_count+i_count+o_count+u_count}")
print(f"A: {a_count} ,  E: {e_count} ,  I: {i_count} ,  O: {o_count} ,  U: {u_count}") 