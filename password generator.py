'''Name: Areesha Kaleem
codsoft internship Sep Batch A3'''


import random
from art import *
tprint("Password  Generator",font="medium")
length = int(input("Enter length of password :"))
character = input ("Do you want add special character (yes/no):")
case_p = input("Do you want to add upper case alphabets (yes/no):")
case_l = input("Do you want to add lower case alphabet (yes/no):")
digits = input("Do you want to add digits (yes/no):")
generate_password = ""

sc = "!@#$%^&*()_|:<>?/';,.`~="
alp = "abcdefghijklmnopqrstuvwxyz"
d = "123456789"

for i in range(length):
    if character == "yes":
        generate_password += random.choice(sc)
    if case_p == "yes":
        upc = random.choice(alp)
        generate_password += upc.upper()
    if case_l == "yes":
        generate_password += random.choice(alp)
    if digits == "yes":
        generate_password += random.choice(d)

if len(generate_password) == length:
    print(generate_password)
else:
    generate_password = generate_password[0:length]
    print(generate_password)