# Image Randomizer Tool

## Description
This Python project allows you to **randomly combine and modify three BMP images**. The images are resized to 400x400 pixels and processed pixel by pixel with random operations to generate three new images.  

The final images are saved as PNG both in a default `output/` folder and in a directory of your choice.

---

## Features
- Resize input images to 400x400
- Random pixel manipulation combining three images
- Supports BMP images
- Saves output as PNG
- Opens an HTML file (`index.html`) after processing

---

## Requirements
- Python 3.8+
- [Pillow](https://pypi.org/project/Pillow/) library

## Install dependencies
```bash
pip install Pillow
```

## Usage 
1. Run the program:
```bach
python main.py
```

2. Select three BMP images when prompted.

3. Select a directory to save output images.

4. Check the output/ folder or your chosen directory for results:

- a_f.png

- b_f.png

- c_f.png

The program will also open index.html in your default browser.
