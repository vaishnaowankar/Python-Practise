from replit import clear
# this program was coded on replit ,so this module is used to use the clear function below.

def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  from art import logo
  print(logo)

  num1 = float(input("Enter the first number: "))

  for key in operations:
    print(key) 

  state = True
  while state:
    
    operation_symbol = input("Pick an operation: ")

    num2 = float(input("Enter the next number: "))

    calculation = operations[operation_symbol]
    result = calculation(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {result} ")

    ques = input(f"type 'y' to continue calculating with {result} or type 'n' to start new calculation. : ")

    if ques == "y":
      num1 = result
    else:
      state = False
      clear()
      calculator()
    

calculator()