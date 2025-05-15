import random

def getUserChoice():
    print('\n----------------- Rock Paper Scissors -----------------')
    choice = input("Enter your Choice (Rock, Paper or Scissors):- ").lower()
    print("-------------------------------------------------------\n")

    while choice not in ['rock', 'paper', 'scissors']:
        print('Invalid Choice')
        choice = input("Enter your Choice (Rock, Paper or Scissors):- ").lower()
        print('-------------------------------------')

    return choice

def getComputerChoice():
    return random.choice(['rock', 'paper', 'scissors'])

def winner(user,computer):
    if user == computer:
        return 'tie'
    elif user == 'rock' and computer == 'scissors':
        return 'user'
    elif user == 'paper' and computer == 'rock':
        return 'user'
    elif user == 'scissors' and computer == 'paper':
        return 'user'
    else:
        return 'computer'

def play():
    userScore = 0
    computerScore = 0

    while True:
        userChoice = getUserChoice()
        computerChoice = getComputerChoice()

        print(f"Your Choice: {userChoice}\n"
              f"Computer Choice: {computerChoice}\n")
        res = winner(userChoice, computerChoice)
        if res == 'tie':
            print("Tie Match !!")
        elif res == 'user':
            print("You Win !!")
            userScore += 1
        else:
            print("Computer Win !!")
            computerScore += 1

        print(f"\nCurrent Score :-\n"
              f"Your Score : {userScore}\n"
              f"Computer Score : {computerScore}\n")

        play_again = input("Do you want to play again? (y/n) ").lower()

        if play_again != 'y':
            break

    print("Bye, Thank you for Playing")


play()