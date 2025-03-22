import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    lower_bound = 1
    upper_bound = 100
    secret_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        try:
             guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
             attempts += 1
            
             if guess < lower_bound or guess > upper_bound:
                print("Please choose a number between {lower_bound} and {upper_bound}.")
                             
             if guess < secret_number:
                 print("Too low! Try again!")
                    
             elif guess > secret_number:
                  print("Too high! Try again!")
              
             else:
                 print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                 break
              
             
        except ValueError:
           print("Invalid input. Please enter a valid number.")
            
            
def play_game():
  playing = True
  while playing:
    guess_the_number()
    keep_playing = input('Do you want to keep playing? Press y for yes, n for no: ')
    
    if keep_playing.lower() == 'n':
      playing = False
      print("Thanks for playing!")
      
    
    
    
# Run the game
play_game()