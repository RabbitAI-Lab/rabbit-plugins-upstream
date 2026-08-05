---
name: "watchitai"
version: "2.1.0"
description: "Cross-platform screen sharing, remote desktop control, and real-time monitoring for AI agents. View and control your computer screen from any phone or browser via WebRTC P2P. Supports Windows, macOS, and Linux. No Node.js required — self-contained Go binaries."
author: "WatchItAI"
tags: "screen-sharing,remote-control,remote-desktop,webrtc,p2p,monitoring,ai-agent,desktop-control,screen-capture,mouse-control,keyboard-control,openclaw,claude-code,cursor,trae,accessibility"
---

# WatchItAI Skill

跨平台屏幕共享与远程控制技能，支持 Windows、macOS 和 Linux。

通过对话即可启动屏幕共享，生成会话链接，你可以在远端手机浏览器中查看并远程控制电脑屏幕。

## 何时使用

当用户提到以下内容时，自动使用此技能：
- "分享屏幕"、"屏幕共享"、"共享我的屏幕"
- "远程控制"、"帮我操作电脑"
- "远程查看电脑"、"用手机看电脑"
- "watchitai share"、"启动 watchitai"

## 快速开始

### 启动屏幕共享

直接运行分享命令（无需 Node.js，使用自包含 Go 二进制）：

**macOS / Linux：**
```bash
bash run.sh share
```

**Windows：**
```cmd
run.cmd share
```

启动后会自动在浏览器中打开本地主机页面（`http://localhost:8765/`），点击"开始共享"即可生成会话链接，在远端手机浏览器中打开该链接即可查看屏幕。

支持参数：

**macOS / Linux：**
```bash
bash run.sh share --duration 60 --permission control --audio --auto-start
```

**Windows：**
```cmd
run.cmd share --duration 60 --permission control --audio --auto-start
```

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--duration <min>` | 会话时长（分钟） | 30 |
| `--permission <view\|control>` | 远端权限 | view |
| `--audio` | 共享音频 | 关闭 |
| `--auto-start` | 自动开始共享 | 关闭 |
| `--no-preflight` | 跳过权限预检 | 关闭 |

### 通过 AI 工具启动（获取监控链接）

在 OpenClaw / Trae / WorkBuddy 等 AI 工具中，使用 `link` 命令创建会话并获取监控链接：

**macOS / Linux：**
```bash
bash run.sh link --duration 30 --permission control
```

**Windows：**
```cmd
run.cmd link --duration 30 --permission control
```

该命令会：
1. 启动本地桥接服务
2. 通过 API 创建共享会话
3. 自动打开本地主机页面并开始共享
4. 输出监控链接供 AI 工具展示给用户

**重要：AI 工具输出格式要求**

命令输出中包含 `__WATCHITAI_LINK__` 标记行，AI 工具必须从该标记行提取 URL，并以 markdown 超链接形式呈现给用户，**不要**以纯文本或代码块形式展示链接。

输出示例：
```
✅ 屏幕共享会话已创建！

🔗 会话链接（在远端设备打开）:
   https://watchitai.net/s/abc123?token=xxx
__WATCHITAI_LINK__https://watchitai.net/s/abc123?token=xxx
```

AI 工具应将链接呈现为：

> ✅ 屏幕共享已启动！
>
> [🔗 点击打开监控页面](https://watchitai.net/s/abc123?token=xxx)
>
> 在手机浏览器中打开上述链接即可查看并远程控制电脑屏幕。会话时长 30 分钟，按 Ctrl+C 结束。

### 双模式架构

WatchItAI 支持两种使用模式：

1. **浏览器直接使用**：访问 `https://watchitai.net/host`，使用浏览器原生 `getDisplayMedia()` 进行屏幕共享。由于浏览器 PNA（私有网络访问）限制，此模式仅支持查看，不支持远程控制。

2. **AI 工具启动**：通过 `share` 或 `link` 命令启动，桥接服务提供本地主机页面（`http://localhost:8765/`），页面与桥接服务同源连接，不受 PNA 限制，支持完整的远程控制功能。

| 模式 | 屏幕共享 | 远程控制 | 桥接服务 |
|------|---------|---------|---------|
| 浏览器直接 | ✓ | ✗ | 不需要 |
| AI 工具启动 | ✓ | ✓ | 需要 |

### 权限检查（首次使用）

**macOS / Linux：**
```bash
bash run.sh permissions
```

**Windows：**
```cmd
run.cmd permissions
```

如果有权限缺失，按照提示授予权限后重新运行。

## 安装

技能使用自包含的 Go 二进制文件，**无需 Node.js，无需 npm install**，解压即用。

> **下载源**：默认使用 `https://watchitai.net/watchitai-skill.zip`（主源）。若不可达，可从 [GitHub Releases](https://github.com/SwordLonn/WatchItAI/releases) 下载：
> ```bash
> curl -L https://github.com/SwordLonn/WatchItAI/releases/latest/download/watchitai-skill.zip -o watchitai.zip
> ```

### OpenClaw

```bash
mkdir -p ~/.openclaw/skills && cd ~/.openclaw/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### Claude Code

```bash
mkdir -p ~/.claude/skills && cd ~/.claude/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### WorkBuddy

```bash
mkdir -p ~/.workbuddy/skills && cd ~/.workbuddy/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

Windows 用户：
```powershell
mkdir $env:USERPROFILE\.workbuddy\skills -Force
cd $env:USERPROFILE\.workbuddy\skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
Expand-Archive watchitai.zip -DestinationPath .
Remove-Item watchitai.zip
```

### CowPaw

```bash
mkdir -p ~/.cowpaw/skills && cd ~/.cowpaw/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### Trae

```bash
mkdir -p ~/.trae-cn/skills && cd ~/.trae-cn/skills
curl -L https://watchitai.net/watchitai-skill.zip -o watchitai.zip
unzip watchitai.zip && rm watchitai.zip
```

### 从源码安装（开发模式）

```bash
cd ~/Documents/workspace/WatchItAI
bash skill/install.sh
```

此脚本会自动检测平台、复制正确的二进制文件到 `~/.trae-cn/skills/watchitai/bin/`。

## 配置

编辑 `config.json` 或设置环境变量：

```json
{
  "domain": "watchitai.net",
  "bridgePort": 8765,
  "mode": "server"
}
```

| 配置项 | 环境变量 | 说明 | 默认值 |
|--------|----------|------|--------|
| `domain` | `WATCHITAI_DOMAIN` | WatchItAI 服务域名 | `watchitai.net` |
| `bridgePort` | `WATCHITAI_BRIDGE_PORT` | 本地桥接端口 | `8765` |
| `mode` | `WATCHITAI_MODE` | 运行模式 | `server` |

查看配置：

**macOS / Linux：**
```bash
bash run.sh config
```

**Windows：**
```cmd
run.cmd config
```

## 权限

### macOS

首次使用需运行权限预检：

```bash
bash run.sh preflight
```

需要的权限：
- 📹 屏幕录制 — 屏幕共享和截图
- 🖱️ 辅助功能 — 鼠标和键盘控制
- ⌨️ 输入监控 — 键盘事件监听

随时检查权限状态：

```bash
bash run.sh permissions
```

### Linux

需安装系统工具（如未使用 nut.js）：

```bash
# Debian/Ubuntu
sudo apt install xdotool scrot
```

## 命令列表

**macOS / Linux：**
```bash
bash run.sh share              # 开始屏幕共享（打开本地主机页面）
bash run.sh link               # 创建会话并返回监控链接（供 AI 工具使用）
bash run.sh start              # 仅启动桥接服务
bash run.sh status             # 查看桥接状态
bash run.sh permissions        # 检查权限
bash run.sh preflight          # 权限预检 (macOS)
bash run.sh authorize --request # 一键授权：自动打开浏览器，登录后点确认即可关联账户
bash run.sh authorize <CODE>   # 授权码关联：用网页端生成的 8 位码关联账户
bash run.sh info               # 系统信息
bash run.sh version            # 查看版本
```

**Windows：**
```cmd
run.cmd share              REM 开始屏幕共享
run.cmd link               REM 创建会话并返回监控链接
run.cmd start              REM 仅启动桥接服务
run.cmd status             REM 查看桥接状态
run.cmd permissions        REM 检查权限
run.cmd preflight          REM 权限预检
run.cmd authorize --request REM 一键授权：自动打开浏览器，登录后点确认即可关联账户
run.cmd authorize <CODE>   REM 授权码关联：用网页端生成的 8 位码关联账户
run.cmd info               REM 系统信息
run.cmd version            REM 查看版本
```

## 账户授权

将技能绑定到你的 watchitai.net 账户，解锁更长会话、更高配额和审计历史。

### 推荐方式：一键 Device Flow

在运行技能的终端执行（无需复制任何密钥）：

**macOS / Linux：**
```bash
bash ~/.trae-cn/skills/watchitai/run.sh authorize --request
```

**Windows：**
```cmd
%USERPROFILE%\.trae-cn\skills\watchitai\run.cmd authorize --request
```

执行后：
1. 终端显示授权链接，并自动打开默认浏览器
2. 在浏览器中登录（如未登录），点击「确认授权」
3. 技能端自动获取凭证并写入 `config.json`，全程无需手动复制

### 备选方式：8 位授权码

1. 登录 [watchitai.net/profile](https://watchitai.net/profile) → 技能授权
2. 点击「8 位授权码」生成一次性码（5 分钟有效）
3. 在技能端终端执行：

**macOS / Linux：**
```bash
bash ~/.trae-cn/skills/watchitai/run.sh authorize XXXX-XXXX
```

**Windows：**
```cmd
%USERPROFILE%\.trae-cn\skills\watchitai\run.cmd authorize XXXX-XXXX
```

## 跨平台支持

| 功能 | Windows | macOS | Linux |
|------|---------|-------|-------|
| 屏幕共享 | ✅ | ✅ | ✅ |
| 鼠标移动/点击/滚轮 | ✅ | ✅ | ✅ |
| 键盘输入 | ✅ | ✅ | ✅ |
| 屏幕截图 | ✅ | ✅ | ✅ |
| 系统通知 | ✅ | ✅ | ✅ |

## 工作原理

1. 本地启动桥接服务（localhost:8765），同时提供：
   - WebSocket 桥接端点（`/bridge`）— 系统能力调用
   - 本地主机页面（`/`）— 自包含的屏幕共享 UI
   - API 代理（`/api/*`）— 代理到云端 API 服务器
2. 本地主机页面与桥接服务同源连接，不受浏览器 PNA 限制
3. 屏幕视频流通过 WebRTC P2P 直接传输，不经过服务器中转
4. 远程控制指令通过桥接服务转发到本地执行
5. 你可以在远端设备通过会话链接在浏览器中查看/控制

## Bridge API

连接地址：`ws://localhost:8765/bridge`

### 消息类型

| 类型 | 说明 |
|------|------|
| `controlMouse` | 鼠标控制 |
| `controlKey` | 键盘控制 |
| `controlWheel` | 滚轮控制 |
| `captureScreen` | 屏幕截图 |
| `getScreenSources` | 显示器列表 |
| `showNotification` | 系统通知 |
| `getPermissions` | 权限状态 |
| `ping` | 心跳 |

### HTTP 端点

| 路径 | 方法 | 说明 |
|------|------|------|
| `/health` | GET | 健康检查 |
| `/permissions` | GET | 权限状态 |
| `/screenshot` | GET | 当前截图 (PNG) |
| `/token` | GET | 获取桥接 token |
| `/create-session` | POST | 一步创建会话（返回 shareUrl + localUrl） |
| `/api/*` | ALL | API 代理（转发到 watchitai.net，解决跨域 CSRF 问题） |

## 安全

- 桥接服务仅监听 localhost，不会暴露到公网
- 屏幕视频流使用 WebRTC 端到端加密
- 会话链接包含随机房间号，仅持有链接的设备可以加入

## 文件结构

```
watchitai/
├── run.sh                # Unix 入口脚本（自动检测平台，调用 Go 二进制）
├── run.cmd               # Windows 入口脚本
├── config.json           # 配置
├── SKILL.md
├── bin/
│   ├── watchitai-darwin-amd64       # macOS Intel 二进制
│   ├── watchitai-darwin-arm64       # macOS Apple Silicon 二进制
│   ├── watchitai-linux-amd64        # Linux Intel 二进制
│   ├── watchitai-linux-arm64        # Linux ARM64 二进制
│   ├── watchitai-windows-amd64.exe  # Windows x64 二进制
│   └── cliclick                      # macOS 鼠标控制工具（bundled）
└── scripts/
    ├── ensure_macos_permissions.sh
    ├── take_screenshot.py
    └── take_screenshot.ps1
```
