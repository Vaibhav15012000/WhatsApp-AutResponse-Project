import pyautogui as pt
import time
import pyperclip
import random
import cv2
from selenium import webdriver


#chrome_browser=webdriver.Chrome(executable_path="C:\\Users\lenovo\WhatsApp Bot\WhatsApp\chromedriver")
#chrome_browser.get("https://web.whatsapp.com/")

time.sleep(5)


img = cv2.imread("C:\\Users\lenovo\WhatsApp Bot\WhatsApp\Smiley_paperclip.png")
position1=pt.locateOnScreen(img,confidence=.8)

x=position1[0]
y=position1[1]

#Gets message
def get_message():
    global x,y 
    
    img = cv2.imread("C:\\Users\lenovo\WhatsApp Bot\WhatsApp\Smiley_paperclip.png")
    position=pt.locateOnScreen(img,confidence=.8)
    x=position[0]
    y=position[1]
    
    pt.moveTo(x,y,duration=.5)
    pt.moveTo(x+85,y-40,duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(30,-200)
    pt.click()
    whatsap_message = pyperclip.paste()
    pt.click()
    print("Message_recieved:" + whatsap_message)

    
    return whatsap_message
   

#Posts 
def post_response(message):
    global x,y 
    
    img = cv2.imread("C:\\Users\lenovo\WhatsApp Bot\WhatsApp\Smiley_paperclip.png")
    position=pt.locateOnScreen(img,confidence=.6)
    x=position[0]
    y=position[1]
    
    pt.moveTo(x+200,y+20,duration=.5)
    pt.click()
    
    pt.typewrite(message,interval=.01)
    
    pt.typewrite("\n",interval=.01)
    
#Processes_Response
def process_response(message):
    random_no=random.randrange(3)
    
    if "?" in str(message).lower():
        return "Dont ask Questions?"
    
    else:
        if random_no==0:
            return "That's cool"
        elif random_no==1:
            return"Good morning"
        else:
            return "Bye"
        
        
        time.sleep(10)
        
        
        check_for_new_messages()
        
        
        
        
        
        
        
        
        
#check for new messages
def check_for_new_messages():
    pt.moveTo(x+70,y-33,duration=.5)


    while True:
        try:
            img1 = cv2.imread("C:\\Users\lenovo\WhatsApp Bot\WhatsApp\Green_dot.png")
            position=pt.locateOnScreen(img1,confidence=.7)
            
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                time.sleep(.5)
            
            
            
            
        except(Exception):
            print("No new messages!!!")
            
        if pt.pixelMatchesColor(int(x+70),int(y-33),(255,255,255),tolerance=10):
            print("Is_white")
            processed_message=process_response(get_message())        
            post_response(processed_message)
            
        else:
            print("No new messages!!...")
            
        time.sleep(10)
        
        
    
    
check_for_new_messages()    
processed_message=process_response(get_message())        
post_response(processed_message)




    