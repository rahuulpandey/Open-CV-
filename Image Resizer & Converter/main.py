'''Loads an image. 

Resizes it to a new width and height.

Converts it to grayscale and HSV.
'''

import cv2
import sys


#taking image input 
input_img=input("enter image name: ")
#reading image
orig_image=cv2.imread(input_img)




while True:

    choice_input=int(input("choose what you want to do with the image:\n" \
    "1- Resize it to new w,h\n" \
    "2- convert the color of image(hsv,gray etc.)\n" \
    "3- exit the program\n" \
    "Enter Your Choice: "))


    if choice_input == 1:    #Resize it to new w,h
        w= int(input("enter the width you want: "))
        h= int(input("enter the height you want: "))
        resize_image=cv2.resize(orig_image, (w, h))
        cv2.imshow("Resized Image", resize_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



    elif choice_input == 2:    #convert the color of image(hsv,gray etc.)

        type_input=int(input("choose a type in which you want to convert your image:\n" \
        "1- grayscale\n" \
        "2- hsv\n" \
        "3- BGR --> RGB\n"
        "Enter Your Choice: "))

        if type_input == 1:
            converted_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)

        elif type_input == 2:
            converted_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2HSV)

        elif type_input == 3:
            converted_image = cv2.cvtColor(orig_image, cv2.COLOR_BGR2RGB)

        else:
            print("enter a valid input")
            break
        cv2.imshow("Converted Image", converted_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    elif choice_input == 3:    #exiting the program
        print("exiting the program.")
        sys.exit()


    else:
        print("please choose correct input!!")




    



