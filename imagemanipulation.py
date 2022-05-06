from PIL import Image, ImageFilter
from PIL import Image, ImageEnhance
import os 

while True:
    user_choice=input("which image would u like to modify?(pic1-pic10)")
    usershow=Image.open(user_choice +".jpg")
    usershow.show()
    user_confirmation=input("Is this the correct image?(yes/no)")
    if user_confirmation=="yes":
        break

choice=input("How would u like to modify ur image(resize,png,black/white,blur,enhance,or rotate)")
while True:

    if choice=="rotate":
        image1=Image.open(user_choice + ".jpg")
        rot_num=int(input("Length of rotation?: "))
        image1.rotate(rot_num).save(user_choice+'_rotate.jpg')
    
    

    elif choice=="resize":
        image1=Image.open(user_choice + ".jpg")
        choose=int(input("choose the picture size: "))
        image1.resize(choose).save(user_choice+'_resize.jpg')
        
           
    elif choice=="blur":
        image1=Image.open(user_choice + ".jpg")
        u_choice=int(input("how much do u want to blur it? "))
        image1.filter(ImageFilter.GaussianBlur(u_choice)).save(user_choice+'_blur.jpg')


    elif choice=="black/white":
        image1=Image.open(user_choice + '.jpg').convert(mode='L')
        image1.save(user_choice+'_black/white.jpg')
    
    elif choice=="png":
        image1=Image.open(user_choice + ".jpg")
        image1.save(user_choice+'.Png')


    elif choice=="enhance":
        image1=Image.open(user_choice + ".jpg")
        enhancer = ImageEnhance.Brightness(image1) 
        brightness_choice=float(input("how dark or bright do you want it to be?(0.5-dark/1.5-bright)"))
        img_light = enhancer.enhance(brightness_choice) 
        img_light.save(user_choice+'_enhanced.jpg')

    else:
        print("invalid response.")
        break

    multi_changes=input("would u like to create more changes? Type a random character to quit")
    if multi_changes=="yes":
        choice=input("How would u like to modify ur image(resize,png,black/white,blur,enhance,or rotate)")
    else:
        break

while True:
    try:
        view=input("type the picture folder name if you would like to view your edited picture. Type a random character to quit.")
        view_image=Image.open(view)
        view_image.show()
    except:
        print('file does not exist or u typed it incorrectly')
        break
    
