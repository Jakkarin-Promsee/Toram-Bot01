import pyautogui
import time
import pygetwindow as gw
import random

def hold_press(duration, ch):
    pyautogui.keyDown(ch)
    time.sleep(duration)
    pyautogui.keyUp(ch)
    
def press(ch, t):
    game_window_title = "ToramOnline"  
    active_window = gw.getActiveWindow()
    if active_window is not None and active_window.title == game_window_title:
        for _ in range(t):
            pyautogui.keyDown(ch)
            time.sleep(0.05)
            pyautogui.keyUp(ch)

if __name__ == "__main__":
    tSkill = 9000
    tBuff1 = 9000
    tBuff2 = 9000
    delay = 0.1
    
    while True:
        game_window_title = "ToramOnline"  
        active_window = gw.getActiveWindow()
        if active_window is not None and active_window.title == game_window_title:
            press('f',2)
            time.sleep(0.25)
            tSkill+=0.25
            tBuff1+=0.25
            tBuff2+=0.25
            
            if(tSkill>=2):
                time.sleep(0.5)
                tBuff1+=0.5
                tBuff2+=0.5
                tSkill+=0.5
                
                for _ in range(10-random.randint(0, 1)):
                    press('7',1)
                    now = delay+random.randint(10, 25)/100
                    time.sleep(now)
                    tBuff1+=now
                    tBuff2+=now
                    tSkill+=now
                tSkill = 0
            
            if(tBuff1>=60):
                time.sleep(1)
                tBuff1+=1
                tBuff2+=1
                tSkill+=1
                press('6',2)
                tBuff1 = 0
            
            if(tBuff2>=900):
                time.sleep(1)
                tBuff1+=1
                tBuff2+=1
                tSkill+=1
                press('8',2)
                tBuff2 = 0