# # Python 2.x program for Speech Recognition
#
# import speech_recognition as sr
#
# # enter the name of usb microphone that you found
# # using lsusb
# # the following name is only used as an example
# mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
# # Sample rate is how often values are recorded
# sample_rate = 48000
# # Chunk is like a buffer. It stores 2048 samples (bytes of data)
# # here.
# # it is advisable to use powers of 2 such as 1024 or 2048
# chunk_size = 2048
# # Initialize the recognizer
# r = sr.Recognizer()
#
# # generate a list of all audio cards/microphones
# mic_list = sr.Microphone.list_microphone_names()
#
# # the following loop aims to set the device ID of the mic that
# # we specifically want to use to avoid ambiguity.
# for i, microphone_name in enumerate(mic_list):
#     if microphone_name == mic_name:
#         device_id = i
#
#     # use the microphone as source for input. Here, we also specify
# # which device ID to specifically look for incase the microphone
# # is not working, an error will pop up saying "device_id undefined"
# with sr.Microphone() as source:
#     # wait for a second to let the recognizer adjust the
#     # energy threshold based on the surrounding noise level
#     r.adjust_for_ambient_noise(source)
#     print("Say Something")
#     # listens for the user's input
#     audio = r.listen(source)
#
#     try:
#         text = r.recognize_google(audio)
#         print("you said: " + text)
#
#         # error occurs when google could not understand what was said
#
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#
#     except sr.RequestError as e:
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))




# # importing the pyttsx library
# import pyttsx3
#
# # initialisation
# engine = pyttsx3.init()
#
# # testing
# engine.say("My first code on text-to-speech")
# engine.say("Thank you, hackjnu")
# engine.runAndWait()




# from tkinter import *
#
# root=Tk()
# root.geometry('1000x1000')
#
# root.title("Park_me")
#
# l=Label(root,text="Finding Parking Made Easy")
# l.pack()
#
# b=Button(root,text="Find Parking")
# b.pack()
#
# root.mainloop()


import mysql.connector
import tkinter as tk                 # python 3
from tkinter import font  as tkfont  # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

# from PIL import ImageTK, Image

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Perfect Solution For Your Parking", font=controller.title_font)
        label.pack(side="top", fill="x", pady=150)

        button1 = tk.Button(self, text="Find Parking!",command=lambda: controller.show_frame("PageOne"))

        button2 = tk.Button(self, text="Provide Parking!",command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Route Map", font=controller.title_font)
        label.pack(side="top", fill="x", pady=100)
        button = tk.Button(self, text="Go to the start page",command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()


    mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="hackjnu")

    mycursor = mydb.cursor()

    mycursor.execute("select * from provide")

    for i in mycursor:
        print(i)
        print()
    app.geometry('1000x1000')

    app.title("Park_me")

    # canvas=tk.Canvas(app,width=300,height=160)
    # image=ImageTK.PhotoImage(Image.open())

    app.mainloop()
