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
    prev_time = datetime.datetime.now()
    run_time = datetime.datetime.now()
    
    tBuff1 = 0
    tBuff2 = 0
    delay = 0.1
    time_count = 0
    
    while True:
        game_window_title = "ToramOnline"  
        active_window = gw.getActiveWindow()
        
        #Check that the game is main window
        if active_window is not None and active_window.title == game_window_title:
            
            #Main Farming function (Syclone arrow)
            for _ in range(4+random.randint(0,2)):
                press('f',2)
                time.sleep(0.25)
    
            time.sleep(0.2)
            
            for _ in range(10-random.randint(0, 3)):
                if random.randint(0,4) == 0:
                    press('f',2)
                    
                press('7',1)
                now = delay+random.randint(10, 25)/100
                time.sleep(now)
            
            #Count time
            current_time = datetime.datetime.now()
            different_time = current_time - prev_time
            different_run_time = current_time - run_time
            tBuff1 -= different_time.total_seconds()
            tBuff2 -= different_time.total_seconds()
            mouse_time_check -= different_time.total_seconds()
            prev_time = current_time
            print(f"Afk: {different_run_time.total_seconds()/60:.2f}m, Use: {different_time.total_seconds():.1f}s, tBuff1: {tBuff1:.1f}s, tBuff2: {tBuff2:.1f}s")
            
            #Main Buff1 fuction (Detection Skill) CD:60s
            if tBuff1 <= 0:
                time.sleep(1)
                press('6',2)
                tBuff1 = 60
                   
            #Main Buff1 fuction (Brave Ora Skill) CD: 15m
            if tBuff2 <= 0:
                time.sleep(1)
                press('8',2)
                tBuff2 = 900
                
            #Make nopattern character movement
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
                    
            #Make nopattern mouse movement  
            if mouse_time_check <= 0:
                current_pos = pyautogui.position()
                dx = abs(current_pos[0] - prev_pos[0])
                dy = abs(current_pos[1] - prev_pos[1])
                if dx <= 30 or dy <= 30:
                    new_x = random.randint(30, screen_width - 30)
                    new_y = random.randint(30, screen_height - 30)
                    pyautogui.moveTo(x=new_x, y=new_y, duration=random.randint(1,3))
                prev_pos = pyautogui.position()
                mouse_time_check = random.randint(60,300)

                
            
            
                