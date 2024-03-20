import calculator as clt
import time
import os

# result =0
condition = True
def calculator(f_num): #function for calculation operation
  result=0
  operation =""

  #calculation
  print ("+\n-\n*\n/\n")
  operation = input ("Pick an operation: ") #insert operation
  s_num = float(input("What's the next number?: ")) #insert number
  #operation
  if (operation=="+"):
    result = f_num + s_num #sum

  elif (operation=="-"):
    result = f_num - s_num #minus

  elif (operation=="*"):
    result = f_num * s_num #multiply

  elif (operation=="/"):
    result = f_num / s_num #divide

  else:
    print("The operation is invalid")

  #print
  print(f_num, operation, s_num, "=", result)
  return result

def ulang (new_num): #for yes option
  new_answer=calculator(new_num) #use previous result as a first number 
  return new_answer


def yesno (jawapan):
  #input
  print (f"Type 'y' if you want to continue calculating with {jawapan}?")
  pilihan = input("Type 'n' to start a new calculation. Type 'q' to quit: ")
  print("------------------------------\n")
  option = pilihan  
  
  
  # option=yesno(jawapan=answer)
  if (option=='n'): #if no, new f_num
    print("------------------------------\n")
    return True

  elif (option=='y'): #f_num=result
    print (f"{answer} will be used as the first number\n")
    print("------------------------------\n")
    while (option=='y'):
      
      yesno(calculator(ulang(answer))) # to repeat the calculation process
    

  elif (option=='q'):
    print("------------------------------\nExit the calculator")

    for i in range(0,5):
      print(5-i)
      time.sleep(0.8)    # Pause 3 seconds
    print("Thank you!")
    return False 
  else:
    print ('Invalid Option')
    return False


while condition:
  os.system('clear')
  print(clt.pic)
  answer = calculator(f_num=float(input("What's the first number?: ")))
  if not yesno(jawapan=answer):
    condition=False

  else:
    condition = True
    

