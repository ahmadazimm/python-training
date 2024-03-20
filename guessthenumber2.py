import random
CORRECT  = random.randint (1,100)
gameover = False
EASY = 10
HARD = 5
def game(guess, chance): #game function
  global gameover
  if (guess > CORRECT):
    print ("Your guess is too high")
    return chance - 1
  elif (guess < CORRECT)    :
    print ("Your guess is too low")
    return chance - 1
  else:
    print ("You guessed it right! \nYou win!")
    gameover = True
    return chance - 1
   # chance decreases by 1
def display (chance):
  if not gameover:
    if (chance>0):
      print ("Guess again!")
    elif (chance == 0):
      print ("You ran out of chances! \nYou lose!")
      print ("---------------------------------------------")
      
#input function
def guessing():
  print ("---------------------------------------------")
  print (f"You have {chance} chances to guess the number")
  guess =  int(input ("Make a guess: "))
  return guess

def level ():
  print("Welcome to Number Guessing Game!\nI'm thinking of number between 1 and 100")
  difficulty = input ("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  
  if difficulty == "easy":
    return EASY
  elif difficulty == "hard":
    return HARD

#all run here
chance = level()
while (chance>0) and not gameover:
  guess = guessing()
  chance = game(guess, chance)
  display(chance)
print (f"The number is {CORRECT}")
