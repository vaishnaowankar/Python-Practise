#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

no_of_turns = 0



def logic():
  global no_of_turns
  number = random.randint(1,100)
  print(f"You have {no_of_turns} attempts remaining to guess the number.")
  while no_of_turns > 0:
    number_guess = int(input("Guess the number: "))
    
    if number_guess == number:
      print(f"You guessed it right, it was {number}.... YOU WON!")
      exit()
    elif number_guess > number:
      print("Too High")
    else:
      print("Too Low")
      

    no_of_turns -= 1
    if no_of_turns == 0:
      break
    print(f"You have {no_of_turns} attempts remaining to guess the number.")

  print("You run out of guesses. YOU LOSE")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I have a number in my mind between 1 and 100, Guess it!")

choice = input("Which mode you want to play? : 'easy' or 'hard'\n").lower()

if choice == "easy":
  no_of_turns = 10
  logic()
elif choice == "hard":
  no_of_turns = 5
  logic()
else:
  print("Invalid Input") 













