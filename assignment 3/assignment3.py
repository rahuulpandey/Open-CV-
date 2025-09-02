import cv2 as cv 
import sys

print('''Which Camera do you want to select: 
0 → Laptop Cam 
1 → Mobile Cam''')


cam_type = int(input('Enter Your Choice: '))
camera=cv.VideoCapture(cam_type)


if cam_type not in range(0,2):
    sys.exit('select valid camera input')

else:

    while True:

        print('''\nSelect Camera Mode:
    1 → Live video only (just view)
    2 → Record video and save
    3 → Exit
              
    (PRESS q to Quit Cam Screen)
    (PRESS s to Save Cam Image)\n''')

        # taking choice input of user.
        user_choice_input=int(input("Enter Mode: "))

        #if user select option 1 (i.e. Live video only (just view))
        if user_choice_input==1:
            while True:
                success,frame=camera.read()
                cv.imshow("Live Video Cam", frame)

                if not success:
                    print('Camera Not Working! Check Camera!')
                    break 


                key_press= cv.waitKey(1) &0xff 
                if key_press==ord('q'):
                    print("Exiting VIDEO CAM.....")
                    break

                elif key_press == ord('s'):
                    saved_frame=frame.copy()
                    print("Closing Cam View to save image...")
                    break
            camera.release()
            cv.destroyAllWindows()
        
            if key_press == ord('s'):
                img_name=input("Enter Image Name: ")
                img_format=input("Enter Image Format: ").lower()
                cv.imwrite(f'{img_name}.{img_format}',frame)
                print(f"{img_name}.{img_format} saved successfully!")



        #if user select option 2 (i.e. Record video and save)
        elif user_choice_input==2:
            codec_map={
                'avi':'XVID',
                'mp4':'MP4V',
                'mov':'MP4V'
            }
            video_name=input('enter the name of the video file: ')
            video_format=input("enter the video format (avi/mp4/mov): ").lower()
            fps=int(input("Enter FPS: "))
            frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
            frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))
            codec_format = cv.VideoWriter_fourcc(*codec_map.get(video_format,'XVID'))
            recorder=cv.VideoWriter(f'{video_name}.{video_format}', codec_format , fps, (frame_width,frame_height))
            
            while True:
                success,frame=camera.read()
                
                if not success:
                    print('Camera Not Working! Check Camera!')
                    break

                recorder.write(frame)
                cv.imshow("recording live", frame)

                if cv.waitKey(1) & 0xff == ord("q"):
                    break

            camera.release()
            recorder.release()
            cv.destroyAllWindows()
                

        elif user_choice_input==3:
            print("Exiting....")
            sys.exit()

        else:
            print("Please choose a valid input")
