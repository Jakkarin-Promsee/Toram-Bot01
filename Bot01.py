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
    tSkill = 0
    tBuff = 0
    delay = 0.1
    
    while True:
        game_window_title = "ToramOnline"  
        active_window = gw.getActiveWindow()
        if active_window is not None and active_window.title == game_window_title:
            time.sleep(1)
            tSkill+=1
            tBuff+=1
            
            if(tSkill >= 12):
                tSkill=0
                
                for _ in range(4-random.randint(0, 1)):
                    press('5',1)
                    now = delay+random.randint(0, 50)/100
                    time.sleep(now)
                    tBuff+=now
                    tSkill+=now
                    
                
                press('8',1)
                now = 3+random.randint(0, 50)/100
                time.sleep(now)
                tBuff+=now
                tSkill+=now
                
                press('7',1)
                now = 3+random.randint(0, 50)/100
                time.sleep(now)
                tBuff+=now
                tSkill+=now
                
                for _ in range(4-random.randint(0, 1)):
                    press('6',1)
                    now = delay+random.randint(0, 50)/100
                    time.sleep(now)
                    tBuff+=now
                    tSkill+=now
                
            
            if(tBuff>=240):
                tBuff=0
                press('4',2+random.randint(0, 1))
                now = delay+random.randint(0, 50)/100
                time.sleep(now)
                tBuff+=now
                tSkill+=now
