"""
Test Tesseract OCR installation.
"""
import os, sys
os.environ["TESSERACT_PATH"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image, ImageDraw

# Create test image
img = Image.new("RGB", (200, 50), "white")
draw = ImageDraw.Draw(img)
draw.text((10, 10), "Hello Test", fill="black")

text = pytesseract.image_to_string(img, lang="eng")
print("OCR result:", repr(text.strip()))
assert "Hello" in text, f"Expected Hello, got {text}"

# Check available langs
import subprocess
result = subprocess.run(
    [r"C:\Program Files\Tesseract-OCR\tesseract.exe", "--list-langs"],
    capture_output=True, text=True
)
print("Available langs:", result.stdout)
print("Tesseract English OCR: OK")
