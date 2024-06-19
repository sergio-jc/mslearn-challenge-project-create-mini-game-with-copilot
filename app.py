import random

# import required libraries
# write 'hello world' to the console
print('hello world')

OPTIONS = ['rock', 'paper', 'scissors']

def get_user_choice():
    user_choice = input('Please choose rock, paper, or scissors: ')
    while user_choice not in OPTIONS:
        print('Invalid choice. Please choose rock, paper, or scissors.')
        user_choice = input('Please choose rock, paper, or scissors: ')
    return user_choice

def get_computer_choice():
    return random.choice(OPTIONS)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'
    
def play_game():
    games_played = 0  # Variable para realizar un seguimiento del número de juegos jugados
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        print(f'You chose {user_choice}. The computer chose {computer_choice}.')
        if winner == 'tie':
            print('It\'s a tie!')
        else:
            print(f'The winner is {winner}!')
        games_played += 1  # Incrementar el número de juegos jugados
        # Give the user the option to play again
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again != 'yes':
            break
    print(f'Number of games played: {games_played}')  # Mostrar el número de juegos jugados
    print('Thanks for playing!')
    
if __name__ == '__main__':
    play_game()
