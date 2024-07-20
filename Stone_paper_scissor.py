import random
options=['r','p','s']
def game(user_choice):
    while True:
        if user_choice == 1:
            choice_name = "Rock"
        elif user_choice == 2:
            choice_name = "Paper"
        elif user_choice == 3:
            choice_name = "Scissor"
        print("User chose:", choice_name)
        print("Now it's computer's turn!")
        comp_choice = random.choice(options)
        if comp_choice=='s':
            comp_choice_name = 'Scissor'
        elif comp_choice=='r':
            comp_choice_name = 'Rock'
        elif comp_choice == 'p':
            comp_choice_name = 'Paper'
        print("Computer chose:", comp_choice_name)
        print("It's", choice_name, 'v/s', comp_choice_name)
        if comp_choice_name == 'Scissor' and choice_name == 'Paper':
            print("Computer wins!")
        elif comp_choice_name == 'Rock' and choice_name == 'Scissor':
            print("Computer wins!")
        elif comp_choice_name == 'Scissor' and choice_name == 'Rock':
            print("You win!")
        elif comp_choice_name == 'Rock' and choice_name == 'Paper':
            print("You win!")
        elif comp_choice_name == 'Paper' and choice_name == 'Rock':
            print("Computer wins!")
        elif comp_choice_name == 'Paper' and choice_name == 'Scissor':
            print("You win!")
        elif comp_choice_name == choice_name:
            print("It's a draw!")
        reply = input("Do you want to play again? (Y/N):")
        if reply == 'Y':
            user_input = int(input("Enter 1:Rock , 2:Paper, 3:Scissor:-"))
            while user_input > 3 or user_input < 1:
                user_input = int(input('Enter a valid choice please:'))
            game(user_input)
        elif reply == 'N':
            exit()

user_input = int(input("Enter 1:Rock , 2:Paper, 3:Scissor:-"))
while user_input > 3 or user_input < 1:
    user_input = int(input('Enter a valid choice please: '))
game(user_input)
