import numpy as np
import time
import cv2
from cvzone.HandTrackingModule import HandDetector
from pygame import mixer
cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector =HandDetector(detectionCon=0.8)

keys=[["C1","D1",'E1',"F1","G1","A2","B2","C2","D2","E2","F2","G2","A3","B3"],["C#","D#","F#","G#","A#","C#","D#","F#","G#","A#"]]

class Button():
    def __init__(self,pos,text,size,color):
        self.pos=pos
        self.size=size
        self.text=text
        self.color=color
buttonList=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):   
        if i==0:
            buttonList.append(Button([38*j+15,80],key,[35,100],(255,255,255)))
        else:
            buttonList.append(Button([(40+j)*j+25,80],key,[35,50],(0,0,0)))    

           
def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        colorr=button.color
        cv2.rectangle(img,button.pos,(x+w,y+h),colorr,cv2.FILLED)
        cv2.putText(img,button.text,(x+10,y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(214,0,220),2)
    return img    

while True:
    success,img=cap.read()
    img= detector.findHands(img)
    lmlist,bboxInfo=detector.findPosition(img)
    img=drawAll(img,buttonList)


    cv2.imshow("IMAGE",img)
    cv2.waitKey(1)


