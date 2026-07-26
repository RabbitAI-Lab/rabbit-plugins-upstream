# Desktop Control — Windows 桌面控制 Skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Windows](https://img.shields.io/badge/OS-Windows%2010%2F11-blue)]()

> **⚠️ 重要免责声明**
> 本技能赋予 AI 代理控制鼠标、键盘、屏幕截图的完整能力。
> **仅限以下场景使用：**
> - 您自己的个人电脑，且是您主动授权的操作
> - 网关绑定 `127.0.0.1`（仅本地访问）
> - 可信的本地环境
>
> **严禁用于：**
> - 未经授权的设备操控
> - 恶意攻击、批量作弊、自动化攻击
> - 任何违反法律法规的行为
>
> 作者不对因滥用本技能产生的任何法律责任负责。

> **🔒 隐私承诺**
> - 所有操作**完全在本地执行**
> - **完全离线可用**，无需互联网连接
> - **无任何数据上传**到外部服务器
> - **无遥测、无日志上传、无后台心跳**
> - 截屏数据仅保存在本地临时目录
> - 键盘输入**不记录或不外发**
> - **抓包验证**：运行期间零网络请求
> - 只有你自己能看到你的桌面

Industrial-grade Windows desktop automation for OpenClaw agents.

## 🏗 Architecture

```
OpenClaw Agent
    │
    ├─ client.py (IPC, ~80 lines)
    │     └─ auto-starts daemon on first use
    │           └─ named pipe (message mode, user-SID locked)
    │                 └─ Daemon Process (stays in memory)
    │                       ├─ SendInput (mouse/keyboard)
    │                       ├─ mss (screenshots)
    │                       ├─ win32gui (windows)
    │                       └─ pywinauto (UIA, STA thread pool)
```

Key design:
- **常驻守护进程**：首次调用启动，后续 <100ms 响应，无重复 Python 加载
- **原生 Win32 输入**：`SendInput` via ctypes，非 pyautogui 的已弃用 API
- **Unicode 安全**：`KEYEVENTF_UNICODE` 模式，不污染剪贴板
- **STA 线程池**：UIA 操作在独立 COM 线程运行
- **命名管道权限隔离**：管道名含用户 SID + 会话 ID，禁止跨用户访问

## 📦 前置要求

- **操作系统**：Windows 10 或 11
- **Python**：3.9+ 和 pip（技能依赖 Python 运行环境）
- **运行模式**：控制台会话（RDP 断开时无法显示窗口）

> 注：绝大多数桌面操作只需普通用户权限。仅当需要操控管理员级窗口（如任务管理器、UAC 弹窗）时，才需要以管理员身份运行网关。

## 📥 安装

```powershell
# 1. 安装技能
openclaw skills install @sunsettide/desktop-control

# 2. 安装 Python 依赖
cd skills/desktop-control
pip install -r requirements.txt

# 或者用安装脚本（建议先检查脚本内容）
# pip install -r requirements.txt
# 脚本仅执行 pip install -r requirements.txt
```

## 🚀 Quick Start

```bash
# 守护进程自动启动。直接调用任何命令：

# 移动鼠标
python client/client.py mouse_move '{"x": 500, "y": 300}'

# 截图
python client/client.py screenshot '{"format": "b64"}'

# 列出窗口
python client/client.py window_list '{}'
```

## 📋 API 方法一览

| 类别 | 方法 | 说明 |
|:-----|:-----|:------|
| 🖱️ 鼠标 | `mouse_move` / `mouse_click` / `mouse_drag` / `mouse_scroll` / `mouse_position` | 移动/点击/拖拽/滚轮/定位；支持 `monitor` 参数多显示器锚定 |
| ⌨️ 键盘 | `keyboard_type` / `keyboard_press` / `keyboard_hotkey` | Unicode 输入/单键/快捷键 |
| 📸 截图/像素 | `screenshot` / `screenshot_save` / `pixel_color` | base64 或文件模式；支持 `region` 截取指定区域；支持 `monitor` 多显示器锚定；`pixel_color` 获取单点颜色 |
| 🪟 窗口 | `window_list` / `window_focus` / `window_close` / `window_move` / `window_resize` / `window_minimize` / `window_maximize` / `window_info` / `window_set_topmost` | 枚举/激活/关闭/移动/缩放/置顶 |
| 🔍 UIA | `uia_find` / `uia_click` / `uia_get_text` | 元素查找/点击/文本读取 |
| 📁 文件 | `file_drag_drop` | 文件拖拽到指定窗口（基于剪贴板粘贴，无 COM 依赖） |
| 👁️ OCR | `screen_ocr` | 屏幕区域文字识别（需安装 Tesseract） |
| 🔥 全局热键 | `register_hotkey` / `unregister_hotkey` / `list_hotkeys` | 注册/注销/列举全局热键（后台消息泵 + 线程池执行） |
| 👁️ 图像匹配 | `image_find` | 模板图像匹配定位（CV2 TM_CCOEFF_NORMED，可选依赖） |
| 🎬 宏录制 | `macro_start_recording` / `macro_stop_recording` / `macro_playback` | 录制鼠标/键盘操作并回放（pynput 可选依赖） |
| 🧩 多会话 | `session_create` / `session_switch` / `session_list` / `session_destroy` | 独立操作上下文（monitor、变量、焦点） |
| 📜 脚本编排 | `script_run` | 声明式自动化脚本（支持条件、循环、重试、变量） |
| 👁️ 窗口感知 | `get_active_window` / `window_get_context` | 获取前台窗口信息 / UIA 控件树（2 层深度，1 秒超时） |
| ⚙️ 守护进程 | `ping` / `daemon_status` / `daemon_shutdown` / `refresh_monitors` | 健康检查/状态/关闭/刷新显示器列表 |

## 🔒 安全机制

- **命名管道权限**：管道名包含用户 SID + 会话 ID，仅当前用户可连接
- **输入边界**：坐标范围校验、按键白名单、单条指令长度限制
- **最小权限**：普通场景用户权限即可运行；仅为高权限窗口场景才需管理员
- **操作日志**：本地记录指令类型和执行时间（不记录敏感输入）
- **频率控制**：内置操作频率上限，防止滥用
- **无外联**：零网络请求，零遥测

## 🧪 测试

```bash
# 完整集成测试
python tests/test_all.py

# UIA 专项测试（启动记事本 → 读取/编辑/关闭）
python tests/test_uia.py
```

## 使用建议
- **单次文本输入建议不超过 4000 字符**，超长输入会被 SendInput 逐字符发送，耗时较长
- 大量文本建议拆分为多次 `keyboard_type` 调用

## ⚠️ 已知限制

| 限制 | 说明 |
|:-----|:------|
| **UIPI** | 管理员级窗口无法被普通用户权限的输入模拟操控；需以管理员身份运行守护进程 |
| **Python 依赖** | 需要 Python 3.9+ |
| **冷启动** | 首次调用需 2-10 秒（加载 pywinauto） |
| **DirectInput** | 部分游戏使用 DirectInput，SendInput 无法注入 |
| **远程桌面** | RDP 断开后窗口截图可能为黑屏 |
| **无沙箱隔离** | 技能直接在宿主机桌面运行 |

## 安全审计

本技能已通过 ClawHub VirusTotal 扫描（64/64 厂商标记为清洁）和 SkillSpector 静态分析，未检测到恶意模式。

## 📄 License

MIT License. See [LICENSE](LICENSE).

---

_Built for OpenClaw 🦞_
