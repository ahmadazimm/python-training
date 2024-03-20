import os

print ("Welcome to the secret BID game!\n")
condition =True
bidder = {}
press=input("Please enter 'S' to start the game.\n").upper()
if press == "S":
  os.system('clear') #clear screen
  
  while condition: #condition if still have bidder
    name = input("What is your name?\n") #inser input
    bid = int(input("What your bid?\n$"))
    yesno = input ("Are ther any other bidder? 'yes' or 'no'\n")

    bidder[name] = bid
    
    if yesno == 'no': #to break the loop
      os.system('clear')
      print("Thank you for joining us!\n")
      condition = False
      highest=0
      winner=""
    
    # to check the highest
      for bidname in bidder:
          if bidder[bidname] > highest:
              highest = bidder[bidname]
              winner = bidname
      print ("The winner is: " + winner)
      print (f"with bid of ${highest}\n")
      
      
      
     
    
    elif yesno =='yes':
      os.system('clear') 
      continue
    else:
      print ("Input is not valid")
      break
else:
  print ("Input is not valid")
  
#   for names in bidder:#to go through each bid
