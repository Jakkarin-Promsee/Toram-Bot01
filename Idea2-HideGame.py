import pyautogui
import time
import threading
import pygetwindow as gw



def write_to_display(window_title, window):
    i = 0
    while True:
        try:
            window.activate()
            window.hide()  # Hide the window
            pyautogui.typewrite('z', interval=0.05)  # Type 'z' with a 0.1s interval
            print(f'Wrote "z" to {window_title}')
            window.activate()  # Activate the window again to ensure focus
        except IndexError:
            print(f'Window "{window_title}" not found')
        time.sleep(3)  # Wait for 3 seconds before repeating
        i+=3
        if(i>=9):
            window.show()  # Show the window after typing
            time.sleep(10)

if __name__ == "__main__":
    # Specify the program window titles
    window = gw.getWindowsWithTitle("ToramOnline")[0]

    # Start a thread for each program
    threads = []
    thread = threading.Thread(target=write_to_display, args=("ToramOnline", window))
    threads.append(thread)
    thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
