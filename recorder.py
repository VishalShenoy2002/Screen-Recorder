import cv2
import numpy as np
import pyautogui
import datetime

'''
    TODO:
        1. Add Different Arguments to run it in a single Command
        2. Make a Menu Driven Program for the same
        3. Convert the original program into and Object Called Recorder ---> Done
'''

class Recorder:

    def __init__(self):

        self.FOURCC=cv2.VideoWriter_fourcc("m","p","4","v")
        self.FPS=12.0
        self.TIMESTAMP=str(datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S"))
        self.FILENAME="{}.mp4".format(self.TIMESTAMP)
        self.SIZE=(pyautogui.size()[0],pyautogui.size()[1])

        self.video=cv2.VideoWriter(self.FILENAME,self.FOURCC,self.FPS,self.SIZE)

    def record(self):
        while True:
            self.image=pyautogui.screenshot()
            self.image=np.array(self.image)
            self.image=cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

            self.video.write(self.image)
            cv2.imshow('Recording',self.image)
            if cv2.waitKey(1) & 0xFF==ord('q'):
                break
        self.video.release()
        cv2.destroyAllWindows()

print('''
   _____                            _____                        _           
  / ____|                          |  __ \                      | |          
 | (___   ___ _ __ ___  ___ _ __   | |__) |___  ___ ___  _ __ __| | ___ _ __ 
  \___ \ / __| '__/ _ \/ _ \ '_ \  |  _  // _ \/ __/ _ \| '__/ _` |/ _ \ '__|
  ____) | (__| | |  __/  __/ | | | | | \ \  __/ (_| (_) | | | (_| |  __/ |   
 |_____/ \___|_|  \___|\___|_| |_| |_|  \_\___|\___\___/|_|  \__,_|\___|_|   
                                                                             
                                                                             
''')


