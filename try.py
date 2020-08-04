# import cv2
#
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# chart = cv2.imread('abc.png')
# cap = cv2.VideoCapture(0)
# i = 0
# mov_x = 0
# mov_y = 0
# moved_x = 320
# moved_y = 240
# mov_x = 0
# mov_y = 0
# while cap.isOpened():
#     _, img = cap.read()
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     happy = cv2.imread('happy.jfif')
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 4)
#         cen_x = x+1/2*w
#         cen_y = y+1/2*h
#         if i ==0 :
#             cal_x = cen_x
#             cal_y = cen_y
#         moved_x = moved_x + int(mov_x)
#         moved_y = moved_y + int(mov_y)
#         mov_x = 0
#         mov_y = 0
#         if moved_x-20 < 0 or moved_y-20 <0 or moved_x +20 >640 or moved_y +20 >480:
#             moved_x = 320
#             moved_y = 240
#         img = cv2.circle(img, (moved_x,moved_y), 20, (0, 255, 0), -1)
#         if abs(cal_y-cen_y) > 15:
#             if cal_y>cen_y:
#                 mov_y = -6
#             else:
#                 mov_y = 6
#         elif abs(cal_x-cen_x)> 20:
#             if cal_x>cen_x:
#                 mov_x = -6
#             else:
#                 mov_x = 6
#         img = cv2.circle(img,(int(cen_x),int(cen_y)),2,(0,255,0),-1)
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = img[y:y + h, x:x + w]
#         eyes = eye_cascade.detectMultiScale(roi_gray)
#         for (ex,ey,ew,eh) in eyes:
#             cv2.rectangle(roi_color, (ex,ey),(ex+ew,ey+eh),(0, 255, 0), 5)
#     img= cv2.flip(img, 1)
#
#     cv2.imshow('img', img)
#     i = i + 1
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# cap.release()




from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import vlc
import datetime
import time
import cv2
from random import *

root = Tk()
root.title(" It's just a trail")


# frame = LabelFrame(root,text = "This is a button",padx=25,pady =25)
# frame.pack(padx = 30, pady= 30)
# b = Button(frame, text = "click on it",padx=5,pady =15).grid(row=0,column = 0)
# b2 = Button(frame, text = "click on it",padx=5,pady =15).grid(row=1,column = 1)

# r = IntVar()
# r.set('2')
# i = 0
#
# def clicked():
#     global i
#     i += 1


# def popup():
#     response = messagebox.askquestion("Hello World","this is my zone now")
#     Label(root,text = response).pack()
def check_time():
    global idle_times
    myLabel.configure(text=datetime.datetime.now().replace(microsecond=0))
    current_time = datetime.datetime.now()

    if current_time.minute == 0 and current_time.second == 0:
        p = vlc.MediaPlayer(
            ("sounds" + char_list[char_pos] + str(current_time.hour) + ".mp3"))
        p.play()
        idle_times = [randint(5, 25),randint(35, 55)]

    if (current_time.minute in idle_times) and current_time.second == 0:
        Free_voice = vlc.MediaPlayer("sounds" + char_list[char_pos] + "_free.mp3")
        Free_voice.play()
    root.after(1000, check_time)

def reset():
    global char_pos
    if char_pos == len(char_list):
        char_pos = 0

def change_char():
    global my_char
    global char_list
    global char_pos
    char_pos += 1
    reset()
    intro_char(char_list, char_pos)
    my_char = ImageTk.PhotoImage(
        Image.open('Characters' + char_list[char_pos] + '.png'))
    global Label_img
    Label_img.configure(image=my_char)


def intro_char(char_list, char_pos):
    global intro_voice
    if intro_voice.is_playing:
        intro_voice.stop()
    intro_voice = vlc.MediaPlayer("sounds" + char_list[char_pos] + "_Intro.mp3")
    intro_voice.play()

def check_idle():
    global char_list
    global char_pos
    global idle_times
    myLabel = Label(root, text= idle_times)
    myLabel.grid(row=2, column=7)
    Free_voice = vlc.MediaPlayer("sounds" + char_list[char_pos] + "_free.mp3")
    Free_voice.play()


char_pos = -1
char_list = ['\Верный','\Warspite','\Kawakaze','\Yura','\Ark_Royal']
idle_times = [randint(5, 25),randint(35, 55)]

intro_voice = vlc.MediaPlayer(r"sounds/TitleCallA" + str(randint(1, 20)) + ".mp3")
intro_voice.play()

frame_time = LabelFrame(root,text = "Current Time",padx = 20, pady= 5)
frame_time.grid(row = 0, column = 0,columnspan = 3,padx = 10, pady= 1)
myLabel = Label(frame_time, text=datetime.datetime.now().replace(microsecond=0))
myLabel.grid(row = 0, column = 0)

check_time()


button_pop = Button(root, text="switch character", padx=10, pady=5, command=change_char)
button_pop.grid(row =1, column=0,columnspan = 1,padx = 10, pady= 10)


button_quit = Button(root, text="Quit", padx=10, pady=5, command=root.quit)
button_quit.grid(row=1, column=1, columnspan=4, padx=10, pady=10)


button_check_idle = Button(root, text="check idle voice", padx=10, pady=5, command=check_idle)
button_check_idle.grid(row =1, column=6,columnspan = 10,padx = 60, pady= 10)


my_img = ImageTk.PhotoImage(Image.open('Characters\logo.png'))
Label_img = Label(root, image=my_img)
Label_img.grid(row=2, column=0,columnspan = 3,padx = 10, pady= 10)

# r1 = Radiobutton(root, text="Option1",variable = r,value = 1, command = lambda:clicked(i))
# r1.pack()

# r2 = Radiobutton(root, text="Option2",variable = r,value = 2,command = lambda:clicked(i))
# r2.pack()

# myButton = Button(root,text = "check",padx=30,pady =12.5,command = lambda:clicked(r.get()))
# myButton.pack(padx = 40)

# button_pop = Button(root, text = "clock_hibiki", padx = 10, pady = 5,command = clock_Hibiki)
# button_pop.pack(padx = 10, pady= 10)

root.mainloop()









