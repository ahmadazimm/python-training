print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
true = 0
love = 0
name = name1 +name2
for x in name:
  if name == "T" or "t":
    true+=1
  if name == "R" or "r":
    true+=1
  if name == "U" or "u":
    true+=1
  if name == "E" or "e":
    true+=1
print (true)
