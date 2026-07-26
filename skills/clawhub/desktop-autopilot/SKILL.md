---
slug: desktop-autopilot
name: desktop-autopilot
version: "1.0.0"
displayName: 桌面自动驾驶
summary: 智能桌面 GUI 自动化，视觉识别定位、智能等待、工作流编排，DPI 自适应不迷路。
license: MIT
description: |-
  桌面自动驾驶为 AI Agent 提供基于视觉的智能 GUI 自动化能力。它不依赖固定坐标，而是通过图像识别、OCR 文本定位、智能等待元素出现来操控界面，内置工作流编排、录制回放、DPI 自适应与多显示器支持，让自动化脚本像人一样"看着屏幕操作"。

  核心能力：视觉元素定位（图像匹配+OCR）、智能等待（等元素出现/消失）、工作流编排（步骤序列+条件分支）、录制回放、DPI 自适应坐标转换、多显示器管理、安全护栏（确认模式+操作日志+回滚快照）。

  适用场景：表单自动填写、数据录入、应用间数据搬运、UI 回归测试、重复性操作自动化、一人公司省人力。

  差异化：相比仅暴露原始鼠标键盘 API 的方案，本技能新增视觉优先定位（先找图/找字再点击，而非盲点坐标）、智能等待（轮询元素出现，不再硬编码 sleep）、工作流编排（把多步操作封装为可重放流程）、DPI 自适应（自动校正缩放导致的坐标偏移）、操作快照回滚（危险操作前截图，出错可参照）。定位为"自动驾驶层"，与系统控制器（系统层进程/文件）明确分工。

  触发关键词：桌面自动化, GUI, 鼠标, 键盘, 截图, 图像识别, 表单填写, 自动驾驶, desktop, mouse, keyboard, screenshot, OCR, autopilot
tags:
- 自动化
- 桌面自动化
- 视觉识别
tools:
- read
- exec
---

# 桌面自动驾驶

让 AI Agent 像人一样"看着屏幕操作"，而不是盲点坐标。本技能解决五个核心痛点：**坐标漂移**（DPI 缩放、窗口移动导致固定坐标失效）、**时机不对**（元素没加载就点击）、**识别率低**（原始 locateOnScreen 效果差）、**操作不可逆**（点错了无法回退）、**流程难复用**（每次重写脚本）。

## 职责边界

本技能聚焦 **GUI 层**自动化，与系统控制器（系统层）明确分工：

| 本技能负责 | 系统控制器负责 |
|:-----------|:---------------|
| 鼠标点击与移动 | 进程/服务管理 |
| 键盘输入与快捷键 | 文件系统操作 |
| 屏幕截图与图像识别 | 环境变量/注册表 |
| 窗口管理（GUI 层） | 计划任务（系统级） |
| GUI 工作流编排 | 系统资源监控 |

## 核心理念：视觉优先

**铁律**：优先用"找图/找字"定位元素，最后才用固定坐标。坐标会因 DPI、窗口位置、分辨率而漂移，图像识别不会。

```python
# 错误：盲点坐标（DPI 一变就错）
dc.click(500, 300)

# 正确：找图后点击中心
location = dc.find_on_screen("submit_button.png")
if location:
    dc.click_center(location)

# 更好：找文字（OCR）
location = dc.find_text("提交")
if location:
    dc.click_center(location)
```

## 快速开始

### 安装依赖

```bash
pip install pyautogui pillow opencv-python pygetwindow pytesseract
# OCR 还需安装 Tesseract: https://github.com/tesseract-ocr/tesseract
```

### 视觉优先的基本流程

```python
from desktop_autopilot import Autopilot

ap = Autopilot(failsafe=True, dpi_aware=True)

# 1. 智能等待元素出现（不硬编码 sleep）
ap.wait_for_image("login_button.png", timeout=10)

# 2. 找到并点击
ap.click_image("login_button.png")

# 3. 等输入框出现，输入文本
ap.wait_for_image("username_field.png", timeout=5)
ap.click_image("username_field.png")
ap.type_text("john@example.com")

# 4. 截图保存结果
ap.screenshot("after_login.png")
```

## 智能等待（核心差异化）

原始方案用 `time.sleep(2)` 硬等，慢且不可靠。本技能提供智能等待：

### wait_for_image - 等图像出现

```python
ap.wait_for_image(
    "submit_button.png",
    timeout=10,        # 最长等 10 秒
    interval=0.5,      # 每 0.5 秒检查一次
    confidence=0.8     # 匹配置信度
)
# 返回 True/False，找到立即返回不等满 timeout
```

### wait_for_text - 等文字出现（OCR）

```python
ap.wait_for_text("登录成功", timeout=10)
```

### wait_for_image_gone - 等图像消失

```python
# 等加载动画消失，表示加载完成
ap.wait_for_image_gone("loading_spinner.png", timeout=30)
```

### wait_for_color - 等颜色变化

```python
# 等某点变成绿色（表示成功）
ap.wait_for_color(500, 300, (0, 200, 0), timeout=10)
```

### 组合等待模式

```python
# 等元素出现 OR 超时（任一先满足）
ap.wait_any(
    lambda: ap.find_image("success.png"),
    lambda: ap.find_image("error.png"),
    timeout=15
)
```

## 视觉定位（核心差异化）

### find_image - 多尺度图像匹配

原始 `locateOnScreen` 只做单尺度匹配，DPI 变化就找不到。本技能做多尺度：

```python
location = ap.find_image(
    "button.png",
    confidence=0.8,
    multiscale=True,     # 多尺度匹配（抗 DPI）
    grayscale=True       # 灰度匹配（加速）
)
# 返回 (x, y, w, h) 或 None
```

### find_text - OCR 文字定位

```python
location = ap.find_text("提交订单")
if location:
    ap.click_center(location)
```

### find_all - 找所有匹配

```python
# 找所有"删除"按钮
buttons = ap.find_all_images("delete_icon.png")
for btn in buttons:
    ap.click_center(btn)
```

### click_image - 找图并点击（一步到位）

```python
ap.click_image("save_button.png", confidence=0.85)
# 等价于 find_image + click_center
```

### 坐标系与 click_center

```python
def click_center(self, location):
    """location 是 (x, y, w, h)，点击中心点"""
    x, y, w, h = location
    self.click(x + w//2, y + h//2)
```

## DPI 自适应（核心差异化）

Windows DPI 缩放（125%/150%）是坐标漂移的首要原因。本技能自动处理：

```python
ap = Autopilot(dpi_aware=True)
# 内部自动:
# 1. 读取系统 DPI 缩放比例
# 2. 截图前校正坐标到物理像素
# 3. 图像匹配用物理像素
```

```python
# 手动查询当前 DPI
scale = ap.get_dpi_scale()  # 返回 1.0 / 1.25 / 1.5 等
print(f"当前 DPI 缩放: {scale*100}%")
```

## 鼠标控制

```python
ap.move_mouse(x, y, duration=0, smooth=True)  # 移动到绝对坐标
ap.move_relative(dx, dy)                       # 相对移动
ap.click(x, y, button='left', clicks=1)        # 点击
ap.click(button='right')                       # 右键
ap.double_click(x, y)                          # 双击
ap.drag(x1, y1, x2, y2, duration=0.5)          # 拖拽
ap.scroll(-5)                                  # 滚动（负=向下）
ap.get_mouse_position()                        # 获取当前位置
```

## 键盘控制

```python
ap.type_text("Hello", interval=0, wpm=None)    # 输入文本
ap.press('enter')                               # 单键
ap.press('tab', presses=3)                      # 多次按键
ap.hotkey('ctrl', 'c')                          # 快捷键
ap.key_down('shift')                            # 按住
ap.key_up('shift')                              # 释放
```

### 键名速查

| 类别 | 键名 |
|:-----|:-----|
| 字母数字 | `'a'`-`'z'`, `'0'`-`'9'` |
| 功能键 | `'f1'`-`'f24'` |
| 特殊键 | `enter`/`esc`/`space`/`tab`/`backspace`/`delete`/`home`/`end`/`pageup`/`pagedown` |
| 方向键 | `up`/`down`/`left`/`right` |
| 修饰键 | `ctrl`/`shift`/`alt`/`win`/`cmd` |
| 标点 | `.`/`,`/`?`/`!`/`;`/`:`/`[`/`]`/`{`/`}`/`(`/`)`/`+`/`-`/`*`/`/`/`=` |

## 屏幕操作

```python
ap.screenshot()                          # 全屏截图，返回 Image
ap.screenshot(region=(x,y,w,h))         # 区域截图
ap.screenshot(filename="cap.png")       # 保存到文件
ap.get_pixel_color(x, y)                # 取色 (r,g,b)
ap.get_screen_size()                    # 屏幕分辨率 (w,h)
```

## 窗口管理

```python
ap.get_all_windows()                    # 列出所有窗口
ap.activate_window("Chrome")            # 按标题激活
ap.get_active_window()                  # 当前焦点窗口
ap.minimize_window("Calculator")        # 最小化
ap.maximize_window("Calculator")        # 最大化
ap.get_window_rect("Chrome")            # 窗口位置与大小
```

## 工作流编排（核心差异化）

把多步操作封装为可重放的工作流：

```python
# 定义工作流
wf = ap.workflow("fill-form")

wf.step("等待表单加载", lambda: ap.wait_for_image("form.png", timeout=10))
wf.step("填写姓名", lambda: (ap.click_image("name_field.png"), ap.type_text("张三")))
wf.step("填写邮箱", lambda: (ap.click_image("email_field.png"), ap.type_text("z@x.com")))
wf.step("提交", lambda: ap.click_image("submit.png"))
wf.step("等待成功", lambda: ap.wait_for_text("提交成功", timeout=10), critical=True)

# 执行（带断点恢复）
wf.run()
```

### 条件分支

```python
wf = ap.workflow("smart-login")

wf.step("找登录按钮", lambda: ap.find_image("login_btn.png"))
wf.branch(
    condition=lambda result: result is not None,
    steps=[
        ("点击登录", lambda: ap.click_image("login_btn.png")),
        ("输入凭据", lambda: (ap.click_image("user.png"), ap.type_text("john")))
    ],
    else_steps=[
        ("可能已登录，找首页", lambda: ap.wait_for_image("home.png", timeout=5))
    ]
)
```

### 工作流持久化与回放

```python
# 保存工作流
wf.save("workflows/fill-form.json")

# 加载并回放
wf2 = ap.load_workflow("workflows/fill-form.json")
wf2.run()
```

## 录制回放（核心差异化）

手动操作一次，录制后无限回放：

```python
# 开始录制
ap.record_start("data-entry")

# ... 用户手动操作（鼠标点击、键盘输入被记录）...

# 停止录制
ap.record_stop()
# 自动保存到 recordings/data-entry.json

# 回放（带视觉校验）
ap.playback("data-entry", verify=True)
# verify=True 时每步回放前截图校验，不匹配则暂停
```

## 安全护栏（核心差异化）

### 操作快照回滚

危险操作前自动截图，出错可参照：

```python
ap.snapshot("before-form-submit")  # 截图存档
ap.click_image("submit.png")
if not ap.wait_for_text("成功", timeout=5):
    ap.show_snapshot("before-form-submit")  # 展示操作前状态
    ap.alert("提交可能失败，请检查")
```

### 确认模式

```python
ap = Autopilot(require_approval=True)
ap.click(500, 300)  # 弹窗确认："允许点击 (500,300)? [y/n]"
```

### Failsafe（急停）

鼠标移到屏幕任一角落立即中止所有自动化：

```python
ap = Autopilot(failsafe=True)
# 角落坐标: (0,0), (w-1,0), (0,h-1), (w-1,h-1)
```

### 操作日志

所有操作自动记录到 `~/.skill-platform/autopilot/logs/`：

```
2026-07-18T09:00:00Z | click_image | submit.png | SUCCESS | (520, 340)
2026-07-18T09:00:02Z | type_text | john@example.com | SUCCESS
2026-07-18T09:00:05Z | wait_for_text | 提交成功 | TIMEOUT | 等待10秒未出现
```

## 场景化指南

### 场景 A：表单自动填写

```python
ap = Autopilot(dpi_aware=True)
ap.snapshot("before")

ap.wait_for_image("name_field.png", timeout=10)
ap.click_image("name_field.png")
ap.type_text("张三")

ap.press('tab')
ap.type_text("zhang@example.com")

ap.press('tab')
ap.type_text("13800138000")

ap.click_image("submit.png")
ap.wait_for_text("提交成功", timeout=10) or ap.show_snapshot("before")
```

### 场景 B：应用间数据搬运

```python
# 从 Excel 复制数据到 CRM
ap.activate_window("Excel")
ap.hotkey('ctrl', 'c')  # 假设已选中

ap.activate_window("CRM")
ap.wait_for_image("crm_input.png", timeout=10)
ap.click_image("crm_input.png")
ap.hotkey('ctrl', 'v')
ap.click_image("save.png")
```

### 场景 C：UI 回归测试

```python
# 工作流：登录→操作→验证
wf = ap.workflow("login-test")
wf.step("打开登录页", open_login_page)
wf.step("输入凭据", enter_credentials, critical=True)
wf.step("提交", click_submit)
wf.step("验证首页", lambda: ap.wait_for_image("home.png", timeout=10), critical=True)
result = wf.run()
print("测试结果:", "PASS" if result.success else "FAIL")
```

### 场景 D：多文件批量处理

```python
ap.key_down('ctrl')
for file_pos in [(100, 200), (100, 250), (100, 300)]:
    ap.click(*file_pos)
ap.key_up('ctrl')
ap.hotkey('ctrl', 'c')
# 切到目标文件夹
ap.activate_window("目标文件夹")
ap.hotkey('ctrl', 'v')
```

## FAQ

**Q：图像识别找不到元素怎么办？**
A：① 提高置信度容差 `confidence=0.7`；② 开启 `multiscale=True` 抗 DPI；③ 改用 OCR `find_text`；④ 检查截图模板是否过期（UI 改版后需更新模板）。

**Q：DPI 缩放导致坐标偏移？**
A：用 `dpi_aware=True` 初始化，本技能自动校正。或优先用图像/文字定位，避免硬坐标。

**Q：多显示器负坐标怎么处理？**
A：副显示器在主显示器左侧/上方时坐标为负。`get_screen_size()` 只返回主屏，用 `get_all_monitors()` 获取全部。图像定位不受影响（全屏搜索）。

**Q：某些应用屏蔽了模拟输入？**
A：游戏和部分安全应用（如银行 U 盾）会屏蔽 SendInput。可尝试以管理员权限运行，或改用应用本身的 API/CLI。

**Q：录制回放可靠吗？**
A：`verify=True` 时每步回放前截图校验，UI 变化会暂停等人工介入。纯坐标回放不可靠，建议结合视觉校验。

**Q：和系统控制器怎么配合？**
A：本技能管 GUI 操作（点击、输入、截图），系统控制器管系统操作（进程、文件、服务）。如"启动应用"用系统控制器，"在应用里填表"用本技能。

## 故障排查

| 症状 | 可能原因 | 处置 |
|:-----|:---------|:-----|
| 图像找不到 | DPI 缩放/UI 改版 | `multiscale=True`，更新模板图 |
| 坐标点击偏移 | DPI 未校正 | `dpi_aware=True` |
| 键盘输入无效 | 目标窗口失焦 | 先 `activate_window` 再输入 |
| 操作过快出错 | 元素未加载 | 用 `wait_for_image` 替代 sleep |
| Failsafe 误触发 | 鼠标靠近角落 | 调大角落容差或关闭（慎用） |
| OCR 识别差 | Tesseract 未装/语言包缺 | 安装 Tesseract + 中文语言包 |
| 多显示器坐标乱 | 副屏负坐标 | 用图像定位避免坐标问题 |

## 性能优化

1. **灰度匹配**：`grayscale=True` 提速 3 倍，多数场景够用。
2. **区域限定**：`find_image(region=(x,y,w,h))` 只搜指定区域，大幅加速。
3. **缓存模板**：重复使用的模板图预加载，避免每次读盘。
4. **智能等待早返回**：`wait_for_image` 找到立即返回，不硬等满 timeout。
5. **批量操作**：用工作流编排批量执行，减少单次调用开销。

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 的任意 AI Agent
- **操作系统**：Windows / macOS / Linux（需图形界面）
- **Python**：3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| PyAutoGUI | Python 包 | 必需 | `pip install pyautogui` |
| Pillow | Python 包 | 必需 | `pip install pillow` |
| OpenCV (opencv-python) | Python 包 | 必需（图像识别） | `pip install opencv-python` |
| PyGetWindow | Python 包 | 必需（窗口管理） | `pip install pygetwindow` |
| pytesseract | Python 包 | 可选（OCR） | `pip install pytesseract` |
| Tesseract OCR | 系统程序 | OCR 必需 | 官方安装 + 中文语言包 |
| NumPy | Python 包 | 推荐（多尺度匹配） | `pip install numpy` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本技能为本地桌面操作，无需外部 API Key。
- OCR 功能需本地安装 Tesseract，无需 Key。
- 部分应用自动化可能需要管理员权限。

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + Python 执行）
- **说明**：Agent 通过 Python API 驱动 GUI 自动化，本技能提供视觉定位、智能等待与工作流编排，实际操作通过 PyAutoGUI/OpenCV 执行。
