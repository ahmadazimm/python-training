import random
import name 
import os


condition = True

def computerchoice():
  if comp_firstcard + comp_secondcard < 18:
    comp_choice = ["yes","no"]
    comp_addcard = random.choice(comp_choice)
    if comp_addcard == "yes":
      comp_card.append(int(random.choice(card))) #adding another card on the list
      print("Computer choose to add card!")

    elif comp_addcard == "no":
      print("Computer choose to not add card!")

def ace ():
  if 1 in mycard:
    ace = input(f"You have an ace, do you want it to be 1 or 11: ")
    if ace == "1":
      print(f"Your cards: {mycard}")
      print("-------------------------------------------")
    elif ace == "11":
      for i in range(len(mycard)-1):
        if mycard[i] == 1:
          mycard[i] = 11
          print(f"Your cards: {mycard}")
          print("-------------------------------------------")

def game():
  if sum(mycard) > 21: #if total value is greater than 21
    print("You busted")
  else:
    computerchoice()
    ace()
    print(f"Computer cards: {comp_card}") 
    print("-------------------------------------------")
    if sum(comp_card) > 21:
        print("Computer busted")
        print("You win!")
    elif sum(comp_card) > sum(mycard):
        print("You lose")
    elif sum(comp_card) < sum(mycard):
        print("You win!")
    else:
        print("It's a tie")
    print("-------------------------------------------")
  print(input("Press enter to continue..."))
  os.system('clear')

while condition:

  print(name.poker)
  card = [1,2,3,4,5,6,7,8,9,10,10,10,10] #because king, queen, jack = 10
  firstcard = int(random.choice(card)) #calling first card
  secondcard = int(random.choice(card))
  
  mycard = [firstcard, secondcard]

  yesno = input ("Do you want to play?: 'y' or 'n'\n") #condition
  if yesno == 'y':
    
    print(f"You cards: {mycard}")
    
    comp_firstcard = int(random.choice(card))
    comp_secondcard = int(random.choice(card))
    
    print (f"Computer first card: {comp_firstcard}") #computer first card
    addcard=input("Do you want to take another card?: ") #add one more card
    print("-------------------------------------------")
      
    comp_card = [comp_firstcard, comp_secondcard] #computer list card
 
    if addcard == "y":
        mycard.append(int(random.choice(card))) #adding another card on the list
        print(f"Your cards: {mycard}")
        game()
        
    else:
        print("You stand")
        game()
    
  elif yesno == 'n':
    print("-------------------------------------------")
    print("Thank you!")
    condition = False
    print(input("Press enter to continue..."))
    os.system('clear')
