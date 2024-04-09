import pygetwindow as gw
import time
import pyautogui
import datetime
import random

def activate_program(program_name):
    window = gw.getWindowsWithTitle(program_name)[0]
    window.activate()

def move_program_window(program_name, new_x, new_y):
    windows = gw.getAllWindows()
    for window in windows:
        if window.title == program_name:
            window.moveTo(new_x, new_y)
            print(f"move to ({new_x}, {new_y}).")
            return True
    return False

def get_program_position(program_name):
    windows = gw.getAllWindows()
    for window in windows:
        if window.title == program_name:
            return window.left, window.top
    return None

def get_program_size(program_name):
    windows = gw.getAllWindows()
    for window in windows:
        if window.title == program_name:
            return window.left-window.right, window.top-window.bottom
    return None

def press(ch, t):
    game_window_title = "ToramOnline"  
    active_window = gw.getActiveWindow()
    if active_window is not None and active_window.title == game_window_title:
        for _ in range(t):
            pyautogui.keyDown(ch)
            time.sleep(0.05)
            pyautogui.keyUp(ch)

def hold_press(ch, duration):
    game_window_title = "ToramOnline"  
    active_window = gw.getActiveWindow()
    pyautogui.keyDown(ch)
    time.sleep(duration)
    pyautogui.keyUp(ch)
    
def sell_item(position):
    #open terminal to go to Guild bar
    time.sleep(2)
    press('t',1) 
    time.sleep(1)
    pyautogui.moveTo(733+position[0], 246+position[1], duration=0.5)
    pyautogui.click()

    #wait the game loading
    time.sleep(10)

    #walk to seller
    hold_press('w',1.4)
    hold_press('a',1.6)
    time.sleep(1)

    #tell with seller, go to sell window
    time.sleep(2)
    press('f',1) 
    time.sleep(1)
    pyautogui.moveTo(499+position[0], 399+position[1], duration=0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(383+position[0], 234+position[1], duration=0.5)
    pyautogui.click()
    time.sleep

    #sell item, 1 loop can sell 20 item. Character have 75 slot (4time = 80 slot)
    for _ in range(4):
        #set base postion of each item in bag
        item_positions = [(526, 176), (615, 178), (708, 180), (799, 178), (894, 178)]

        #select item to sell
        for i in range(4):
            for pos in item_positions:
                pyautogui.moveTo(pos[0]+position[0], pos[1]+91*i+position[1], duration=0.2)
                pyautogui.click()
                time.sleep(0.05)
            time.sleep(0.1)
            
        #set sell button position
        sell_position = [(235, 234), (501, 495), (504, 433)]

        #click to sell item
        for pos in sell_position:
            pyautogui.moveTo(pos[0]+position[0], pos[1]+position[1], duration=0.5)
            pyautogui.click()
            time.sleep(0.2)

    #close sell window (end the sell)
    pyautogui.moveTo(923+position[0], 64+position[1], duration=0.5)
    pyautogui.click()
    time.sleep(1)

    #open terminal to go out guild bar
    time.sleep(2)
    press('t',1) 
    time.sleep(1)
    pyautogui.moveTo(733+position[0], 246+position[1], duration=0.5)
    pyautogui.click()    
    time.sleep(10)

def check_mana(position):
    #Check mana by check color where mana is 500mp
    # no mana (8, 9, 13) : black
    # 500 mana (108, 240, 219) : blue
    
    color = pyautogui.pixel(473+position[0], 496+position[1])
    target_color = (8, 9, 13)
    tolerance = 20
    within_range = all(abs(color[i] - target_color[i]) <= tolerance for i in range(3))

    if within_range:
        return False
    else :
        return True

    
if __name__ == "__main__":
    #setting and activate game terminal
    game_window_title = "ToramOnline"
    activate_program(game_window_title)
    
    #use to move game window
    # new_x, new_y = 0, 0
    # move_program_window(program_name, new_x, new_y)

    #read game window information to adjust mouse position
    time.sleep(1)
    position = get_program_position(game_window_title)
    size = get_program_size(game_window_title)
    screen_width, screen_height = pyautogui.size()
    pyautogui.FAILSAFE = False
    
    if position:
        print(f"position : {position}")
    if size:
        print(f"size : {size}")
        
    
    #setting timer variable
    prev_pos = pyautogui.position()
    mouse_time_check = random.randint(60,300)
    prev_time = datetime.datetime.now()
    run_time = datetime.datetime.now()
    
    #setting skill to zero
    tBuff1 = 0
    tBuff2 = 0
    sell = 0
    delay = 0.1
    time_count = 0
    
    while True:
        #check the main window now
        active_window = gw.getActiveWindow()
        
        #check that the game is main window
        if active_window is not None and active_window.title == game_window_title:
            
            #main farming function (normal attack)
            for _ in range(4+random.randint(0,2)):
                press('f',2)
                time.sleep(0.25)
    
            time.sleep(0.2)
            
            #main farming function (cyclone arrow)
            for _ in range(10-random.randint(0, 3)):
                #check mana enough
                if check_mana(position):
                    if random.randint(0,4) == 0:
                        press('f',2)
                        
                    press('7',1)
                    now = delay+random.randint(10, 25)/100
                    time.sleep(now)
            
            #count time
            current_time = datetime.datetime.now()
            different_time = current_time - prev_time
            different_run_time = current_time - run_time
            tBuff1 -= different_time.total_seconds()
            tBuff2 -= different_time.total_seconds()
            sell -= different_time.total_seconds()
            mouse_time_check -= different_time.total_seconds()
            prev_time = current_time
            print(f"Afk: {different_run_time.total_seconds()/60:.2f}m, sell: {sell:.1f}s, tBuff1: {tBuff1:.1f}s, tBuff2: {tBuff2:.1f}s")
            
            #function to sell item in bag when it full
            if sell <= 0:
                sell_item(position)
                sell = 1200
                tBuff1 = 0
                tBuff2 = 0
            
            #main buff1 fuction (detection skill) CD:60s
            if tBuff1 <= 0:
                time.sleep(1)
                press('6',2)
                tBuff1 = 60
                   
            #main buff2 fuction (brave aura skill) CD: 15m
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
                    
            #make nopattern mouse movement  
            if mouse_time_check <= 0:
                current_pos = pyautogui.position()
                dx = abs(current_pos[0] - prev_pos[0])
                dy = abs(current_pos[1] - prev_pos[1])
                if dx <= 30 or dy <= 30:
                    new_x = random.randint(30+position[0], screen_width - 30+position[1])
                    new_y = random.randint(30+position[0], screen_height - 30+position[1])
                    pyautogui.moveTo(x=new_x, y=new_y, duration=random.randint(1,3))
                prev_pos = pyautogui.position()
                mouse_time_check = random.randint(60,300)
    





    

    


