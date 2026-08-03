import random
import string

#1. Combine letters, numbers, and symbols into one big text pool
characters = string.ascii_letters + string.digits + string.punctuation

#2. Pick random characters from that pool and join them together
password = "".join(random.choice(characters) for _ in range(length))

#3. user input for password length
print("Welcome to the Password Generator!")
length = int(input("Enter the desired password length: "))

#4. Print the final password to the screen
print("Your new password is:", password)