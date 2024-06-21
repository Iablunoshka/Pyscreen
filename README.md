# Pyscreen

This Python script provides an automated screen capture tool with additional functionality to copy either text or images to the clipboard based on user-defined actions.

## Features

- **Keyboard Shortcuts:** Detects and responds to keyboard shortcuts for initiating specific actions:
  - `Shift + Win + A`: Capture a screenshot and copy the text within the selected area.
  - `Alt + A`: Capture a screenshot and copy the selected area as an image.
- **Text Recognition:** Utilizes Tesseract OCR to extract text from captured screen areas and copy it to the clipboard.
- **Image Capture:** Copies the captured screen area as an image to the clipboard.
- **Easy Configuration:** Customizable keyboard shortcuts and other parameters for tailored use.

## Dependencies

- `Pillow (PIL)`: Required for image processing and saving screenshots.
- `pynput`: Used for monitoring mouse and keyboard events.
- `pytesseract`: Integrates Tesseract OCR for text recognition.
- `pyperclip`: For copying text to the clipboard.
- `win32clipboard`: Enables interaction with the Windows clipboard.
- `keyboard`: For capturing keyboard events.

## Installation

To install the necessary dependencies, run:
```bash
pip install Pillow pynput pytesseract pyperclip pywin32 keyboard
```

## Usage

1. **Run the script:**
   ```bash
   python pyscreen.py
   ```
2. **Keyboard Shortcuts:**
   - Press `Shift + Win + A` to capture a screen area and copy the text within it to the clipboard.
   - Press `Alt + A` to capture a screen area and copy it as an image to the clipboard.

3. **Selecting the Screen Area:**
   - Click and drag the mouse to select the area of the screen you want to capture.

4. **Customizing Shortcuts:**
   - You can customize the keyboard shortcuts and other settings by modifying the script.

## Notes

- Ensure that Tesseract OCR and its language packs are installed and configured properly for accurate text recognition.
- This tool is primarily designed for Windows operating systems due to its reliance on `win32clipboard`.


## Contact

If you have questions or suggestions, feel free to reach out to me on Discord: `6masia9`.
