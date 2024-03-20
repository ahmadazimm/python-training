#want the random words
import random
import func as fx
import name as nm
choice = random.choice(nm.animal)

#display the blank
display = list("_" * len(choice))
print (fx.logo)
#choice\
endgame =False 
life =6
#we got 6 life
def game():
  
  
  #input the letter
  letter = input("Enter a letter: ").lower()
  
  #insert the letter inside blank
  for huruf in range(len(choice)):
  
    #if guess betul
    if choice[huruf] == letter:
      display[huruf] = letter
  if letter in display:
    print("You have already guessed this letter")
    #hangman
  if letter not in choice:
    global life
    life -= 1
    global i
    i+= 1
    print(f"You have {life} life left")
    


i=0
#if ever display not get the whole answer  
#this join module is to join the string
print (f"{''.join(display)}")

while not endgame:
  game()
  #if player feel in the blanks
  print (f"{''.join(display)}")
  print(fx.hangman[i])
  if "_" not in display:
    endgame = True
    print(nm.yowin)
    #if guess salah

      
  #if hangman complete
  elif life==0:
    
    endgame = True
    print (f"The word is :\n{choice}")
    print (nm.youlose)
    
  


#check if the letter is present in the word
#this will insert hangman


