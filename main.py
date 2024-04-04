import random

#### FUNCTIONS ####
'''
Randomly selects a secret word from a bank of over 50,000 words. Returns the secret word.
'''
def pick_word():
	wordbank = open("word_bank.txt","r") #opens text file for reading
	words = wordbank.read() #stores contents of txt file in variable
	words = words.split() #place words into a list.
	return random.choice(words)

'''
Takes in the number of incorrect guesses as an argument and prints the approptiate hangman status.
'''
def print_body(num_inc):
	if num_inc ==0:
		print("_______")
		print("|")
		print("|")
		print("|")
		print("|")
		print("|")
	elif num_inc == 1:
		print("_______")
		print("|     0")
		print("|")
		print("|")
		print("|")
		print("|")
	elif num_inc ==2:
		print("_______")
		print("|     0")
		print("|     |")
		print("|")
		print("|")
		print("|")
	elif num_inc ==3:
		print("_______")
		print("|     0")
		print("|    /|")
		print("|")
		print("|")
		print("|")
	elif num_inc ==4:
		print("_______")
		print("|     0")
		print("|    /|\\")
		print("|")
		print("|")
		print("|")
	elif num_inc ==5:
		print("_______")
		print("|     0")
		print("|    /|\\")
		print("|    / ")
		print("|")
		print("|")
	elif num_inc ==6:
		print("_______")
		print("|     0")
		print("|    /|\\")
		print("|    / \\")
		print("|")
		print("|")








		
#### GAME #####
# Select secret word
secret_word = pick_word()
# Create dashes list
def starting_dashes(secret_word):
  sec_word_dashes = []
  for i in range(len(secret_word)):
    sec_word_dashes.append("_")
  return sec_word_dashes
dashes = starting_dashes(secret_word)
def intro():
  print("This is your word:")
  print()
  print(dashes)
  print()
  print("And here's Billy. Billy is going to be hung if you can't get a correct guess of the secret word in six tries. You don't want Billy to die, do you?")
  print("         _____________________________________")
  print("        |Please help me I don't want to die :(|")
  print("        | ------------------------------------")
  print("        |/")
  print("_______")
  print("|     0")
  print("|    /|\\")
  print("|    / \\")
  print("|")
  print("|")
  print()
  print("3... 2.. 1. START!")
  print()
num_inc = 0
num_left = 6
guessed = []

def display_dashes(dashes):
    print("".join(dashes))
  
def replace_dashes(dashes, secret_word, guess):
  for i in range(len(secret_word)):
    if secret_word[i] == guess:
      dashes[i] = guess
  return dashes
# Create list of previous guess


#Create a variable that store the number of incorrect guesses

def check_guess(dashes, secret_word, guess, guessed, num_inc):
  if guess in guessed:
    print()
    print("ERROR: GUESS HAS ALREADY BEEN MADE")
    print()
    print(guessed)
    print()
    display_dashes(dashes)
    print()
  else:
    guessed.append(guess)
    if len(guess) > 1:
      if guess == secret_word:
        dashes = replace_dashes(dashes, secret_word, guess)
      else:
        num_inc += 1
        print_body(num_inc)
    else:
      for i in range(len(secret_word)):
        if secret_word[i] == guess:
          dashes = replace_dashes(dashes, secret_word, guess)
      if guess not in dashes:
        num_inc += 1
  return dashes, guessed, num_inc
        
    
##### GAME LOOP #### 
# while loop that runs as long as the number of incorrect guess is less than 6 and there are "_" in the dashes list
# while num < 6 and "-" in dashes:

intro()
while num_inc < 6 and "_" in dashes:
  print("Status of hangman:")
  print()
  print_body(num_inc)
  print()
  print("Secret word progress:")
  display_dashes(dashes)
  print()
  print("Number of incorrect guesses (you are only allowed 6):" , num_inc)
  print()
  guess = input("What do you guess is in the word?: ")
  dashes, guessed, num_inc = check_guess(dashes, secret_word, guess, guessed, num_inc)

if num_inc == 6:
  print()
  print("Oh no! You used up all of your guesses and couldn't save Billy in time! SHAME ON YOU!!!")
  print()
  print("         _____________________________________")
  print("        |GaAGh GURgle glurrrr.... (×_×)       |")
  print("        | ------------------------------------")
  print("        |/")
  print("_______")
  print("|     0")
  print("|    /|\\")
  print("|    / \\")
  print("|")
  print("|")
  print()
  print("The secret word was:" , secret_word)

if "_" not in dashes:
  print()
  print("Hurray! You guessed the word correctly in time, and you saved Billy! Good job you!")
  print()
  print("         _____________________________________")
  print("        |Thank you for saving me :D           |")
  print("        | ------------------------------------")
  print("        |/")
  print("_")
  print("|     0")
  print("|    /|\\")
  print("|    / \\")
  print("|")
  print("|")
  print()
  print("The secret word was:" , secret_word)
  # replace_dashes(dashes, secret_word, guess)
  
	# Display gallows

	# Display dashes

	# Ask player for guess and process guess

# Print a message - If the player wins, write a congratualtory message, otherwise let the know they lost and print the secret word.