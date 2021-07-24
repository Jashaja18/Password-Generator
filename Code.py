# import necessary modules
import random
import string

print('Hello, Welcome to Password Generator')

# input the length of characters you would like
length = int(input('\nEnter a number to get started: '))

# define data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

# combine the data
all = lower + upper + num + symbols

# use random
temp = random.sample(all, length)

# create the password
password = "".join(temp)
