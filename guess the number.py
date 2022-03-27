


import random 

def guess(r):
    random_number= random.randint(1,r)
    guess=0
    while guess!=random_number:
        guess=int(input("guess a number"))
        if guess<random_number:
            print("guess again. too low.")
        elif guess>random_number:
            print("guess again.Too high.")
    print ("You are correct!")


def computer_guess(a):
    low=1
    high=a 
    feedback=""
    while feedback!="c":
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f'is {guess} too high(h) or too low(l) or correct(c)?').lower()
        if feedback=="h":
            high=guess-1
        elif feedback=="l":
            low=guess+1
    print("the computer guessed ur number!")
while True:
    choose_game=input("which game would you like to play?enter user guess,computer guess,or q to quit")
    if choose_game=="user guess":
        guess(10)
    elif choose_game=="computer guess":
        computer_guess(40)
    elif choose_game=="q":
        break
    else:
        print("input is incorrect. choose again.")





