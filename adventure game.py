from PIL import Image
#images
image1= Image.open("garden.jpg")
image2=Image.open("forest.jpg")
image3=Image.open("hill.jpg")
image4=Image.open("waterfall.jpg")
#asks for users name and greets them
def get_name():
    while True:
        name = input("Type your name: ")
        if name.isalpha():
            print("Hello",name," Welcome to this adventure!")
            return True
        else: 
            print("Response is invalid. please try again")

get_name()

answer = input("where do you want to start your adventure?(secret garden/abandoned forest) ").lower()

if answer == "secret garden":
    image1.show()
    answer = input("You come to a waterfall, you can walk around it or swim accross?(walk/swim) ").lower()
    image4.show()
    if answer == "swim":
        answer=input("You see two paths. path one looks dangerous and damaged and two looks crowded. choose your path.(one/two) ").lower()
        if answer == "one":
            answer=input("You take five steps and see a lion sleeping next to a tree. Do you continue walking or go back? ").lower()
            if answer=="continue":
                print("you accidenatly wake up the lion and it eats you alive. you lose. ")
            elif answer=="go back":
                print("you were lost and couldn't go back. you lose.")
            else:
                print('Not a valid option. You lose.')
        if answer == "two":
            print("you get killed by a speeding car and lose.")
        else:
            print('Not a valid option. You lose.')
    if answer== "walk":
        answer=input("you come to a boat. Do you take the boat and try to escape?(yes/no) ").lower()
        if answer=="yes":
            answer=input("you take the boat and after two hours of rowing the boat,you see an island. Do you head towards it?(yes/no) ").lower()
            if answer=="yes":
                answer=input("you land on the island and find a crashed airplane, food,and a flare gun. Do you take the stuff?(yes/no) ").lower()
                if answer=="yes":
                    print("you see a big ship sailing and you use the flare gun.The people on the ship see and help you go back home. you WIN!")
                elif answer=="no":
                    print("you die of starvation. You lose.")
            elif answer=="no":
                print(" big wave hits you and you drown. you lose")
            else:
                print('Not a valid option. You lose.')
        elif answer=="no":
            print("you dont know where to go and die of starvation. you lose")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

elif answer == "abandoned forest":
    image2.show()
    answer = input("You come to a little hill. do you want to climb it or head back (climb/back)? ").lower()
    image3.show()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "climb":
        answer = input("You climb the hill and see an abandoned airplane. Do you go explore it (yes/no)? ").lower()

        if answer == "yes":
            answer=input("it looks like it could work. do you want to try to fly it?(yes/no) ").lower()
            if answer=="yes":
                print("it works. you go back to your home and WIN!")
            else:
                print('Not a valid option. You lose.')
        elif answer == "no":
            print("you're lost and have no other options. you die of starvation.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("You did a good job! Thank u for trying")