import pyautogui
import time
import pygetwindow as gw
import random
import datetime

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
    screen_width, screen_height = pyautogui.size()
    prev_pos = pyautogui.position()
    mouse_time_check = random.randint(60,300)
    
    tSkill = 9000
    tBuff1 = 9000
    tBuff2 = 9000
    delay = 0.1
    
    time_count = 0
    
    while True:
        game_window_title = "ToramOnline"  
        active_window = gw.getActiveWindow()
        
        if active_window is not None and active_window.title == game_window_title:
            if random.randint(0,10) == 0:
                r = random.randint(0,4)
                if r == 0:
                    press('w',2+random.randint(0,1))
                elif r == 1:
                    press('a',2+random.randint(0,1))
                elif r == 2:
                    press('s',2+random.randint(0,1))
                elif r == 3:
                    press('d',2+random.randint(0,1))
                    
            press('f',2)
            time.sleep(0.25)
            tSkill+=0.25
            tBuff1+=0.25
            tBuff2+=0.25
            mouse_time_check -= 1
            
            if tSkill >= 2:
                time.sleep(0.5)
                tBuff1+=0.5
                tBuff2+=0.5
                tSkill+=0.5
                
                for _ in range(10-random.randint(0, 1)):
                    if random.randint(0,4) == 0:
                        press('f',2)
                        
                    press('7',1)
                    now = delay+random.randint(10, 25)/100
                    time.sleep(now)
                    tBuff1+=now
                    tBuff2+=now
                    tSkill+=now
                tSkill = 0
            
            if tBuff1 >= 60:
                time.sleep(1)
                tBuff1+=1
                tBuff2+=1
                tSkill+=1
                press('6',2)
                tBuff1 = 0
                    
            if tBuff2>=900:
                time.sleep(1)
                tBuff1+=1
                tBuff2+=1
                tSkill+=1
                press('8',2)
                tBuff2 = 0
                
            if mouse_time_check <= 0:
                current_pos = pyautogui.position()
                dx = abs(current_pos[0] - prev_pos[0])
                dy = abs(current_pos[1] - prev_pos[1])
                if dx <= 30 or dy <= 30:
                    pyautogui.moveTo(x=random.randint(0, screen_height), y=random.randint(0, screen_width), duration=random.randint(1,3))
                prev_pos = pyautogui.position()
                mouse_time_check = random.randint(60,300)
            
                