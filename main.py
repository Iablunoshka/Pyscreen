import pyautogui
from PIL import ImageGrab, Image
from pynput.mouse import Listener, Button
from pynput import keyboard as kb
from pynput.keyboard import Key
import win32clipboard
from io import BytesIO
import keyboard
import pytesseract
import pyperclip

x1, y1, x2, y2 = None, None, None, None
alt_pressed = False
ctrl_pressed = False

# Функция для обработки нажатий клавиш клавиатуры
def on_key_press(key):
    global alt_pressed, ctrl_pressed
    if key == Key.alt_l:
        alt_pressed = True
    elif key == Key.ctrl_l:
        ctrl_pressed = True

# Функция для обработки отпускания клавиш "Alt" и "Ctrl"
def on_key_release(key):
    global alt_pressed, ctrl_pressed
    if key == Key.alt_l:
        alt_pressed = False
    elif key == Key.ctrl_l:
        ctrl_pressed = False

# Функция для обработки нажатий левой кнопки мыши
def on_click(x, y, button, pressed):
    global x1, y1, x2, y2
    if button == Button.left and pressed and alt_pressed:
        copy_flag = True
        coordinates(x, y,copy_flag)
    elif button == Button.left and pressed and ctrl_pressed:
        copy_flag = False
        coordinates(x, y, copy_flag)



def coordinates(x, y,copy_flag):
    global x1, y1, x2, y2
    if x1 is None and y1 is None:
        x1 = x
        y1 = y
    else:
        x2 = x
        y2 = y

        print(f"Начальные координаты: X = {x1}, Y = {y1}")
        print(f"Конечные координаты: X = {x2}, Y = {y2}")
        screen(copy_flag)


def screen(copy_flag):
    global x1, y1, x2, y2
    # Захватываем изображение экрана в заданных координатах
    screenshot = ImageGrab.grab(bbox=(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)))
    # Сохраняем скриншот в файл
    screen_path = "C:\\Users\\Moldovan_Gaming\\Pictures\\Screenshots\\screen.png"
    screenshot.save(screen_path)

    if copy_flag==True:
        print("copy text")
        # Копирование текста в буфер обмена
        image = Image.open(screen_path)
        text = pytesseract.image_to_string(image, lang='rus+eng+ukr')
        pyperclip.copy(text)
    elif copy_flag==False:
        print("copy img")
        # Копирование изображения в буфер обмена
        image = Image.open(screen_path)
        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

    x1, y1, x2, y2 = None, None, None, None


# Запуск прослушивания событий мыши и клавиатуры
with Listener(on_click=on_click) as mouse_listener:
    with kb.Listener(on_press=on_key_press, on_release=on_key_release) as keyboard_listener:
        keyboard.wait('q')
