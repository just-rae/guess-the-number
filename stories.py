
def story1():
    adj=input("adjective: ")
    adj2=input("adjective: ")
    verb1=input("verb: ")
    verb2=input("verb: ")
    madlib=f"learning python is {adj}! I {verb1} it because it is {adj2}!" 
    print(madlib)
def story2():
    verbing=input("verb ending in ing: ")
    place=input("place: ")
    noun=input("noun: ")
    noun2=input("noun: ")
    number=input("number: ")
    plural_nouns=input("plural noun: ")
    adj=input("adjective: ")
    madlib=f"{verbing} is my favorite thing to do on weekends. My {noun} and I like to go to {place}. Last time we went, we saw {number}{noun2} on the {plural_nouns}.It was {adj}!"
    print(madlib)
def story3():
    number=input("number: ")
    noun=input("noun: ")
    verbing=input("verb ending in ing: ")
    noun2=input("noun: ")
    madlib=f"recent study reveals more than {number} of greenhouse gas emissions is caused by {noun}. These gas emissions cause {noun2} and will destroy our planet if left unaddressed. Some solutions might inlcude {verbing} ecofriendly products instead of plastic. "
    print(madlib)
while True:
    choose=input("which story would u like to play?(story1,story2,or story3).Press q to quit ").lower()
    if choose=="story1":
        story1()
    elif choose=="story2":
        story2()
    elif choose=="story3":
        story3()
    elif choose=="q":
        break
    else:
        print("Response is invalid. Please try again.")