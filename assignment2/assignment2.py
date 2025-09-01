# Importing necessary library
import cv2 as cv
import sys
user=input("Enter Username: ")

# taking input of image from user
input_image=input("imput an image: ")
#reading the image
orig_image=cv.imread(input_image)


if orig_image is None:
        print("Error: No image found" \
        "Exiting!")
        sys.exit()


while True:

        # Taking user input for which operation he want to perform 
    print(f"""\nWhat do you want to do {user} ?
        1. Draw a Line?
        2. Draw a Circle?
        3. Draw a Rectangle?
        4. Add some text?
        5. Exit
        """)

    options = {
    1: "Draw a Line",
    2: "Draw a Circle",
    3: "Draw a Rectangle",
    4: "Input Text",
    5: "Exit"}

    # checking the input
    try:
        user_input=int(input("Enter Your Choice: "))
        if user_input not in range (1,6):
            print("Enter valid option")
        else:
            print(f"You selected: {user_input} ({options[user_input]})")

    except ValueError:
        print("Please enter a integer value")

    # main operation on the image
    if orig_image is not None:

        # draw a line 
        if user_input==1:
            try:
                x1, y1 = map(int, input("Enter x,y for point1: ").split(','))
                x2, y2 = map(int, input("Enter x,y for point2: ").split(','))
                b,g,r = map(int, input("Enter the color value of BGR():  ").split(','))
                thickness=int(input("Enter the thickness: "))
                cv.line(orig_image,(x1,y1),(x2, y2),(b,g,r),thickness)
                cv.imshow("Edited Image",orig_image)
                cv.waitKey(0)
                cv.destroyAllWindows()
            except:
                print("Invalid input! Please enter values properly.")


        # draw a circle
        elif user_input==2:
            try:
                cx, cy = map(int, input("Enter x,y for center: ").split(','))
                radius=int(input("Enter the radius of circle: "))
                b,g,r = map(int, input("Enter the color value of BGR():  ").split(','))
                thickness=int(input("Enter the thickness: "))
                cv.circle(orig_image,(cx,cy),radius,(b,g,r),thickness)
                cv.imshow("Edited Image",orig_image)
                cv.waitKey(0)
                cv.destroyAllWindows()                

            except:
                print("Invalid input! Please enter values properly.")


        # draw a rectangle
        elif user_input==3:
            try:
                x1, y1 = map(int, input("Enter x,y for point1: ").split(','))
                x2, y2 = map(int, input("Enter x,y for point2: ").split(','))
                b,g,r = map(int, input("Enter the color value of BGR():  ").split(','))
                thickness=int(input("Enter the thickness: "))
                cv.rectangle(orig_image,(x1, y1),(x2, y2),(b,g,r),thickness)
                cv.imshow("Edited Image",orig_image)
                cv.waitKey(0)
                cv.destroyAllWindows()
                
            except :
                print("Invalid input! Please enter values properly.")
        

        # add some text
        elif user_input==4:
            try:
                text=input("Enter the text you want to show on image: ")
                x, y = map(int, input("Enter x,y position for text: ").split(','))
                fontScale=float(input("Enter the font scale you want: "))
                b,g,r = map(int, input("Enter the color value of BGR():  ").split(','))
                thickness=int(input("Enter the thickness: "))
                cv.putText(orig_image,text,(x,y),cv.FONT_HERSHEY_TRIPLEX, fontScale,(b,g,r),thickness,)
                cv.imshow("Edited Image",orig_image)
                cv.waitKey(0)
                cv.destroyAllWindows()
            except :
                print("Invalid input! Please enter values properly.")


        # exit the program
        elif user_input==5:
            print("Exiting The Program")
            sys.exit()

    
        # asking for saving the image       
        save_img=input(f"{user} do you want to save the image? (Y/N)")
        if save_img.lower() == "y":
            print("Please specify the name and format of the image:")
            name=input("name: ")
            format=input("format: ")
            cv.imwrite(f"{name}.{format}",orig_image)
            print(f"{name}.{format} saved successfully!")
