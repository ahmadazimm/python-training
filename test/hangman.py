#want the random words
import random
import picture_hang as pic
words = ["ahmad","azim","fikri","syahrul"]
choice = random.choice(words)

#display the blank
display = list("_" * len(choice))
print (pic.logo)

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
    
    #hangman
  if letter not in choice:
    global life
    life -= 1
    global i
    i+= 1
    print(f"You have {life} life left")
    


i=0
#if ever display not get the whole answer  
print (f"{''.join(display)}")

while not endgame:
  game()
  #if player feel in the blanks
  print (f"{''.join(display)}")
  print(pic.hangman[i])
  if "_" not in display:
    endgame = True
    print("YOU WIN")
    #if guess salah

      
  #if hangman complete
  elif life==0:
    
    endgame = True
    print (f"The word is :\n{choice}")
    print ("YOU LOSE")
    
  


#check if the letter is present in the word
#this will insert hangman


