import random
CORRECT  = random.randint (1,100)
gameover = False

def game(): #game function
  global chance
  global gameover

  print ("---------------------------------------------")
  print (f"You have {chance} chances to guess the number")
  guess =  int(input ("Make a guess: "))

  if (guess > CORRECT):
    print ("Your guess is too high")

  elif (guess < CORRECT)    :
    print ("Your guess is too low")

  else:
    print ("You guessed it right! \nYou win!")
    gameover = True

  chance -=1 # chance decreases by 1

  if not gameover:
    if (chance>0):
      print ("Guess again!")
    elif (chance == 0):
      print ("You ran out of chances! \nYou lose!")
      print ("---------------------------------------------")
#main function
def level():
  print("Welcome to Number Guessing Game!\nI'm thinking of number between 1 and 100")
  difficulty = input ("Choose a difficulty. Type 'easy' or 'hard': ").lower()

  if difficulty == "easy":
    chance = 10
  elif difficulty == "hard":
    chance = 5

level()
while chance>0 and not gameover:
  game()
  
print (f"The number is {CORRECT}")
