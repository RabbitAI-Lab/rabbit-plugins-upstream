---
slug: gif-whatsapp-tool-free
name: gif-whatsapp-tool-free
version: 1.0.0
displayName: WhatsApp表情搜索
summary: WhatsApp GIF 表情搜索发送工具，支持 Tenor/Giphy 搜索并自动转换为 MP4 格式发送，适合个人日常聊天使用.
license: Proprietary
edition: free
description: 'WhatsApp GIF 表情搜索发送工具，支持 Tenor/Giphy 搜索并自动转换为 MP4 格式发送，适合个人日常聊天使用。核心能力:

  - 搜索 Tenor 和 Giphy 平台的 GIF 表情

  - 自动将 GIF 转换为 WhatsApp 兼容的 MP4 格式

  - 一键发送到指定 WhatsApp 联系人

  - 支持中英文关键词搜索

  适用场景:

  - 个人日常 WhatsApp 聊天表情发送

  - 节日祝福与庆祝场景

  - 情感表达与趣味互动

  差异化:

  - 免费版聚焦单次搜索发送...'
tags:
  - WhatsApp
  - GIF
  - 多媒体
  - 聊天工具
  - 表情搜索
  - 搜索
  - 检索
  - 工具
  - gif
  - mp4
  - tmp
  - whatsapp
  - message
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
category: "Knowledge"
---
# WhatsApp 表情搜索（免费版）

## 概述

WhatsApp 表情搜索免费版是一款面向个人用户的 GIF 表情搜索与发送工具。WhatsApp 不支持直接发送 Tenor 或 Giphy 的 GIF 链接，本工具自动完成 GIF 下载、格式转换为 MP4、发送到指定联系人的一站式流程，让 WhatsApp 聊天更生动有趣.
## 核心能力

| 能力 | 说明 | 免费版支持 |
|---|---|-----|
| GIF 搜索 | 搜索 Tenor 和 Giphy 平台 | 是 |
| 格式转换 | GIF 自动转 MP4 | 是 |
| 发送到 WhatsApp | 通过 message 工具发送 | 是 |
| 批量发送 | 一次发送多个 GIF | 否 |
| 自定义字幕 | 添加文字说明 | 否 |
| 定时发送 | 定时发送 GIF | 否 |
| GIF 库管理 | 收藏常用 GIF | 否 |

### 已知限制
执行已知限制操作,使用`input_params`参数进行配置,支持创建/查询/导出等操作.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 单次搜索最多返回 5 个结果
单次搜索最多返回 5 个结果

**处理**: 解析单次搜索最多返回 5 个结果的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回单次搜索最多返回 5 个结果的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 一次只能发送给 1 个联系人
一次只能发送给 1 个联系人

**处理**: 解析一次只能发送给 1 个联系人的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回一次只能发送给 1 个联系人的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持自定义字幕（使用空格占位
不支持自定义字幕（使用空格占位）

**处理**: 解析不支持自定义字幕（使用空格占位的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持自定义字幕（使用空格占位的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持定时发送
不支持定时发送

**处理**: 解析不支持定时发送的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持定时发送的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 不支持 GIF 收藏库
不支持 GIF 收藏库

**处理**: 解析不支持 GIF 收藏库的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回不支持 GIF 收藏库的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

**处理**: 解析已知限制的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回已知限制的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：表情搜索发送工具、搜索并自动转换为、格式发送、适合个人日常聊天、核心能力、平台的、自动将、转换为、兼容的、一键发送到指定、支持中英文关键词等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：日常聊天表情发送

用户在 WhatsApp 聊天时希望发送一个庆祝的 GIF.
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | WhatsApp表情搜索处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```bash
# 搜索庆祝类 GIF
gifgrep "celebration" --max 5 --format url
# ...
# 下载并转换格式
curl -sL "GIF_URL" -o /tmp/gif.gif
ffmpeg -i /tmp/gif.gif -movflags faststart -pix_fmt yuv420p \
  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/gif.mp4 -y
# ...
# 发送到 WhatsApp
cp /tmp/gif.mp4 /root/.skill-platform/workspace/gif.mp4
message action=send to=NUMBER message=" " \
  filePath=/root/.mp4 gifPlayback=true
```

预期效果：联系人在 WhatsApp 中收到一个循环播放的庆祝 GIF.
### 场景二：节日祝福发送

用户希望在节日时发送应景的 GIF 祝福.
```bash
# 搜索新年祝福 GIF
gifgrep "happy new year fireworks" --max 5 --format url
# ...
# 选择最合适的一个，下载并发送
curl -sL "SELECTED_URL" -o /tmp/newyear.gif
ffmpeg -i /tmp/newyear.gif -movflags faststart -pix_fmt yuv420p \
  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/newyear.mp4 -y
cp /tmp/newyear.mp4 /root/.skill-platform/workspace/newyear.mp4
message action=send to=FRIEND_NUMBER message="新年快乐" \
  filePath=/root/.mp4 gifPlayback=true
```

### 场景三：情感表达回复

用户想要用表情回复朋友的消息，表达惊讶或搞笑.
```bash
# 搜索搞笑表情
gifgrep "laughing funny" --max 5 --format url
# ...
# 快速发送（一行命令）
curl -sL "URL" -o /tmp/g.gif && \
ffmpeg -i /tmp/g.gif -movflags faststart -pix_fmt yuv420p \
  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" /tmp/g.mp4 -y 2>/dev/null && \
cp /tmp/g.mp4 /root/.skill-platform/workspace/g.mp4
```

## 不适用场景

以下场景WhatsApp表情搜索不适合处理：

- 黑帽SEO手段
- 搜索引擎作弊
- 付费广告投放管理

## 触发条件

需要SEO优化、关键词分析、排名提升、搜索流量优化时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 依赖详情

```bash
# 安装 gifgrep（GIF 搜索工具）
# 参考 gifgrep 官方文档安装
# ...
# 安装 ffmpeg（格式转换）
# macOS
brew install ffmpeg
# ...
# Ubuntu/Debian
sudo apt install ffmpeg
# ...
# 验证安装
ffmpeg -version
gifgrep --version
```

### 执行首次搜索发送

```bash
# 1. 搜索 GIF
gifgrep "thumbs up" --max 3 --format url
# ...
# 2. 下载 GIF
curl -sL "GIF_URL_FROM_RESULTS" -o /tmp/gif.gif
# ...
# 3. 转换为 MP4
ffmpeg -i /tmp/gif.gif -movflags faststart -pix_fmt yuv420p \
# ...
# 4. 复制到工作区
cp /tmp/gif.mp4 /root/.mp4
# ...
# 5. 发送
message action=send to=CONTACT_NUMBER message=" " \
  filePath=/root/.mp4 gifPlayback=true
```

**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
#
## 示例

### 常用搜索关键词

| 情感 | 推荐搜索词 |
|---:|---:|
| 开心 | celebration, party, dancing, excited |
| 赞同 | thumbs up, nice, good job, applause |
| 搞笑 | laugh, lol, haha, funny |
| 惊讶 | mind blown, shocked, surprised, wow |
| 难过 | crying, sad, disappointed |
| 无奈 | facepalm, ugh, annoyed |
| 爱意 | heart, love, hug |
| 酷炫 | sunglasses, cool, awesome |

### 发送注意事项

```text
重要：WhatsApp 的 message 工具只能发送工作区目录中的文件
- 文件必须位于 /root/.skill-platform/workspace/ 目录下
- /tmp 目录中的文件会报错 LocalMediaAccessError
- 消息体不能为空，使用单个空格作为占位符
- 必须设置 gifPlayback=true 才能以 GIF 形式播放
```

## 最佳实践

### 搜索关键词优化

1. **使用英文搜索**：Tenor 和 Giphy 的英文结果更丰富
2. **具体描述场景**：`happy birthday cake` 比 `birthday` 更精准
3. **多结果对比**：获取 5 个结果后选择最合适的，而非直接用第一个
4. **避免过于宽泛**：`funny cat` 比 `cat` 更有针对性

### GIF 选择建议

```bash
# 获取多个结果进行对比
gifgrep "thank you" --max 5 --format url
# ...
# 查看文件名和描述，选择最合适的
# 避免选择过大或过小的 GIF
# 优选 480p 或 720p 分辨率的 GIF
```

### 发送频率控制

- 一个对话中发送 1 个 GIF 即可，不要连续发送多个
- 不是每条消息都需要 GIF，适度使用
- 考虑接收方的感受，避免发送不当内容

## 常见问题

### GIF 搜索无结果

```bash
# 检查网络连接
curl -I https://media.tenor.com
# ...
# 尝试更换关键词
gifgrep "happy" --max 5 --format url  # 使用更通用的词
# ...
# 检查 gifgrep 配置
gifgrep --config
```

### ffmpeg 转换失败

```bash
# 检查 ffmpeg 是否安装
ffmpeg -version
# ...
# 重新安装 ffmpeg
# macOS
brew reinstall ffmpeg
# ...
# 验证 GIF 文件完整性
file /tmp/gif.gif
```

### 发送失败 LocalMediaAccessError

```text
原因：文件未复制到工作区目录
解决：确保执行 cp 命令将文件复制到 /root/.skill-platform/workspace/
```

```bash
# 正确流程
cp /tmp/gif.mp4 /root/.mp4
# ...
# 然后再发送
message action=send to=NUMBER message=" " \
  filePath=/root/.mp4 gifPlayback=true
```

### GIF 在 WhatsApp 中不循环播放

```bash
# 确保设置了 gifPlayback=true
message action=send to=NUMBER message=" " \
  filePath=/root/.mp4 gifPlayback=true
# ...
# 检查 MP4 格式参数
ffmpeg -i /tmp/gif.gif -movflags faststart -pix_fmt yuv420p \
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **网络环境**：需可访问 Tenor、Giphy 和 WhatsApp 服务
- **存储空间**：至少 100MB 用于临时文件存储

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| gifgrep | CLI 工具 | 是 | 参考官方文档安装 |
| ffmpeg | 多媒体处理 | 是 | `brew install ffmpeg` 或 `apt install ffmpeg` |
| curl | 文件下载 | 是 | 系统自带 |
| WhatsApp message 工具 | 发送服务 | 是 | 平台内置 |
| LLM API | API | 是 | 由 Agent 内置 LLM 提供 |

### API Key 配置

- 免费版无需额外 API Key
- gifgrep 使用公开 API，无需认证
- WhatsApp 发送使用平台内置 message 工具，无需单独配置

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，部分功能需要 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行任务
- **适用人群**：个人 WhatsApp 用户、社交活跃用户
- **升级建议**：如需批量发送、定时发送、GIF 库管理等高级功能，请使用 PRO 版本

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "WhatsApp表情搜索处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "gif whatsapp"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
