import re

email = input("Enter Email ID: ")
password = input("Enter Password: ")

email_pattern = r'^[A-Za-z0-9][A-Za-z0-9._%+-]*@[A-Za-z0-9.-]+\.(com|org|edu|in)$'

password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!*])[A-Za-z\d@#$%&!*]{8,}$'

if re.fullmatch(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")

if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Invalid Password")
