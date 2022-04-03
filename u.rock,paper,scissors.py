import random
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r') or (player=='r'and opponent =='l')or (player=='l'and opponent=='sp')or (player=='sp'and opponent=='s')or (player=='s'and opponent=='l')or (player=='sp'and opponent=='r')or(player=='l'and opponent=='p')or(player=='p'and opponent=='sp'):
        return True
counter=0
while True:
    user = input("What's your choice? 'r' for rock, 'p' for paper, 'l' for lizard ,'sp' for spock,'s' for scissors\n. Press q to quit ").lower()
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        print ('It\'s a tie')
    if user=="q":
        print ("your score: "+str(counter))
    if is_win(user,computer):
        counter=counter+1
        print( "Whoo..you won!")
    if is_win(computer,user):
        print( 'Computer won this game:(')
    