#import libraries
import random
import string

# Heading
  
print("RANDOM PASSWORD GENERATOR")
print("--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--x--")

# Code
def generate_password():
 lowerletters='abcdefghijklmnopqrstuvwxyz'
 upperletters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 numbers='1234567890'
 symbols='!@#$%^&*=+-_/~'

# combine all to create password

 combine=lowerletters+upperletters+symbols+numbers
 passlength=int(input("Enter the length of password: "))

#use random function
 template= random.sample(combine,passlength)

 password= " ".join(template)

#Print the password
 print("The password generate: ",password)

#LOOP
while True:
 generate_password()

 choice=input("Do you want to create a password again(yes/no)? : ").lower()
 if(choice!='yes' and  choice!='y'):
  print("Exiting Password Generator !!!")
  break

#Default
print("Thank you!!")