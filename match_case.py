import random
# Generating a random number from 1-10
while True:
    secret_number = random.randint(1, 10)
    attempts = 0

# Prompting user to guess a number
    while True:
        guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it? \n"))
        attempts += 1
# Matching user guess
        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations, you guessed it! It took you {attempts} guesses.")
                break
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")
    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
    else:
        print("New game starts!")                