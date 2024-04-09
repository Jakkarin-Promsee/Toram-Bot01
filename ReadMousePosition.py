from pynput.mouse import Listener

def on_click(x, y, button, pressed):
    if button == button.left and pressed:
        print(f"Left-click detected at position: ({x}, {y})")

# Start the listener to monitor mouse events
with Listener(on_click=on_click) as listener:
    listener.join()