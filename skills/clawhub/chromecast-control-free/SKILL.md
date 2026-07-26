---
slug: "chromecast-control-free"
name: "chromecast-control-free"
version: 1.0.1
displayName: "投屏设备基础版"
summary: "基础投屏控制，设备发现、媒体投放、播放和音量管理"
license: "MIT"
description: |-
  使用catt工具控制局域网投屏设备的免费版。支持设备发现、基础媒体投放、播放控制和音量调节.
  适用于家庭娱乐和简单投屏场景。升级至完整版可解锁进度跳转、队列管理、字幕加载、
  状态管理和多设备别名管理功能.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
pricing_tier: "L2-标准级"
suggested_price: "19.9 CNY/per_use"

---
# 投屏设备控制（免费版）

使用 `catt`（Cast All The Things）工具控制局域网内的投屏协议设备。免费版提供设备发现、基础媒体投放、播放控制和音量调节功能.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 投屏设备基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
本Skill无需额外API Key（LLM能力由Agent平台内置提供）

### 可用性分类
- **分类**: MD+EXEC（）

## 核心能力

### 1. 设备发现

通过 `catt scan` 命令扫描局域网内的所有投屏设备。返回设备名称和IP地址列表。使用 `-d <device>` 参数通过设备名称或IP地址指定目标设备。适用于初次配置和设备定位。- 验证返回数据的完整性和格式正确性
- 参考`设备发现`的配置文档进行参数调优
### 2. 媒体投放
通过 `catt cast <url>` 命令将视频或音频投放到目标设备。支持YouTube视频、Vimeo、直接视频URL（MP4/MKV/WebM）和本地文件。使用 `-d <device>` 参数指定目标设备。适用于家庭影院和基础投屏场景.
**处理**: 解析用户提供的媒体URL或文件路径,验证格式兼容性后通过catt命令投放到目标Chromecast设备,自动处理设备发现和连接.
**输出**: 返回媒体投放的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`媒体投放`的配置文档进行参数调优
### 3. 播放控制
通过 `catt play`、`catt pause` 和 `catt stop` 命令控制播放状态。`play` 恢复播放，`pause` 暂停播放，`stop` 完全停止播放。使用 `-d <device>` 参数指定目标设备。适用于播放过程中的即时控制.
**处理**: 接收播放控制指令(play/pause/stop/skip),映射到对应的catt子命令并执行,返回播放状态变更确认.
**输出**: 返回播放控制的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 音量控制
通过 `catt volume <0-100>` 设置绝对音量（0-100范围），`catt volumeup 10` 增加10，`catt volumedown 10` 减少10。`catt volumemute on` 静音，`catt volumemute off` 取消静音。适用于不同内容间的音量统一管理.
**输入**: 用户提供音量控制所需的指令和必要参数.
**处理**: 解析音量参数(绝对值0-100或相对增减),通过catt volume命令调整设备音量,返回设置后的音量值.
**输出**: 返回音量控制的处理结果,包含执行状态码、结果数据和执行日志。- 验证返回数据的完整性和格式正确性
- 参考`音量控制`的配置文档进行参数调优
### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 升级提示

以下为完整版（chromecast-control）独有功能，免费版不可用：

- **进度跳转**：`catt seek` 支持秒数和HH:MM:SS格式跳转，`catt ffwd`/`rewind` 快进后退
- **队列管理**：`catt add`/`remove`/`clear` 管理YouTube播放队列，`-n` 参数设置下一首
- **状态管理**：`catt save`/`restore` 保存和恢复播放状态，支持跨设备迁移
- **字幕加载**：`catt cast -s ./subtitles.srt` 加载SRT字幕文件，`-t` 从指定时间点播放
- **设备别名管理**：`set_alias`/`set_default`/`del_alias` 多设备别名快速切换
- **高级投放选项**：`-b` 后台投放、`-y format=best` 格式选择、`-r` 播放列表投放

升级至完整版以获取全部能力.
## 使用流程

1. 运行 `catt scan` 发现局域网内的投屏设备，记录设备名称或IP地址
2. 通过 `catt -d <device> cast <url>` 投放YouTube视频或直接视频URL
3. 使用 `catt -d <device> play`/`pause`/`stop` 控制播放状态
4. 通过 `catt -d <device> volume <0-100>` 调节音量
5. 如需进度跳转、队列管理或字幕加载等高级功能，升级至完整版

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤.
## 示例

### 示例1：发现设备并投放YouTube视频

```bash
# 扫描局域网设备
catt scan
# 输出示例:
# 192.168.1.163 - Living Room TV
# 192.168.1.200 - Bedroom Speaker
# ...
# 投放YouTube视频到指定设备
catt -d "Living Room TV" cast "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# ...
# 暂停播放
catt -d "Living Room TV" pause
# ...
# 设置音量为50
catt -d "Living Room TV" volume 50
```

### 示例2：投放本地视频文件

```bash
# 投放本地MP4文件
catt -d 192.168.1.163 cast ./video.mp4
# ...
# 恢复播放
catt -d 192.168.1.163 play
# ...
# 增加音量10
catt -d 192.168.1.163 volumeup 10
# ...
# 停止播放
catt -d 192.168.1.163 stop
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `catt scan` 找不到设备 | 网络阻止mDNS发现 | 使用设备IP地址直接连接：`catt -d 192.168.1.163 cast <url>` |
| 本地文件投放失败 | TCP端口45000-47000被防火墙阻止 | 开放端口45000-47000范围，或使用网络共享URL代替本地文件 |
| 设备未响应 | 设备休眠或网络断开 | 确认设备已开机且在同一局域网，重新运行 `catt scan` |
| 音量参数超出范围 | 传入了0-100之外的值 | 确保音量值在0-100范围内，使用 `volumeup`/`volumedown` 增减 |
| 请求进度跳转功能 | 免费版不支持 `seek`/`ffwd`/`rewind` | 升级至完整版以使用进度跳转功能 |
| 请求字幕加载功能 | 免费版不支持 `-s` 字幕参数 | 升级至完整版以使用字幕加载功能 |
| 请求队列管理功能 | 免费版不支持 `add`/`remove`/`clear` | 升级至完整版以使用队列管理功能 |

## 常见问题

### Q1: 如何发现局域网中的投屏设备？

运行 `catt scan` 命令扫描局域网。返回结果包含设备名称和IP地址。如果扫描不到设备，可能是网络阻止了mDNS协议，此时可以直接使用设备IP地址连接：`catt -d 192.168.1.163 cast <url>`.
### Q2: 免费版支持投射本地文件吗？

支持。使用 `catt cast ./video.mp4` 命令投射本地文件。需要确保TCP端口45000-47000开放。但免费版不支持加载字幕文件（`-s` 参数），如需字幕功能请升级至完整版.
### Q3: 免费版可以使用进度跳转吗？

不可以。`catt seek`、`catt ffwd` 和 `catt rewind` 是完整版独有功能。免费版仅支持 `play`/`pause`/`stop` 基础播放控制。如需进度跳转，请升级至完整版.
### Q4: 如何调节音量？

使用 `catt volume <0-100>` 设置绝对音量（0-100范围），`catt volumeup 10` 增加10，`catt volumedown 10` 减少10。`catt volumemute on` 静音，`catt volumemute off` 取消静音。使用 `-d <device>` 参数指定目标设备.
### Q5: 免费版支持队列管理吗？

不支持。`catt add`/`remove`/`clear` 队列管理是完整版独有功能。免费版每次只能投放单个媒体。如需队列管理，请升级至完整版.
### Q6: 如何管理多个设备？

免费版通过 `-d <device>` 参数指定目标设备名称或IP地址。完整版支持设备别名管理（`set_alias`/`set_default`），可设置简短别名快速切换设备。如需别名管理，请升级至完整版.
## 已知限制

- 不支持进度跳转（`seek`/`ffwd`/`rewind`），完整版可用
- 不支持队列管理（`add`/`remove`/`clear`），完整版可用
- 不支持字幕加载（`-s` 参数），完整版可用
- 不支持状态保存/恢复（`save`/`restore`），完整版可用
- 不支持设备别名管理（`set_alias`/`set_default`），完整版可用
- 投屏设备与计算机必须在同一局域网内
