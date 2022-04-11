import random, time

print("Welcome to your Password Generator!")

#string of all characters, numbers and a few symbols we can include in our passwords
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&!()+@'

number = input('Please enter the number of passwords you want to generate: ')
number = int(number)

length = input("PLease enter the length of passwords required: ")
length = int(length)

print("Generating your passwords:")
print("...\n")

time.sleep(2)

for p in range(number):
	passwords = ''
	for c in range(length):
		passwords += random.choice(characters)
	print(passwords)