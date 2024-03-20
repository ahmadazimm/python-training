print("             ⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀\n ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀\n ⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄\n⠀⠀⠀⠀ ⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄\n ⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄\n ⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷\n ⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿\n⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃\n ⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇\n⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧\n ⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿\n⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿\n ⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇\n⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃\n ⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇\n ⠀ ⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇\n⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏\n⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀")

print ("Welcome to Among Us.\nYou are the imposter!\nYour mission is to kill or vote out a crewmate (only one).\nGood luck!")
went = input ("You're at the hallway. Where do you want to go?\nType 'left' or 'right'\n")

if went == "left":
  first_step=input ("You walk into a room. There's a vent and a crewmate. What do you want to do?\nType 'vent' to enter the vent. Type 'kill' to kill the crewmate. Type 'stay' if you want to pretent to be a crewmate.\n")
  if first_step == "vent":
    print ("Your crewmate didn't notice you! You run and go to other place.")
    second_step = input ("You can vent out to Weapon or Navigation. Where you want to vent out?\nType 'weapon' or 'navigation'\n")
    if second_step == "navigation":
      print ("You vented out to navigation. Your crewmate saw you and voted you out!!\n\n\n YOU LOSE!")
    else:
      last_step = input ("You vented out to weapon. Your crewmate is busy doing their task.\nKill him? 'yes' or 'no'\n")
      if last_step == "yes":
        print ("You killed your crewmate. You walked out of the room. No one saw you! \n\n\n  YOU WINNNNN!!!!!")
      else:
        print ("You didn't kill your crewmate. You walked out of the room. Suddenly you see a dead crewmate and others think you kill him!\nYou been voted out!\n\n\n  YOU LOSE!")
      
  if first_step == "kill":
    print ("You killed your crewmate. Someone saw you and voted you out!\n\n\n  YOU LOSE!")
  if first_step =="stay":
    second_step = input ("You pretend to be a crewmate. Your crewmate trust you.\nFollow him? 'yes' or 'no'\n")
    if second_step == "yes":
      print ("You followed your crewmate. Your crewmate sus with you and voted you out!\n\n\n  YOU LOSE!\n")
    else:
      print ("You didn't follow your crewmate. Suddenly one of your crewmate use the Emergency Call")
      vote = input ("You can vote out your crewmate. You, blue and green were being the most sus. Who do you want to vote? You RED btw!\nType 'red', 'blue', 'green'\n")
      if vote == "red":
        print ("You voted out yourself. Your crewmate voted you out!\n\n\n  YOU LOSE!")
      elif vote == "blue":
        print ("You voted out blue. Your crewmate voted you out!\n\n\n  YOU LOSE!")
      else:
        print ("You voted out green. Your crewmates also vote green!\n\n\n  YOU WINNNNN!!!!!")

else:
  went = input ("You walk into a room. There's a vent and a crewmate. What do you want to do?\nType 'vent' to enter the vent. Type 'kill' to kill the crewmate.\n")
  if went == "vent":
    print ("Your crewmate notice you and vote you out!\n\n\n YOU LOSE!")
  else:
    print ("You killed your crewmate. Someone saw you and voted you out!\n\n\n  YOU LOSE!")
