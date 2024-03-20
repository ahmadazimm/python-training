import random
import lukisan as lk

#What your choice?
choice = int(input ("What your choice?\nrock = 0, paper = 1, scissor = 2\n"))
#hand = ["rock", "paper", "scissor"]
#you = hand[choice]
display = [lk.rock, lk.paper, lk.scissor]
you = display[choice]
#your choice
print (f"You choose: {you}")
#image display
#mydisplay = [lk.rock, lk.paper, lk.scissor]
#print(display[choice])

#Computer's choice
comp = display[random.randint(0,2)]
#computer's choice
print (f"Computer choose: {comp}\n")
#image display
#comdisplay = [lk.rock, lk.paper, lk.scissor]
#print(comdisplay[random.randint(0,2)])



if you == comp:
  print ("Draw")
elif you == "rock" and comp == "scissor":
  print ("You win")
elif you == "paper" and comp == "rock":
  print ("You win")
elif you == "scissor" and comp == "paper":
  print ("You win")
else:
  print ("You lose")
