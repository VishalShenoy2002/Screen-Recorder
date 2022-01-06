import cv2
import numpy as np
import pyautogui
import datetime

FOURCC=cv2.VideoWriter_fourcc("m","p","4","v")
FPS=12.0
TIMESTAMP=str(datetime.datetime.now().strftime("%d-%m-%y %H-%M-%S"))
FILENAME="{}.mp4".format(TIMESTAMP)
SIZE=(pyautogui.size()[0],pyautogui.size()[1])

video=cv2.VideoWriter(FILENAME,FOURCC,FPS,SIZE)

while True:
    image=pyautogui.screenshot()
    image=np.array(image)
    image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    video.write(image)
    cv2.imshow('Recording',image)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()
