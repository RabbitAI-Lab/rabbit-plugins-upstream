---
slug: control
name: control
version: "1.0.0"
displayName: Control
summary: Advanced desktop automation with mouse, keyboard, and screen control
license: MIT
description: |-
  Advanced desktop automation with mouse, keyboard, and screen control

  核心能力:

  - 效率工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 工作流自动化、任务调度、批处理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: mouse, automation, advanced, control, desktop
tags:
- Automation
tools:
- read
- exec
---

# Control

**The most advanced desktop automation skill for Skill平台.** Provides pixel-perfect mouse control, lightning-fast keyboard input, screen capture, window management, and clipboard operations.

## 🎯 Features

### Mouse Control

* ✅ **Absolute positioning** - Move to exact coordinates
* ✅ **Relative movement** - Move from current position
* ✅ **Smooth movement** - Natural, human-like mouse paths
* ✅ **Click types** - Left, right, middle, double, triple clicks
* ✅ **Drag & drop** - Drag from point A to point B
* ✅ **Scroll** - Vertical and horizontal scrolling
* ✅ **Position tracking** - Get current mouse coordinates

### Keyboard Control

* ✅ **Text typing** - Fast, accurate text input
* ✅ **Hotkeys** - Execute keyboard shortcuts (Ctrl+C, Win+R, etc.)
* ✅ **Special keys** - Enter, Tab, Escape, Arrow keys, F-keys
* ✅ **Key combinations** - Multi-key press combinations
* ✅ **Hold & release** - Manual key state control
* ✅ **Typing speed** - Configurable WPM (instant to human-like)

### Screen Operations

* ✅ **Screenshot** - Capture entire screen or regions
* ✅ **Image recognition** - Find elements on screen (via OpenCV)
* ✅ **Color detection** - Get pixel colors at coordinates
* ✅ **Multi-monitor** - Support for multiple displays

### Window Management

* ✅ **Window list** - Get all open windows
* ✅ **Activate window** - Bring window to front
* ✅ **Window info** - Get position, size, title
* ✅ **Minimize/Maximize** - Control window states

### Safety Features

* ✅ **Failsafe** - Move mouse to corner to abort
* ✅ **Pause control** - Emergency stop mechanism
* ✅ **Approval mode** - Require confirmation for actions
* ✅ **Bounds checking** - Prevent out-of-screen operations
* ✅ **Logging** - Track all automation actions

---

## 🚀 Quick Start

### Installation

First, install required dependencies:

```bash
pip install pyautogui pillow opencv-python pygetwindow
```

### Basic Usage

```python
from skills.desktop_control import DesktopController

dc = DesktopController(failsafe=True)

dc.move_mouse(500, 300)  # Move to coordinates
dc.click()  # Left click at current position
dc.click(100, 200, button="right")  # Right click at position

dc.type_text("Hello from Skill平台!")
dc.hotkey("ctrl", "c")  # Copy
dc.press("enter")

screenshot = dc.screenshot()
position = dc.get_mouse_position()
```

---

## 📋 Complete API Reference

### Mouse Functions

#### `move_mouse(x, y, duration=0, smooth=True)`

Move mouse to absolute screen coordinates.

**Parameters:**

* `x` (int): X coordinate (pixels from left)
* `y` (int): Y coordinate (pixels from top)
* `duration` (float): Movement time in seconds (0 = instant, 0.5 = smooth)
* `smooth` (bool): Use bezier curve for natural movement

**Example:**

```python
dc.move_mouse(1000, 500)

dc.move_mouse(1000, 500, duration=1.0)
```

#### `move_relative(x_offset, y_offset, duration=0)`

Move mouse relative to current position.

**Parameters:**

* `x_offset` (int): Pixels to move horizontally (positive = right)
* `y_offset` (int): Pixels to move vertically (positive = down)
* `duration` (float): Movement time in seconds

**Example:**

```python
dc.move_relative(100, 50, duration=0.3)
```

#### `click(x=None, y=None, button='left', clicks=1, interval=0.1)`

Perform mouse click.

**Parameters:**

* `x, y` (int, optional): Coordinates to click (None = current position)
* `button` (str): 'left', 'right', 'middle'
* `clicks` (int): Number of clicks (1 = single, 2 = double)
* `interval` (float): Delay between multiple clicks

**Example:**

```python
dc.click()

dc.click(500, 300, clicks=2)

dc.click(button='right')
```

#### `drag(start_x, start_y, end_x, end_y, duration=0.5, button='left')`

Drag and drop operation.

**Parameters:**

* `start_x, start_y` (int): Starting coordinates
* `end_x, end_y` (int): Ending coordinates
* `duration` (float): Drag duration
* `button` (str): Mouse button to use

**Example:**

```python
dc.drag(100, 100, 500, 500, duration=1.0)
```

#### `scroll(clicks, direction='vertical', x=None, y=None)`

Scroll mouse wheel.

**Parameters:**

* `clicks` (int): Scroll amount (positive = up/left, negative = down/right)
* `direction` (str): 'vertical' or 'horizontal'
* `x, y` (int, optional): Position to scroll at

**Example:**

```python
dc.scroll(-5)

dc.scroll(10)

dc.scroll(5, direction='horizontal')
```

#### `get_mouse_position()`

Get current mouse coordinates.

**Returns:** `(x, y)` tuple

**Example:**

```python
x, y = dc.get_mouse_position()
print(f"Mouse is at: {x}, {y}")
```

---

### Keyboard Functions

#### `type_text(text, interval=0, wpm=None)`

Type text with configurable speed.

**Parameters:**

* `text` (str): Text to type
* `interval` (float): Delay between keystrokes (0 = instant)
* `wpm` (int, optional): Words per minute (overrides interval)

**Example:**

```python
dc.type_text("Hello World")

dc.type_text("Hello World", wpm=60)

dc.type_text("Hello World", interval=0.1)
```

#### `press(key, presses=1, interval=0.1)`

Press and release a key.

**Parameters:**

* `key` (str): Key name (see Key Names section)
* `presses` (int): Number of times to press
* `interval` (float): Delay between presses

**Example:**

```python
dc.press('enter')

dc.press('space', presses=3)

dc.press('down')
```

#### `hotkey(*keys, interval=0.05)`

Execute keyboard shortcut.

**Parameters:**

* `*keys` (str): Keys to press together
* `interval` (float): Delay between key presses

**Example:**

```python
dc.hotkey('ctrl', 'c')

dc.hotkey('ctrl', 'v')

dc.hotkey('win', 'r')

dc.hotkey('ctrl', 's')

dc.hotkey('ctrl', 'a')
```

#### `key_down(key)` / `key_up(key)`

Manually control key state.

**Example:**

```python
dc.key_down('shift')
dc.type_text("hello")  # Types "HELLO"
dc.key_up('shift')

dc.key_down('ctrl')
dc.click(100, 100)
dc.click(200, 100)
dc.key_up('ctrl')
```

---

### Screen Functions

#### `screenshot(region=None, filename=None)`

Capture screen or region.

**Parameters:**

* `region` (tuple, optional): (left, top, width, height) for partial capture
* `filename` (str, optional): Path to save image

**Returns:** PIL Image object

**Example:**

```python
img = dc.screenshot()

dc.screenshot(filename="screenshot.png")

img = dc.screenshot(region=(100, 100, 500, 300))
```

#### `get_pixel_color(x, y)`

Get color of pixel at coordinates.

**Returns:** RGB tuple `(r, g, b)`

**Example:**

```python
r, g, b = dc.get_pixel_color(500, 300)
print(f"Color at (500, 300): RGB({r}, {g}, {b})")
```

#### `find_on_screen(image_path, confidence=0.8)`

Find image on screen (requires OpenCV).

**Parameters:**

* `image_path` (str): Path to template image
* `confidence` (float): Match threshold (0-1)

**Returns:** `(x, y, width, height)` or None

**Example:**

```python
location = dc.find_on_screen("button.png")
if location:
    x, y, w, h = location
    # Click center of found image
    dc.click(x + w//2, y + h//2)
```

#### `get_screen_size()`

Get screen resolution.

**Returns:** `(width, height)` tuple

**Example:**

```python
width, height = dc.get_screen_size()
print(f"Screen: {width}x{height}")
```

---

### Window Functions

#### `get_all_windows()`

List all open windows.

**Returns:** List of window titles

**Example:**

```python
windows = dc.get_all_windows()
for title in windows:
    print(f"Window: {title}")
```

#### `activate_window(title_substring)`

Bring window to front by title.

**Parameters:**

* `title_substring` (str): Part of window title to match

**Example:**

```python
dc.activate_window("Chrome")

dc.activate_window("Visual Studio Code")
```

#### `get_active_window()`

Get currently focused window.

**Returns:** Window title (str)

**Example:**

```python
active = dc.get_active_window()
print(f"Active window: {active}")
```

---

### Clipboard Functions

#### `copy_to_clipboard(text)`

Copy text to clipboard.

**Example:**

```python
dc.copy_to_clipboard("Hello from Skill平台!")
```

#### `get_from_clipboard()`

Get text from clipboard.

**Returns:** str

**Example:**

```python
text = dc.get_from_clipboard()
print(f"Clipboard: {text}")
```

---

## ⌨️ Key Names Reference

### Alphabet Keys

`'a'` through `'z'`

### Number Keys

`'0'` through `'9'`

### Function Keys

`'f1'` through `'f24'`

### Special Keys

* `'enter'` / `'return'`
* `'esc'` / `'escape'`
* `'space'` / `'spacebar'`
* `'tab'`
* `'backspace'`
* `'delete'` / `'del'`
* `'insert'`
* `'home'`
* `'end'`
* `'pageup'` / `'pgup'`
* `'pagedown'` / `'pgdn'`

### Arrow Keys

* `'up'` / `'down'` / `'left'` / `'right'`

### Modifier Keys

* `'ctrl'` / `'control'`
* `'shift'`
* `'alt'`
* `'win'` / `'winleft'` / `'winright'`
* `'cmd'` / `'command'` (Mac)

### Lock Keys

* `'capslock'`
* `'numlock'`
* `'scrolllock'`

### Punctuation

* `'.'` / `','` / `'?'` / `'!'` / `';'` / `':'`
* `'['` / `']'` / `'{'` / `'}'`
* `'('` / `')'`
* `'+'` / `'-'` / `'*'` / `'/'` / `'='`

---

## 🛡️ Safety Features

### Failsafe Mode

Move mouse to **any corner** of the screen to abort all automation.

```python
dc = DesktopController(failsafe=True)
```

### Pause Control

```python
dc.pause(2.0)

if dc.is_safe():
    dc.click(500, 500)
```

### Approval Mode

Require user confirmation before actions:

```python
dc = DesktopController(require_approval=True)

dc.click(500, 500)  # Prompt: "Allow click at (500, 500)? [y/n]"
```

---

## 🎨 Advanced Examples

### Example 1: Automated Form Filling

```python
dc = DesktopController()

dc.click(300, 200)
dc.type_text("John Doe", wpm=80)

dc.press('tab')
dc.type_text("john@example.com", wpm=80)

dc.press('tab')
dc.type_text("SecurePassword123", wpm=60)

dc.press('enter')
```

### Example 2: Screenshot Region and Save

```python
region = (100, 100, 800, 600)  # left, top, width, height
img = dc.screenshot(region=region)

import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
img.save(f"capture_{timestamp}.png")
```

### Example 3: Multi-File Selection

```python
dc.key_down('ctrl')
dc.click(100, 200)  # First file
dc.click(100, 250)  # Second file
dc.click(100, 300)  # Third file
dc.key_up('ctrl')

dc.hotkey('ctrl', 'c')
```

### Example 4: Window Automation

```python
dc.activate_window("Calculator")
time.sleep(0.5)

dc.type_text("5+3=", interval=0.2)
time.sleep(0.5)

dc.screenshot(filename="calculation_result.png")
```

### Example 5: Drag & Drop File

```python
dc.drag(
    start_x=200, start_y=300,  # File location
    end_x=800, end_y=500,       # Folder location
    duration=1.0                 # Smooth 1-second drag
)
```

---

## ⚡ Performance Tips

1. **Use instant movements** for speed: `duration=0`
2. **Batch operations** instead of individual calls
3. **Cache screen positions** instead of recalculating
4. **Disable failsafe** for maximum performance (use with caution)
5. **Use hotkeys** instead of menu navigation

---

## ⚠️ Important Notes

* **Screen coordinates** start at (0, 0) in top-left corner
* **Multi-monitor setups** may have negative coordinates for secondary displays
* **Windows DPI scaling** may affect coordinate accuracy
* **Failsafe corners** are: (0,0), (width-1, 0), (0, height-1), (width-1, height-1)
* **Some applications** may block simulated input (games, secure apps)

---

## 🔧 Troubleshooting

### Mouse not moving to correct position

* Check DPI scaling settings
* Verify screen resolution matches expectations
* Use `get_screen_size()` to confirm dimensions

### Keyboard input not working

* Ensure target application has focus
* Some apps require admin privileges
* Try increasing `interval` for reliability

### Failsafe triggering accidentally

* Increase screen border tolerance
* Move mouse away from corners during normal use
* Disable if needed: `DesktopController(failsafe=False)`

### Permission errors

* Run Python with administrator privileges for some operations
* Some secure applications block automation

---

## 📦 Dependencies

* **PyAutoGUI** - Core automation engine
* **Pillow** - Image processing
* **OpenCV** (optional) - Image recognition
* **PyGetWindow** - Window management

Install all:

```bash
pip install pyautogui pillow opencv-python pygetwindow
```

---

**Built for Skill平台** - The ultimate desktop automation companion 🦞

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
