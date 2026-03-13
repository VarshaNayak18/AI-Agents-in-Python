# Learning Agent - Program keeps running until the user has the 3 right guesses

score = 0

while score < 3:
    guess = int(input("Guess number between 1-5: "))
    
    if guess == 3:
        print("Correct!")
        score += 1
    else:
        print("Try again")