from PIL import ImageGrab, ImageTk, Image
import tkinter as tk
import keyboard
import threading
from pynput.mouse import Listener, Button
import win32clipboard
from io import BytesIO
import pytesseract
import pyperclip


copy_flag = None
x1, y1, x2, y2 = None, None, None, None
root = None
listener_active = False

def on_key_released(event):
    global copy_flag
    if keyboard.is_pressed('shift') and keyboard.is_pressed('win') and keyboard.is_pressed('a'):
        print("Shift+win+A")
        copy_flag = True
        capture_screenshot()
    elif keyboard.is_pressed('alt') and keyboard.is_pressed('a'):
        copy_flag = False
        print("Alt+a")
        capture_screenshot()

def capture_screenshot():
    image = ImageGrab.grab()
    image.save("C:\\Users\\User_name\\Pictures\\Screenshots\\screen.png")
    show_screenshot(image)

def show_screenshot(image):
    global root, listener_active
    root = tk.Tk()
    root.title("Screen")
    img_width, img_height = image.size
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry(f"{img_width}x{img_height}+{(root.winfo_screenwidth() - img_width) // 2}+{(root.winfo_screenheight() - img_height) // 2}")
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

    listener_active = True
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.start()
    root.mainloop()

def close_window():
    global root, listener_active
    if root is not None:
        root.destroy()
        root = None
        listener_active = False
        print("end0")

def on_click(x, y, button, pressed):
    global x1, y1, x2, y2, listener_active
    if not listener_active:
        return False
    if button == Button.left and pressed:
        coordinates(x, y)


def coordinates(x, y):
    global x1, y1, x2, y2
    if x1 is None and y1 is None:
        x1 = x
        y1 = y
    else:
        x2 = x
        y2 = y
        print(f"Start coordinates: X = {x1}, Y = {y1}")
        print(f"End coordinates: X = {x2}, Y = {y2}")
        screen()

def screen():
    global x1, y1, x2, y2,copy_flag
    screenshot = ImageGrab.grab(bbox=(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    screen_path = "C:\\Users\\User_name\\Pictures\\Screenshots\\screen.png"
    screenshot.save(screen_path)
    if copy_flag:
        image = Image.open(screen_path)
        text = pytesseract.image_to_string(image, lang='rus+eng+ukr')
        pyperclip.copy(text)
        print("Copy text")
    else:
        image = Image.open(screen_path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()
        print("Copy img")

    x1, y1, x2, y2 = None, None, None, None
    root.after(0, close_window)  # Close window in the main thread

def start_listener():
    with Listener(on_click=on_click) as mouse_listener:
        mouse_listener.join()

keyboard.hook(on_key_released)
keyboard.wait('shift+tab')
