# Pyscreen

This Python script provides an automated screen capture tool with additional functionality to copy either text or images to the clipboard based on user-defined actions.

### Features:
- **Keyboard Shortcuts:** Detects and responds to keyboard shortcuts for initiating specific actions.
- **Text Recognition:** Utilizes Tesseract OCR to extract text from captured screen areas and copy it to the clipboard.
- **Image Capture:** Copies the captured screen area as an image to the clipboard.
- **Easy Configuration:** Customizable keyboard shortcuts and other parameters for tailored use.

### Dependencies:
- `Pillow (PIL)`: Required for image processing and saving screenshots.
- `pynput`: Used for monitoring mouse and keyboard events.
- `pytesseract`: Integrates Tesseract OCR for text recognition.
- `win32clipboard`: Enables interaction with the Windows clipboard.
- `keyboard`: For easy exit.
### Usage:
1. Run the script.
2. Press and hold the left mouse button while simultaneously pressing `Alt` to capture a screen area and copy text.
3. Press and hold the left mouse button while simultaneously pressing `Ctrl` to capture a screen area and copy it as an image.
4. Customize keyboard shortcuts or other settings as needed.

### Notes:
- Ensure that Tesseract OCR and its language packs are installed and configured properly for accurate text recognition.
- This tool is primarily designed for Windows operating systems due to its reliance on `win32clipboard`.

## Contact

If you have questions or suggestions, feel free to reach out to me on Discord: 6masia9
