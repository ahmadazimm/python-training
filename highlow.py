import random
import list1 as ls
import os
import name1 as nm
import time

point = 0 
soalan = ls.question
gameover = False


CHOICE = soalan[0] #first choice will const until B is correct


while not gameover: #quiz is the question and answer is the answer
  time.sleep(3)
  os.system('clear')
  print(nm.poker)
  i = random.randint(0 , len(soalan) - 1)
  
  choiceB = soalan[i] #choice B will be random
  if choiceB is CHOICE: #if B is same as CHOICE, need to random again
    choiceB = random.choice(soalan)
  
  print (f"Your point : {point}")
  print("Who has more follower?: ")
 

#description for each choices
  print(f"Option A: {CHOICE['name']} is a {CHOICE['description']} from {CHOICE['country']}")
  print(f"Option B: {choiceB['name']} is a {choiceB['description']} from {choiceB['country']}")

#your guess 
  guess = input("\nA or B\n").lower()
  print(f"your answer is {guess.upper()}")

  if guess == "a":
    if CHOICE['follower'] > choiceB['follower']:
      print("You are right")
      point += 1

    else:
      print("You are wrong")
      print(f"You lose!\nYour point is: {point}")
      gameover = True
      
  elif guess == "b":
    if CHOICE['follower'] < choiceB['follower']:
      print("You are right")
      point += 1
      CHOICE = choiceB #if B is correct, CHOICE const will be choiceB

    else:
      print("You are wrong")
      print(f"You lose!\nYour total point is: {point}")
      gameover = True
