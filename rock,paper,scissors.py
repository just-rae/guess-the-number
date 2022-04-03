import random
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r') or (player=='r'and opponent =='l')or (player=='l'and opponent=='sp')or (player=='sp'and opponent=='s')or (player=='s'and opponent=='l')or (player=='sp'and opponent=='r')or(player=='l'and opponent=='p')or(player=='p'and opponent=='sp'):
        return True
def play():
    counter=0
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 'l' for lizard ,'sp' for spock,'s' for scissors\n. Press q to quit ").lower()
        computer = random.choice(['r', 'p', 's'])
        if user == computer:
            return 'It\'s a tie'
        if is_win(user, computer):
            return "Whoo..you won! Number of games won:"+counter+=1
        if user=="q":
            return counter
        if is_win(computer,user):
            return 'You lost this game:('
choice=input("Type yes if u wanna play rock paper scissors lizard spock or type q to quit. ").lower()
while True:
    if choice=="yes":
        print(play())
    elif choice=="q":
        break 
    else:
        print("Response is invalid.")
    