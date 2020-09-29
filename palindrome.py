#created on: 29 September 2020
#created by Author:Victor NKuna
print("********************WELCOME TO THE PALINDROME PROGRAM********************")
print()
print()
print()

name=input("I am just going to take your details,before we can start,please enter your name below:\n")
print()
print()
sequencre_of_char = input("PLease enter a word or string:")

print()
print()
print(name,"*****WELCOME ONCE AGAIN,THE SYSTEM  WILL PROCESS THE GIVEN WORD*****:",[sequencre_of_char])

print()
print()
reverse = sequencre_of_char[::-1]  #reverse a method

# print("The reverse of the text entered is:",sequencre_of_char,"the reverse is:",proces
if sequencre_of_char==reverse:
    print([sequencre_of_char],"is a palindrome")
else:
    print([sequencre_of_char],"is not a palindrome,but i will reverse it","here is the reversed word:",[sequencre_of_char[::-1]])
