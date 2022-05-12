"""this script lets the user choose an image, edit it how they like,and then lets them view their edited picture"""
from PIL import Image, ImageFilter
from PIL import Image, ImageEnhance
import os 
#image sizes to choose from
sizes=[(200,200),(400,400),(600,600)]
#lets user choose picture and breaks when user confirms chosen image
while True:
    user_choice=input("which image would u like to modify?(pic1-pic10)").lower()
    usershow=Image.open(user_choice +".jpg")
    usershow.show()
    user_confirmation=input("Is this the correct image?(yes/no)").lower()
    if user_confirmation=="yes":
        break
while True:
    choice=input("How would u like to modify ur image(resize,png,black/white,blur,enhance,or rotate) type random character to quit" ).lower()
    #rotates the user's chosen image and shows changes
    if choice=="rotate":
        #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            rot_num=int(input("Length of rotation?: "))
            image1.rotate(rot_num).save(user_choice+'_rotate.jpg')
            image2= Image.open(user_choice+'_rotate.jpg')
            image2.show()
        except:
            print("input must be an integer")


    #resizes user's chosen image and shows changes
    elif choice=="resize":
        #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            choose=int(input("choose 1-3 (size_200='1'/size_400='2'/size_600='3'): "))
            image1.resize(sizes[choose]).save(user_choice+'_resize.jpg')
            image2= Image.open(user_choice+'_resize.jpg')
            image2.show()
        except:
            print("you must choose a number between 0 and 4")

     #blurs user's chosen image and shows changes        
    elif choice=="blur":
        #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            u_choice=int(input("how much do u want to blur it? "))
            image1.filter(ImageFilter.GaussianBlur(u_choice)).save(user_choice+'_blur.jpg')
            image2= Image.open(user_choice+'_blur.jpg')
            image2.show()
        except:
            print("input must be an integer")
            
    #changes picture to b&w and shows changes
    elif choice=="black/white":
        image1=Image.open(user_choice + '.jpg')
        image1.convert(mode='L').save(user_choice+'_blackwhite.jpg')
        image2= Image.open(user_choice+'_blackwhite.jpg')
        image2.show()
        
    #changes jpg picture to png and shows it
    elif choice=="png":
        image1=Image.open(user_choice + ".jpg")
        image1.save(user_choice+'.Png')
        image2= Image.open(user_choice+'.png')
        image2.show()

    #darkens or brightens the picture and shows changes
    elif choice=="enhance":
        #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            enhancer = ImageEnhance.Brightness(image1) 
            brightness_choice=float(input("how dark or bright do you want it to be?(0.5-dark/1.5-bright)"))
            img_light = enhancer.enhance(brightness_choice) 
            img_light.save(user_choice+'_enhanced.jpg')
            image2= Image.open(user_choice+'_enhanced.jpg')
            image2.show()
        except:
            print("input must be an integer or a decimal")

    else:
        print("invalid response.")
        break

#lets user view edited images
while True:
    try:
        view=input("type the picture folder name if you would like to view your edited picture. Type a random character to quit.")
        view_image=Image.open(view)
        view_image.show()
    except:
        print('file does not exist or u typed it incorrectly')
        break
