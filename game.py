"""A number-guessing game."""
import random

# Put your code here

print("Howdy, what's your name?")
name = input("(type in your name) ")
print(name, "I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
my_number = random.randint(1,100)

counter = 0
while True:
    guess=int(input("Your guess? " ))
    counter = counter + 1
    if guess > my_number:
        print("Your guess is too high, try again.")
    elif guess < my_number:
        print("Your guess is too low, try again.")
    else:
        break

print("Well done,", name,"! You found my number in", counter ,"tries!")

    

