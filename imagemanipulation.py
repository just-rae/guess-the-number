"""this script lets the user choose an image, edit it how they like,and then lets them view their edited picture"""
from PIL import Image, ImageFilter
from PIL import Image, ImageEnhance
import os 
#image sizes to choose from
sizes=[(200,200),(400,400),(600,600)]
#lets user choose picture and breaks out of the loop when user confirms chosen image
while True:
    try:
        user_choice=input("which image would u like to modify?(pic1-pic10)").lower()
        usershow=Image.open(user_choice +".jpg")
        usershow.show()
        user_confirmation=input("Is this the correct image?(yes/no)").lower()
        if user_confirmation=="yes":
            break
      except:
        print("invalid input")

while True:
    choice=input("How would u like to modify ur image(resize,png,black/white,blur,enhance,or rotate) type q to quit ").lower()
     #rotates the user's chosen image and shows changes
    if choice=="rotate":
        #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            rot_num=int(input("Length of rotation?: "))
            image1.rotate(rot_num).save('rotated pics/'+user_choice+'_rotate.jpg')
            image2= Image.open('rotated pics/'+user_choice+'_rotate.jpg')
            image2.show()
        except:
            print("input must be an integer")

        
#resizes user's chosen image and shows changes
    elif choice=="resize":
        #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            choose=int(input("choose 1-3 (size_200='1'/size_400='2'/size_600='3'): "))
            image1.resize(sizes[choose]).save('resized pics/'+user_choice+'_resize.jpg')
            image2= Image.open('resized pics/'+user_choice+'_resize.jpg')
            image2.show()
        except:
            print("you must choose a number between 0 and 4")

    #blurs user's chosen image and shows changes
    elif choice=="blur":
         #try and except statement to prevent potential errors from the user input
        try:
            image1=Image.open(user_choice + ".jpg")
            u_choice=int(input("how much do u want to blur it? "))
            image1.filter(ImageFilter.GaussianBlur(u_choice)).save('blurred pics/'+user_choice+'_blur.jpg')
            image2= Image.open('blurred pics/'+user_choice+'_blur.jpg')
            image2.show()
        except:
            print("input must be an integer")

    #changes picture to b&w and shows changes
    elif choice=="black/white":
        image1=Image.open(user_choice + '.jpg')
        image1.convert(mode='L').save('B&W pics/'+user_choice+'_blackwhite.jpg')
        image2= Image.open('B&W pics/'+user_choice+'_blackwhite.jpg')
        image2.show()

    #changes jpg picture to png and shows it
    elif choice=="png":
        image1=Image.open(user_choice + ".jpg")
        image1.save('PNGs/'+user_choice+'.png')
        image2= Image.open('PNGs/'+user_choice+'.png')
        image2.show()

    #darkens or brightens the picture and shows changes
    elif choice=="enhance":
        try:
            image1=Image.open(user_choice + ".jpg")
            enhancer = ImageEnhance.Brightness(image1) 
            brightness_choice=float(input("how dark or bright do you want it to be?(0.5-dark/1.5-bright)"))
            img_light = enhancer.enhance(brightness_choice) 
            img_light.save('enhanced pics/'+user_choice+'_enhanced.jpg')
            image2= Image.open('enhanced pics/'+user_choice+'_enhanced.jpg')
            image2.show()
        except:
            print("input has to be an integer or a decimal")
    elif choice=="q":
        break

    else:
        print("invalid response.")
      

#lets user view edited images
while True:
    #try and except statement to prevent potential errors from the user inputs
    try:
        foldername=input("type the folder in which the picture is in if you would like to view your edited picture. Type q to quit ").lower()
        if foldername =="q":
            break
        filename=input("type the picture file name. ").lower()
        view_image=Image.open(f'{foldername}/'+filename)
        view_image.show()
    except:
        print('file does not exist or u typed it incorrectly')
