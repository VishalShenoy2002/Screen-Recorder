from tkinter import *
from tkinter.messagebox import askyesno


import pyautogui
import cv2
import numpy as np
import datetime


class QRecorder:
    
    FOURCC=cv2.VideoWriter_fourcc("m","p","4","v")
    FPS=12.0

    TIMESTAMP=str(datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S"))
    FILENAME="{}.mp4".format(TIMESTAMP)

    SIZE=(pyautogui.size()[0],pyautogui.size()[1])

    VIDEO=cv2.VideoWriter(FILENAME,FOURCC,FPS,SIZE)
    recording=False

    
    def __init__(self,master):

        self.master=master
        self.master.title("Q Recorder")
        self.master.geometry('500x250')

    
        self.file_location_frame=Frame(self.master)
        self.file_location_frame.pack()

        self.file_location_label=Label(self.file_location_frame,width=40)
        self.file_location_label.configure(text="Click Browse Button To Select File Location")
        self.file_location_label.pack(pady=10,side=LEFT,padx=10)

        self.file_location_browse_button=Button(self.file_location_frame,width=13)
        self.file_location_browse_button.configure(text="Browse")
        self.file_location_browse_button.pack(pady=10,side=LEFT)

        self.record_button=Button(self.master,width=30,height=5,bg='red',font=('',14,'bold'),activebackground='red2',command=self.record)
        self.record_button.configure(text="Start Recording")
        self.record_button.pack(pady=30,anchor=CENTER)

        self.master.mainloop()


    def record(self):
        if self.recording==False:
            self.record_button.configure(text="Stop Recording")
            self.recording=True
            self.start_recording()
        else:
            
            self.recording=False

    def start_recording(self):
        while self.recording==True:
            try:
                image=pyautogui.screenshot()
                image=np.array(image)
                image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                self.VIDEO.write(image)

            except KeyboardInterrupt:
                self.recording=False
                self.record_button.configure(text="Start Recording")
                

                
    

        


if __name__=="__main__":
    root=Tk()
    app=QRecorder(root)