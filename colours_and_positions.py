import pyautogui as pt
import time

while True:
    posXY=pt.position()
    try:
        print(posXY,pt.pixel(posXY[0],posXY[1]))
    
    except:
        print(posXY,pt.pixel(posXY[0],posXY[1]))
     
    time.sleep(1)
    
    if posXY[0]==0:
        break
    
    
            
    
    