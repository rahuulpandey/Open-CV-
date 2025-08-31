import cv2 as cv 
import sys 

# taking input of image from user
input_image=input("imput an image: ")
#reading the image
image_path=cv.imread(input_image)

if image_path is None:
    print("Error: Image not found")
    sys.exit()

# performing following operation on image
print("""what do you want to do with the image: 
        1 -> Show the normal image
        2 -> Convert to grayscale and show the image 
        3 -> Save the grayscale image 
        4 -> Exit
            """)
if input_image is not None:  
    while True:

        # taking inpput for the operation to be performed 
        choice_var=int(input("Enter your choice for the following: "))


        # if input is 1(Show the normal image)
        if choice_var==1:
        # showing the image
            cv.imshow("Image Window",image_path)
            cv.waitKey(0)
            cv.destroyAllWindows()


        # if inpus is 2(Convert to grayscale and show the image )
        elif choice_var==2:
            # grayscale conversion 
            gray=cv.cvtColor(image_path, cv.COLOR_BGR2GRAY)
            # showing the image
            cv.imshow("Image Window", gray)
            cv.waitKey(0)
            cv.destroyAllWindows()  

        # if input is 3 (i.e. Saving the grayscale image )
        elif choice_var==3:
            print("Please specify the name and format of the image:")
            name=input("name: ")
            format=input("format: ")
            # grayscale conversion 
            gray=cv.cvtColor(image_path, cv.COLOR_BGR2GRAY)
            # saving the image
            cv.imwrite(f"{name}.{format}", gray)
            print(f"{name}.{format} saved successfully!")

        # if input is 4(Exit)
        elif choice_var==4:
            print("exiting the program :)")
            sys.exit()

        else:
            print("Please enter a valid input")

