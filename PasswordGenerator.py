import string
import random

def generate(length,numbers=True,punctuation=True):
    letters=string.ascii_letters
    digits=string.digits
    special_characters=string.punctuation
    
    pwd=""
    has_number=False
    has_punctuation=False
    
    chars=letters
    if numbers:
        chars+=digits
        
    if punctuation:
        chars+=special_characters
    
    while len(pwd)<length:
        char=random.choice(chars)
        pwd+=char
    print("Your password is: ",pwd)
    
length=int(input("Enter the length of your password: "))
want_numbers=input("You want numbers in your password [y/n]: ") == "y" 
want_special=input("You want special characters [y/n]: ")

generate(length,want_numbers,want_special)