
#function for encoding
def caesar(words,shift):

  #new word
  new_word= ""
  if code =="decode":
    shift = -shift 

  for i in words: #to check each letter of the words position
    if i in alphabet: #if the word has letter
      position = alphabet.index(i)
      new_position = position + shift #add the shifted position to create a new encode word
      if new_position<len(alphabet):
        new_word += alphabet[new_position] #encode word
      elif new_position > len(alphabet): #if letter is out of alphabet list
        new_position -= len(alphabet)
        new_word += alphabet[new_position]
      
    else:
      new_word += i
  
  print(f"\nYour {code} message is:\n{new_word}")  #your encode word

#loop to continue the process 
condition=True
while condition:
  #print input
  print ('--------------------------------------------------------')
  code= input ("Type 'encode' to encrypt. type 'decode' to decrypt:\n").lower()
  print ('--------------------------------------------------------')
  alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  in_sentence= input("\nType your message:\n").lower()
  in_shift = int(input("Type the shift number:\n"))
  
  caesar(words=in_sentence, shift=in_shift) #caesar function 
  
  #continue the progam
  nak_lagi=input("\nType 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  
  if nak_lagi == "yes":
    condition = True
  elif nak_lagi == "no":
    condition = False
  else:
    print ("You type the wrong input")
    condition = False

#exit 
print ('--------------------------------------------------------')
print ("Thank you for using this service")

