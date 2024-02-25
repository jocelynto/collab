from time import sleep
import win32gui
import win32con

def callback(handle, param):
    s = pywin32.win32gui.GetClassName(handle)
    try:
        print(f'Sending key to {handle}, {s}')
        win32gui.SendMessage(handle, pywin32.win32con.WM_KEYDOWN, ord("s"), 0)
        win32gui.SendMessage(handle, pywin32.win32con.WM_KEYUP, ord("s"), 0)
        sleep(2)
    except Exception:
        print('Exception sending to {handle}, {s}')

window_id = win32gui.FindWindow(None, "Command Prompt - python3 pedal_simplified.py")
win32gui.EnumChildWindows(window_id, callback, 0)