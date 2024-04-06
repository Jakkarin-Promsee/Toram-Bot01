import tkinter as tk
import threading
import pyautogui
import time
import pygetwindow as gw
import random

class BotController:
    def __init__(self, master):
        self.master = master
        master.title("Bot Controller")


        self.start_button = tk.Button(master, text="Start Bot", command=self.start_bot)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Bot", command=self.stop_bot, state=tk.DISABLED)
        self.stop_button.pack()

        self.status_label = tk.Label(master, text="Bot Stopped", fg="red")
        self.status_label.pack()

    def start_bot(self):
        self.bot_thread = threading.Thread(target=self.bot_thread_func)
        self.bot_thread.start()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.status_label.config(text="Bot Running", fg="green")

    def stop_bot(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.status_label.config(text="Bot Stopped", fg="red")
        
    def press(self, ch, t):
        active_window = gw.getActiveWindow()
        if active_window:
            Name_window_using = active_window.title
            window_using = gw.getWindowsWithTitle(Name_window_using)[0]

            window_game = gw.getWindowsWithTitle("ToramOnline")[0]
            window_game.activate()
            for _ in range(t):
                pyautogui.keyDown(ch)
                time.sleep(0.05)
                pyautogui.keyUp(ch)
            window_game.minimize()  # Minimize the game window
            
            if window_using:
                window_using.activate()

    def bot_thread_func(self):
        self.running = True
        tSkill = 900
        tBuff1 = 900
        tBuff2 = 900
        delay = 0.1
        
        while self.running:
            self.press('f',2)
            time.sleep(0.25)
            tSkill+=0.25
            tBuff1+=0.25
            tBuff2+=0.25
            
            if(tSkill>=1.75):
                time.sleep(0.5)
                tBuff1+=0.5
                tBuff2+=0.5
                tSkill+=0.5
                
                for _ in range(10-random.randint(0, 1)):
                    self.press('7',1)
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
                self.press('6',2)
                tBuff1 = 0
            
            if(tBuff2>=900):
                time.sleep(1)
                tBuff1+=1
                tBuff2+=1
                tSkill+=1
                self.press('8',2)
                tBuff2 = 0
            tBuff1+=1
            tBuff2+=1
            print(tBuff1)

def main():
    root = tk.Tk()
    controller = BotController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
