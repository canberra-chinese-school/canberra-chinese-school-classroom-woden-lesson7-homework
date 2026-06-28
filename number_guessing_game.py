# This is the number guessing game we made in class

import random

random_number = random.randint(1, 100)
user_guess = int(input("Guess the number between 1 and 100:"))
while random_number != user_guess:
    if user_guess > random_number:
        print("Too big!")
    elif user_guess < random_number:
        print("Too small!")
    user_guess = int(input("Guess the number between 1 and 100:"))

print("You got it right!")
print("Random number = " + str(random_number))





