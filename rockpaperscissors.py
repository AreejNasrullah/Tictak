import random

# We know that r>s , s>p ,p>r
def play():
    user = input("Enter your choice: 'r' for rock, 'p' for paper, 's' for scissors\n")
    user2 = random.choice(['r','p','s'])
    if user == user2:
        return 'It\'s a tie'

    if winner(user, user2):
        return 'You won!'

    return 'You lost!!'


def winner(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())