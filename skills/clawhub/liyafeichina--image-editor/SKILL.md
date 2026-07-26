---
name: image-editor
description: Use this skill when the user asks to edit, modify, replace text, or add/remove elements in an image. Always preserve original resolution. Always verify output with vision model. Never resize or scale the image.
metadata: {"openclaw": {"requires": {"bins": ["python3"]}}}
---

# Image Editor Skill

## Core Rules (NEVER BREAK)

1. **Preserve original resolution** — never resize, scale, or change dimensions
2. **Verify every output with vision model** — use the `image` tool to check the result before delivering
3. **Use PIL directly** — Python PIL/Pillow for pixel-level manipulation, not external tools

## Workflow

### Step 1: Analyze the original image
```
python3 -c "
from PIL import Image
img = Image.open('PATH')
print(f'Size: {img.size}, Mode: {img.mode}')
"
```

### Step 2: Identify target region
- Open the image with `read` tool (supports jpg/png)
- Use `image` tool with prompt "identify the exact pixel coordinates of [target area]"
- Record: x_start, y_start, x_end, y_end

### Step 3: Edit with PIL
```python
from PIL import Image, ImageDraw, ImageFont
img = Image.open('INPUT')
draw = ImageDraw.Draw(img)

# For text replacement:
# 1. Fill background color over old text
# 2. Draw new text with matching font/color
# macOS Chinese fonts: /System/Library/Fonts/STHeiti Light.ttc

font = ImageFont.truetype('/System/Library/Fonts/STHeiti Light.ttc', size=PIXEL_SIZE)
draw.text((x, y), 'NEW TEXT', fill=(R, G, B), font=font)
img.save('OUTPUT.jpg', quality=95)
```

### Step 4: Verify output (MANDATORY)
Use the `image` tool on the output file with prompt:
"Compare this edited image with the original at ORIGINAL_PATH. Is the text replacement correct? Is resolution preserved? Any artifacts?"

### Step 5: Only deliver after verification passes

## Common mistakes (from real failures)
- ❌ Using web_fetch to "download" an image (it resizes)
- ❌ Skipping vision verification
- ❌ Calling external APIs that don't support the format
- ❌ Saving with wrong quality/format
- ✅ PIL direct pixel manipulation
- ✅ Vision verification of every output
