---
name: qq-music-control
version: 1.0.0
description: 控制 macOS QQ 音乐客户端播放、暂停、下一首、随机播放等
trigger:
  - 播放音乐
  - 放首歌
  - 下一首
  - 上一首
  - 随机播放
  - 暂停音乐
  - QQ音乐
  - 音量
  - play music
  - next song
  - shuffle
---

# QQ 音乐控制 Skill

通过 macOS MediaRemote 私有框架控制 QQ 音乐客户端，**无需 Accessibility 权限**。

## 支持的命令

| 用户说的 | 执行命令 | 说明 |
|----------|----------|------|
| "播放音乐" / "放首歌" / "暂停" | `play` | 切换播放/暂停 |
| "下一首" / "换一首" | `next` | 跳到下一首 |
| "上一首" | `prev` | 回到上一首 |
| "随机播放一首" / "随便来首歌" | `random` | 随机跳转 1-5 次后播放 |
| "音量大一点" | `volume-up` | 增加音量 |
| "音量小一点" | `volume-down` | 减小音量 |
| "QQ音乐状态" / "QQ音乐在运行吗" | `status` | 检查运行状态 |

## 执行方式

所有命令通过 Python 脚本执行。脚本仅使用 Python 标准库（ctypes, subprocess），任何 Python 3 均可运行：

```bash
# 优先使用系统 Python（任何 Python 3 都行）
python3 ~/.workbuddy/skills/qq-music-control/scripts/qq_music.py <command>

# 或使用 WorkBuddy 管理 Python
~/.workbuddy/binaries/python/versions/3.13.12/bin/python3 ~/.workbuddy/skills/qq-music-control/scripts/qq_music.py <command>
```

命令列表：`play` `start` `pause` `next` `prev` `random` `volume-up` `volume-down` `status` `launch`

## 技术原理

- **控制方式**：通过 `MediaRemote.framework`（macOS 私有框架）的 `MRMediaRemoteSendCommand` 函数发送媒体控制命令
- **命令常量**：Play=0, Pause=1, Toggle=2, Stop=3, Next=4, Previous=5, VolUp=6, VolDown=7
- **优势**：不需要 Accessibility 权限、不需要 AppleScript 自动化权限，系统级媒体控制
- **作用范围**：QQ 音乐作为当前 "Now Playing" 应用接收命令
- **前提条件**：QQ 音乐已安装（`/Applications/QQMusic.app`），首次使用会自动启动
- **无需安装任何依赖**：仅使用 ctypes（Python 内置）调用系统框架

## 多机器使用

此 Skill 安装在 `~/.workbuddy/skills/` 用户级别目录，所有项目通用。
在多台 Mac 上各自安装一份，每台机器控制本机的 QQ 音乐客户端。
只需确保：
1. 每台 Mac 都安装了 QQ 音乐（`/Applications/QQMusic.app`）
2. 每台 Mac 都有 Python 3（macOS 自带或通过 brew/miniforge 安装）
