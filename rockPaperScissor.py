import random
def computer():
    obj = ['rock','paper','scissor']
    ran = random.choice(obj)
    return ran


while True:
    player_obj = input("Choose between rock, paper or scissor: ")
    print(computer())
    if player_obj == 'rock' and computer() == 'paper':
        print("computer won")
    elif player_obj == 'rock' and computer() == 'scissor':
        print("Player won")
    elif player_obj == 'paper' and computer() == 'scissor':
        print("computer won")
    elif player_obj == 'paper' and computer() == 'rock':
        print("Player won")
    elif player_obj == 'scissor' and computer() == 'paper':
        print("Player won")
    elif player_obj == 'scissor' and computer() == 'rock':
        print("computer won")
    else:
        print("It's a tie!!!")



print(computer())