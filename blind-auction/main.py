from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo
print(logo)

data = dict()

state = False
while not state:

  name = input("What is your name: ")
  bid = int(input("Enter your bid price: $"))

  
  data.update({name:bid})
  

  ques = input("Are there any other biders?'yes' or 'no' ").lower()
  if ques == "yes":
    clear()
  elif ques == "no":
    state = True
  else:
    print("You entered wrong choice, check again")
    

max = 0
for key in data:
  if data[key] > max:
    max = data[key]
    winner = key


print(f"The winner of the bid is {winner} with highest bid of {data[winner]} ")


