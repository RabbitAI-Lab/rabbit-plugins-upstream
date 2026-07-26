---
name: desktop-control
description: "Windows 桌面控制工具 (從Windows) - 截屏、窗口管理、鼠标键盘控制、进程管理、系统信息。当用户要求截屏、查看进程、关闭程序、桌面控制时使用此技能。"
version: 1.1.3
user-invocable: true
metadata:
  openclaw:
    requires:
      bins:
        - python
        - pip
    install:
      - kind: pip
        package: -r requirements.txt
        bins: [python]
    os:
      - win32
    emoji: "🖥️"
    homepage: https://github.com/sunsettide/desktop-control
---

# desktop-control 桌面控制

Windows 桌面守护进程，通过命名管道提供键鼠操控、屏幕截图、窗口管理、OCR 识别、UIA 自动化等能力。
所有操作在本地执行，零网络外发。

## 前置依赖

- **操作系统**: Windows 10/11
- **Python**: 3.9+
- 首次使用会自动运行 `pip install -r {baseDir}/requirements.txt`

## 如何使用

守护进程会在首次调用时自动启动。对任意客户端工具（如 `exec`、`python`）调用：

```
python {baseDir}/client/client.py <method> '<JSON params>'
```

### 基本鼠标操作

当用户需要移动鼠标或点击时：

```bash
# 鼠标移动到绝对坐标（支持平滑贝塞尔曲线）
python {baseDir}/client/client.py mouse_move '{"x": 500, "y": 300, "duration": 0.3, "curve": "bezier"}'

# 相对移动
python {baseDir}/client/client.py mouse_move_relative '{"dx": 100, "dy": 0}'

# 点击（拆分 down/up 支持拖拽）
python {baseDir}/client/client.py mouse_click '{"button": "left"}'
python {baseDir}/client/client.py mouse_down '{"button": "left"}'
python {baseDir}/client/client.py mouse_up '{"button": "left"}'
```

### 键盘输入

```bash
# 英文/数字输入
python {baseDir}/client/client.py keyboard_type '{"text": "Hello World"}'

# 中文输入 (IME Safe — 自动剪贴板绕过输入法)
python {baseDir}/client/client.py keyboard_type '{"text": "你好世界"}'

# 快捷键
python {baseDir}/client/client.py keyboard_hotkey '{"keys": ["ctrl", "c"]}'
```

### 屏幕截图与 OCR

```bash
# 截屏
python {baseDir}/client/client.py screenshot_save '{"path": "C:\\temp\\shot.png"}'

# 文字定位
python {baseDir}/client/client.py find_text '{"text": "确定", "region": {"left": 0, "top": 0, "width": 800, "height": 600}}'

# 点击文字（自动定位+点击）
python {baseDir}/client/client.py click_text '{"text": "7"}'

# 锚点输入（在文字附近输入）
python {baseDir}/client/client.py type_to_text '{"text": "用户名", "input": "admin", "anchor": "below"}'
```

### 窗口管理

```bash
# 列举所有窗口
python {baseDir}/client/client.py window_list '{}'

# 聚焦某个窗口
python {baseDir}/client/client.py window_focus '{"title": "记事本"}'
```

### 脚本编排

多步操作可以写成 JSON 脚本执行：

```bash
python {baseDir}/client/client.py script_run '{"script": {"steps": [
  {"action": "window_focus", "params": {"title": "记事本"}},
  {"action": "keyboard_type", "params": {"text": "Hello World"}},
  {"action": "screenshot_save", "params": {"path": "C:\\temp\\shot.png"}}
]}}'
```

### AI 代理集成 (Function Calling)

调用 `tools_list` 获取所有可用工具的 OpenAI Function Calling 声明：

```bash
python {baseDir}/client/client.py tools_list '{}'
```

返回 ~17 个工具（`click_text`、`find_text`、`keyboard_type` 等），
可直接用于 LLM Function Calling / Tool Use。

### 一句话自动化

```bash
python {baseDir}/client/client.py goal_run '{"goal": "打开记事本，输入 Hello World，截图保存", "confirm": true}'
```

## 完整方法列表

| 分类 | 方法 | 说明 |
|:---|:---|:---|
| 鼠标 | `mouse_move` | 绝对移动（支持 duration + bezier + tremor） |
| 鼠标 | `mouse_move_relative` | 相对移动 |
| 鼠标 | `mouse_click` | 点击（支持 text 参数字段自动路由到 click_text） |
| 鼠标 | `mouse_down` / `mouse_up` | 拆分按键（支持拖拽选择） |
| 鼠标 | `mouse_scroll` | 滚轮（支持 random_variance） |
| 鼠标 | `mouse_drag` | 拖拽 |
| 鼠标 | `mouse_get_position` | 获取位置（含所在显示器索引） |
| 键盘 | `keyboard_type` | 文本输入（含 IME Safe、delay 区间、pressure） |
| 键盘 | `keyboard_press` / `keyboard_down` / `keyboard_up` | 按键操作 |
| 键盘 | `keyboard_hotkey` | 快捷键（支持 hold_duration） |
| 剪贴板 | `clipboard_get` / `clipboard_set` | 显式剪贴板操作 |
| 截图 | `screenshot` / `screenshot_save` | 截图（支持 region 和 monitor） |
| 截图 | `pixel_color` | 取色 |
| 窗口 | `window_list` / `window_focus` / `window_info` | 窗口枚举、聚焦、信息 |
| 窗口 | `window_close` / `window_minimize` / `window_maximize` / `window_move` / `window_resize` / `window_set_topmost` | 窗口操控 |
| UIA | `uia_find` / `uia_click` / `uia_get_text` | UI 自动化 |
| OCR | `screen_ocr` | 屏幕文字识别 |
| OCR | `find_text` / `click_text` / `type_to_text` | 文字定位/点击/锚点输入 |
| OCR | `screen_context` | 屏幕文字摘要（适合 AI 决策） |
| 图像 | `image_find` | 图像模板匹配 |
| 文件 | `file_drag_drop` | 文件拖放 |
| 会话 | `session_create` / `session_switch` / `session_list` / `session_destroy` | 多会话管理 |
| 脚本 | `script_run` / `script_run_sync` | 脚本执行 |
| 脚本 | `script_status` / `script_results` / `script_cancel` | 异步脚本管理 |
| 脚本 | `script_generate` / `script_generate_and_run` | 自然语言→脚本生成 |
| 脚本 | `script_list_templates` / `script_load_template` | 脚本模板库 |
| 热键 | `register_hotkey` / `unregister_hotkey` / `list_hotkeys` | 全局快捷键 |
| 宏 | `macro_start_recording` / `macro_stop_recording` / `macro_playback` | 宏录制回放 |
| AI | `tools_list` / `tools_call` | Function Calling 工具层 |
| AI | `goal_run` | 目标驱动自动化 |
| 系统 | `ping` / `daemon_status` / `daemon_shutdown` | 守护进程管理 |
| 系统 | `refresh_monitors` | 显示器热插拔刷新 |
| 系统 | `get_active_window` / `window_get_context` | 活动窗口/UIA 上下文 |
| 系统 | `human` 参数（所有键鼠操作） | 拟人化自动感知（浏览器→light/heavy） |

## 安全机制

- 所有操作在本地执行，零网络外发
- 命名管道 DACL 限制为当前用户，禁止 SYSTEM 连接
- 审计日志对 `text`/`password` 字段脱敏
- 鼠标安全边界校验（防止坐标越界）
- 输入超时自动释放（5 秒无响应自动释放卡住按键）
- 操作频率限制（120 次/10秒）
- 可选确认模式（`require_approval=True`）
