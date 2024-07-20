import random
import string

def passw(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
    return password

x = 0
while x <= 0:
    try:
        x = int(input("Enter the length for the password: "))
        if x <= 0:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input , Please enter a valid positive integer ")

password = passw(x)
print("Generated Password:",password)
