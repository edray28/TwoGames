import random


def computerChoice(Move):
    if Move == 0:
        return 'rock'
    elif Move == 1:
        return 'paper'
    elif Move == 2:
        return 'scissors'
    else:
        print('Invalid')


# Game Prompt
print('Welcome to the Game of Rock Paper Scissors!')
rounds = int(input('Please select how many rounds: '))


def game(PplayerChoice, PcomputerChoice):
    playerChoice = PplayerChoice.lower()
    if playerChoice == PcomputerChoice:
        print(
            f'You choose: {playerChoice.upper()} | Computer choice: {PcomputerChoice.upper()}', '\nIt is a TIE!')
    elif playerChoice == 'rock' and PcomputerChoice == 'scissors':
        print(
            f'You choose: {playerChoice.upper()} | Computer choice: {PcomputerChoice.upper()}', '\nYou WIN')
    elif playerChoice == 'paper' and PcomputerChoice == 'rock':
        print(
            f'You choose: {playerChoice.upper()} | Computer choice: {PcomputerChoice.upper()}', '\nYou WIN')
    elif playerChoice == 'scissors' and PcomputerChoice == 'paper':
        print(
            f'You choose: {playerChoice.upper()} | Computer choice: {PcomputerChoice.upper()}', '\nYou WIN')
    else:
        print(
            f'You choose: {playerChoice.upper()} | Computer choice: {PcomputerChoice.upper()}', '\nYou LOSE')


for x in range(rounds):
    player = input(
        "\nPlease Select your Choice: 'Rock' | 'Paper' | 'Scissors'\n")
    Move = random.randint(0, 2)
    game(player, computerChoice(Move))
print('THANK YOU FOR PLAYING!!!!')
