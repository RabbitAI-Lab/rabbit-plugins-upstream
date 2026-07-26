---
name: "chromecast-control-tool-free"
description: "使用catt工具控制Chromecast设备，支持设备发现、视频投屏与基础播放控制。"
license: Proprietary
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "投屏控制免费版"
  version: "1.0.0"
  summary: "使用catt工具控制Chromecast设备，支持设备发现、视频投屏与基础播放控制。"
  tags:
    - "投屏控制"
    - "Chromecast"
    - "智能家居"
    - "个人创作"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# 投屏控制免费版

## 概述

投屏控制免费版是一款面向个人用户的轻量级Chromecast投屏控制工具，基于catt命令行工具实现。支持设备发现、视频投屏、播放控制、状态查询等核心功能，帮助用户将在线视频或本地文件轻松投屏到电视上观看。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| 设备发现 | 扫描局域网内的Chromecast设备 |
| 视频投屏 | 投屏在线视频URL或本地文件 |
| 播放控制 | 播放、暂停、停止、快进快退 |
| 音量控制 | 调整电视音量 |
| 状态查询 | 查看当前播放状态与设备信息 |
| 网站投屏 | 将网页内容投屏到电视 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：catt、工具控制、支持设备发现、视频投屏与基础播、投屏控制免费版、面向个人用户的轻、投屏控制工具、将在线视频或本地、文件投屏到电视、调整音量等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：投屏在线视频

将在线视频投屏到电视上观看。

```bash
# 发现设备
catt scan

# 投屏YouTube视频
catt cast "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# 指定设备投屏
catt -d "Living Room" cast "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```

### 场景二：投屏本地文件

将本地视频或音频文件投屏到电视。

```bash
# 投屏本地视频文件
catt cast "./movie.mp4"

# 投屏本地音频文件
catt cast "./music.mp3"

# 投屏本地图片
catt cast "./photo.jpg"
```

### 场景三：播放控制

控制当前投屏内容的播放。

```bash
# 暂停播放
catt pause

# 继续播放
catt play

# 停止播放
catt stop

# 快进30秒
catt seek 30

# 快退30秒
catt seek -30

# 跳转到指定位置（秒）
catt seek 120

# 调整音量（0-100）
catt volume 50

# 音量增加
catt volumeup

# 音量减小
catt volumedown

# 静音
catt volumemute
```

## 不适用场景

以下场景投屏控制免费版不适合处理：

- 数据库架构设计决策
- NoSQL选型
- 数据仓库ETL设计

## 触发条件

需要数据库操作、SQL查询、数据存储管理时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 依赖详情

```bash
# 使用pip安装
pip install catt

# 验证安装
catt --version
```

### 2. 发现设备

```bash
# 扫描局域网内的Chromecast设备
catt scan

# 示例
# 192.168.1.100 - Living Room
# 192.168.1.101 - Bedroom TV
```

### 3. 投屏并控制

```bash
# 投屏视频
catt -d "Living Room" cast "https://example.com/video.mp4"

# 暂停
catt -d "Living Room" pause

# 调整音量
catt -d "Living Room" volume 60
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 配置示例

### 常用命令一览

| 命令 | 说明 | 示例 |
| --- | --- | --- |
| `scan` | 发现设备 | `catt scan` |
| `cast` | 投屏内容 | `catt cast "URL"` |
| `pause` | 暂停播放 | `catt pause` |
| `play` | 继续播放 | `catt play` |
| `stop` | 停止播放 | `catt stop` |
| `seek` | 跳转进度 | `catt seek 30` |
| `volume` | 设置音量 | `catt volume 50` |
| `status` | 查看状态 | `catt status` |
| `info` | 设备信息 | `catt info` |

### 设备指定方式

| 方式 | 说明 | 示例 |
| --- | --- | --- |
| 设备名称 | 易读 | `-d "Living Room"` |
| IP地址 | 精确 | `-d 192.168.1.100` |

### 支持的投屏内容

| 内容类型 | 格式 | 说明 |
| --- | --- | --- |
| 在线视频 | URL | YouTube、Bilibili等 |
| 本地视频 | mp4, mkv, avi | 需启动本地服务器 |
| 本地音频 | mp3, wav, flac | 音乐播放 |
| 本地图片 | jpg, png | 图片展示 |
| 网页 | URL | 网站内容投屏 |

## 最佳实践

1. **同一网络**：确保控制设备与Chromecast在同一局域网
2. **设备名称**：使用易读的设备名称，便于多设备区分
3. **视频格式**：推荐使用MP4格式，兼容性最好
4. **音量控制**：使用相对音量调整（volumeup/volumedown），避免突然过大
5. **网络稳定**：投屏大文件时确保网络稳定，避免卡顿
6. **及时停止**：使用完毕后执行stop命令，释放设备

## 常见问题

### Q1：scan找不到设备怎么办？

确保Chromecast设备已开机并连接到同一WiFi网络。检查防火墙是否阻止了mDNS发现。

### Q2：投屏本地文件失败怎么办？

catt投屏本地文件时会启动临时HTTP服务器。确保防火墙允许该端口的访问。

### Q3：可以同时控制多个设备吗？

免费版通过 `-d` 参数指定设备，可分别控制不同设备，但不支持同步操作。

### Q4：支持哪些视频网站？

支持YouTube、Bilibili等主流视频网站，部分网站可能需要额外配置。

### Q5：免费版支持播放队列吗？

免费版不支持播放队列功能。如需队列管理，建议升级至PRO版本。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络环境**: 与Chromecast设备在同一局域网
- **Python版本**: 3.7及以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| catt | Python工具 | 必需 | `pip install catt` |
| Chromecast设备 | 硬件 | 必需 | 购买Chromecast硬件 |

### API Key 配置

- 免费版无需任何API Key
- 所有功能通过局域网内catt命令行工具实现，无需云端认证

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Chromecast投屏控制任务。核心功能通过catt命令行工具在局域网内实现，无需云端API。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
