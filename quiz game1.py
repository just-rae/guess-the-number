from PIL import Image 

image1 =Image.open("pyramids.jfif")
image2=Image.open("imagee.jfif")
print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
while True:
    if playing.lower() != "yes":
        quit()

    print("Okay! Let's start :)")
    score = 0

    answer = input("How many countries are there in Africa? ")
    if answer.lower() == "54":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    image1.show()
    answer = input("where's this located? ")
    if answer.lower() == "giza":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("What is the capital of egypt? ")
    if answer.lower() == "cairo":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("How many states are there in the U.S? ")
    if answer.lower() == "50":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("what's Ireland's nickname? ")
    if answer.lower() == "the emerald isle":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("what's the main ingredient in guacamole? ")
    if answer.lower() == "avocado":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("the world wide web exists on the.. ")
    if answer.lower() == "internet":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("A solar eclipse occurs when the moon moves between Earth and... ")
    if answer.lower() == "the sun":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    answer = input("what does discombobulated mean? ")
    if answer.lower() == "confused":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")

    image2.show()
    answer = input("what's the name of this animal? ")
    if answer.lower() == "chameleon":
        print('Correct!')
        score += 1
    else:
        print("Incorrect!")


    print("You got " + str(score) + " questions correct!")
    print("You got " + str((score / 4) * 100) + "%.")
    replay=input("do u want to replay? ")
    if replay=="yes".lower():
        continue
    else:
        break