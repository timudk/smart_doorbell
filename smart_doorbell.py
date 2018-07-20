import tkinter
import numpy as np
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import cv2
from tkinter import *

class Return_Value_In_Entry():
    def __init__(self):
        self.Master=Tk()

        self.Entry=Entry(self.Master)
        self.Entry.pack()

        self.Button=Button(self.Master,text="Submit",command=self.Return)
        self.Button.pack()            

        self.Master.mainloop()

    def Return(self):
        self.TempVar=self.Entry.get()
        self.Master.destroy()

def read_api_key():
	f = open('.clarifai_api_key.txt','r')
	message = f.read().splitlines()
	return ClarifaiApp(api_key=message[0])

test = Return_Value_In_Entry()

app = read_api_key()

model = app.models.get('d02b4508df58432fbb84e800597b8959')

def diff_funct(pic1, pic2):
    diff = 0
    for i in range(1, len(pic1)):
        diff += (pic1[i]-pic2[i]) * (pic1[i]-pic2[i])

    diff = np.sqrt(diff)
    return diff


def doorbell():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    user = []
    friend_name = False

    while True:

        ret, frame = cam.read()
        #cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        #while cv2.waitKey(30) < 0:
        
        if ret and friend_name:
            strin = 'Hello {}'.format(friend_name)
            cv2.putText(frame, strin, (50, 50), cv2.FONT_ITALIC, 0.8, 255)
            cv2.imshow('Video', frame)
        elif ret:
            cv2.putText(frame, 'Hello World', (50, 50), cv2.FONT_ITALIC, 0.8, 255)
            cv2.imshow('Video', frame)
        
        
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
            
        elif k%256 == 117:
            superuser = Return_Value_In_Entry()

            img_name = "superuser_{}_{}.png".format(superuser.TempVar, img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            
            usr_img = ClImage(filename=img_name)
            usr_img_pred = model.predict([usr_img])
            while True:
                try:
                    pic1 = usr_img_pred['outputs'][0]['data']['regions'][0]['data']['embeddings'][0]['vector']
                    user.append([[pic1],[]])
                    break
                except KeyError:
                    print ("Oops!  That was no valid number.  Try again...")
            
        elif k%256 == 102:
            if len(user) == 0:
                print("you first have to add a superuser")
            else:
                usr_friend = Return_Value_In_Entry()
                
                img_name = "friend_{}_{}.png".format(usr_friend.TempVar, img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                
                usr_img = ClImage(filename=img_name)
                usr_img_pred = model.predict([usr_img])
                while True:
                    try:
                        pic1 = usr_img_pred['outputs'][0]['data']['regions'][0]['data']['embeddings'][0]['vector']
                        user[0][1].append([pic1, usr_friend.TempVar])
                        break
                    except KeyError:
                        print ("Oops!  That was no valid number.  Try again...")
            
        elif k%256 == 32:
            # SPACE pressed
            if len(user) == 0:
                print("you first have to add a superuser")
            else:
                if len(user[0][1]) == 0:
                    print("you first have to add a friend")
                else:
                    img_name = "opencv_frame_{}.png".format(img_counter)
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    
                    differences = []
                    for i in user[0][1]:
                        test_img = ClImage(filename=img_name)
                        test_img_pred = model.predict([test_img])
                        while True:
                            try:
                                pic2 = test_img_pred['outputs'][0]['data']['regions'][0]['data']['embeddings'][0]['vector']
                                break
                            except KeyError:
                                print ("Oops!  That was no valid number.  Try again...")

                        differences.append(diff_funct(i[0], pic2))
                        img_counter += 1
                    print(differences)
                    friend_name = user[0][1][differences.index(min(differences))][1]

    cam.release()

    cv2.destroyAllWindows()

def main():
    doorbell()

if __name__ == '__main__':
    main()