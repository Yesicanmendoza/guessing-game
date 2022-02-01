"""A number-guessing game."""
import random

# Put your code here

print("Howdy, what's your name?")
name = input("(type in your name) ")
print(name, "I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
my_number = random.randint(1,100)
