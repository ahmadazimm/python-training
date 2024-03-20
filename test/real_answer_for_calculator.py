import calculator as clt
import os

#make a function for each operation
def add(n1, n2):
  return n1 + n2
    
def substract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2



operation = { # Dictionary with all the operations
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}


def calculator():
  os.system('clear')
  print(clt.pic)
# input
  num1= int(input("Whats the first number?: "))
  condition = True
  while (condition):
  
    for i in operation:
      print(i)
    
    #start calculate
    operation_sign = input("Whats the operation?: ")
    num2= int(input("Whats the next number?: "))
    calculation_function = operation [operation_sign] #name of the operation dict
    answer = calculation_function(num1, num2)
  
    print (f"{num1} {operation_sign} {num2} = {answer}")
  
    #for condition
    yesno = input(f"Press 'y' to calculate use the {answer}. Press 'n' to use a new number. Press 'q' to quit.\n").lower()
    
    if (yesno == "y"):
      num1 = answer
      continue
       
    elif (yesno == "n"):
      calculator()
  
    elif(yesno=='q'):
      print("THANK YOU")
      condition = False


calculator()
