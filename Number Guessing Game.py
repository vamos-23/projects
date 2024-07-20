import random
def game_algo(lower,upper):
    comp_choice = random.randint(lower, upper)
    rounds = 0
    while True:
        guess = int(input("Enter your guess:"))
        rounds += 1
        if (guess == comp_choice):
             print("You guessed it right!")
             break
        elif(guess > comp_choice):
             print("You guessed too high....Take a smaller guess.")
        elif(guess < comp_choice):
             print("You guessed too low....Take a bigger guess.")
    print(f"You took {rounds} rounds to guess the number")
    print("-----GAME OVER-----")
    user_reply=input("Do you want to play again? (Y/N):")
    if user_reply == 'Y':
       lower_bound = int(input("Enter lower bound:"))
       upper_bound = int(input("Enter upper bound:"))
       game_algo(lower_bound, upper_bound)
    elif user_reply == 'N':
       exit()

lower_bound = int(input("Enter lower bound:"))
upper_bound = int(input("Enter upper bound:"))
game_algo(lower_bound, upper_bound)





