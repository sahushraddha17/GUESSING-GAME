# STEP-1 IMPORT RANDOM WORDS 
import random

# STEP-2 CHOOSE YOUR WORD LIST BASED ON DIFFICULTY LEVEL
easy_words = ['cat', 'dog', 'fish', 'bird', 'tree']
medium_words = ['python', 'jumble', 'garden', 'window', 'bottle']
difficult_words = ['elephant' , 'umbrella' , 'different' , 'computer' , 'astronomy']

# WELOCOME_MESSAGE = "Welcome to the Guessing Game!"
print("Welcome to the Guessing Game!")
print("Choose a difficulty level: easy, medium, difficult")

# STEP-3 CHOOSE YOUR WORD LIST BASED ON DIFFICULTY
level = input('enter the difficulty level:').lower()
if level == "easy":
    word  = random.choice(easy_words)
elif level == "medium":
    word = random.choice(medium_words)
elif level == "difficult":
    word = random.choice(difficult_words)
else:
    print("Invalid level selected. Defaulting to easy.")
    word = random.choice(easy_words)

# STEP-4 TAKING ATTEMPT VARIABLE FOR COUNTING NUMBER OF ATTEMPTS
attempt = 0
print("\nGuess the word!") 

# STEP-5 GAME LOOP FOR GUESSING THE WORD
while True:
    guess = input("enter your guess:").lower()
    attempt += 1

    if guess == word:
        print(f"Congratulation ! you guessed the word{guess} in {attempt}")
        break
   
    hint = ''
   
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
              hint += guess[i]
        else:
            hint += '_'


    print(f"Hint: {hint}")
print("Thanks for playing the Guessing Game!")

    
    
          

        

