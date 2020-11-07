from tkinter import *
from PIL import ImageTk,Image
import vlc
import datetime
import time
from random import *

root = Tk()
root.title(" Kantai Collection Clock")

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

char_pos = -1
char_list = ['Верный','Warspite','Kawakaze','Yura','Ark_Royal']
idle_times = [randint(5, 25),randint(35, 55)]

intro_voice = vlc.MediaPlayer(r"sounds/TitleCallA" + str(randint(1, 20)) + ".mp3")
intro_voice.play()

frame_time = LabelFrame(root,text = "Current Time",padx = 20, pady= 5)
frame_time.grid(row = 0, column = 0,columnspan = 3,padx = 10, pady= 1)
myLabel = Label(frame_time, text=datetime.datetime.now().replace(microsecond=0))
myLabel.grid(row = 0, column = 0)

check_time()


button_pop = Button(root, text="Next character", padx=10, pady=5, command=change_char)
button_pop.grid(row =1, column=0,columnspan = 1,padx = 10, pady= 10)


button_quit = Button(root, text="Quit", padx=10, pady=5, command=root.quit)
button_quit.grid(row=1, column=1, columnspan=4, padx=10, pady=10)


button_check_idle = Button(root, text="check idle voice", padx=10, pady=5, command=check_idle)
button_check_idle.grid(row =1, column=6,columnspan = 10,padx = 60, pady= 10)


my_img = ImageTk.PhotoImage(Image.open('Characters\logo.png'))
Label_img = Label(root, image=my_img)
Label_img.grid(row=2, column=0,columnspan = 3,rowspan = 10, padx = 10, pady= 10)

characters = StringVar()
menu = OptionMenu(root,characters,*char_list)
menu.grid(row=2, column=6,columnspan = 10,padx = 60, pady = 10)
characters.trace("w", switch_char)

root.mainloop()









