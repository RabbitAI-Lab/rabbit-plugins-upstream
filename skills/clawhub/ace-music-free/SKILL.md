---
slug: "ace-music-free"
name: "ace-music-free"
version: 1.0.1
displayName: "ACE Music AI音乐LITE"
summary: "ACE Music基础版,文本转音乐生成,支持歌词定制和纯音乐模式"
license: "MIT"
description: |-
  ACE Music AI 音乐生成基础客户端（免费版）。通过 ACE Music 托管的免费 API 调用 ACE-Step 1.5 模型,
  支持文本转音乐、自定义歌词、纯音乐模式三种基础能力。支持时长参数控制,音频以 base64 MP3 返回并由脚本自动解码.
  API 需付费订阅。适用于个人创作者、快速音乐原型、学习试用场景.
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# ACE Music LITE

ACE Music 基础版,基于 ACE-Step 1.5 模型生成 AI 音乐。付费订阅使用。仅支持文本转音乐（text2music）任务.
**范围外**（本技能不做）: 翻唱（cover）、片段重绘（repaint）、批量生成、种子复现、BPM/调性精确控制（需升级付费版）.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---|---|----|----|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 基础生成

使用 `（请参考skill目录中的脚本文件）` 完成一站式生成:

```bash
# 基础文本生成
（请参考skill目录中的脚本文件） "upbeat pop song about summer" --duration 30 --output summer.mp3
# ...
# 自定义歌词
（请参考skill目录中的脚本文件） "gentle acoustic ballad, female vo
# ...
**输入**: 用户提供基础生成相关的配置参数、输入数据和处理选项.
**处理**: 解析文本提示词和生成参数,调用AI模型API执行生成任务,返回生成结果.
# ...
### 参数指南（基础参数）
| 想要 | 参数 |
|:-----|:-----|
| 特定风格 | 在 prompt 中描述: "jazz, saxophone solo, smoky bar" |
| 自定义歌词 | `--lyrics "[Verse]...[Chorus]..."` |
| 无人声 | `--instrumental` |
| 更长歌曲 | `--duration 120`（秒） |
# ...
> **升级提示*
# ...
**处理**: 解析参数指南（基础参数）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
# ...
**输出**: 返回参数指南（基础参数）的处理结果,包含执行状态码、结果数据和执行日志.
#
## 认证
# ...
使用 `ACE_MUSIC_API_KEY` 环境变量。永不打印或暴露 Key.
# ...
```bash
[ -n "${ACE_MUSIC_API_KEY:-}" ] && echo ok || echo missing
```
# ...
若 Key 缺失,引导用户:
1. 浏览器打开 `https://acemusic.ai/playground/api-key`
2. 注册（免费）并创建 API Key
3. 终端环境变量: `export ACE_MUSIC_API_KEY="你的Key"`
4. 配置完成后重新发起生成请求
# ...
**安全红线**: 永不接受/回显/存储来自聊天输入的 Key;Key 仅作认证头使用.
# ...
## 基础生成(补充)
# ...
使用 `（请参考skill目录中的脚本文件）` 完成一站式生成:
# ...
```bash
# 基础文本生成
（请参考skill目录中的脚本文件） "upbeat pop song about summer" --duration 30 --output summer.mp3

# 自定义歌词
（请参考skill目录中的脚本文件） "gentle acoustic ballad, female vocal" \
  --lyrics "[Verse 1]\nSunlight through the window\n\n[Chorus]\nWe are the dreamers" \
  --duration 60 --output ballad.mp3

# 纯音乐（无人声）
（请参考skill目录中的脚本文件） "lo-fi hip hop beats, chill, rainy day" --instrumental --duration 120 --output lofi.mp3
```
# ...
脚本将生成的文件路径输出到 stdout,Agent 应将文件发送给用户.
# ...
## 参数指南（基础参数）(补充)
# ...
| 想要(续)| 参数 |
|---:|---:|
| 特定风格 | 在 prompt 中描述: "jazz, saxophone solo, smoky bar" |
| 自定义歌词 | `--lyrics "[Verse]...[Chorus]..."` |
| 无人声 | `--instrumental` |
| 更长歌曲 | `--duration 120`（秒） |
# ...
> **升级提示**: BPM/调性/语言/种子/批量生成、cover 翻唱、repaint 片段重绘等高级能力仅在 ace-music 付费版中提供.
# ...
## 适用场景
# ...
| 场景 | 典型输入 | 输出内容 |
|:---:|:---:|:---:|
| 基础文本生成 | "生成一首关于夏天的流行歌" | MP3 文件 |
| 带歌词人声生成 | "生成民谣,带歌词" | 带人声 MP3 文件 |
| 纯音乐节拍 | "做一段 lo-fi 节拍" | 无人声 MP3 文件 |
# ...
**不适用于**: 翻唱已有歌曲、修改已有音频、批量生成、精确 BPM/调性控制（需升级付费版）
# ...
## 使用流程
# ...
### Step 1: 校验 API Key
```bash
[ -n "${ACE_MUSIC_API_KEY:-}" ] && echo ok || echo missing
```
# ...
### Step 2: 缺失时引导配置
> 需要先配置 ACE Music API Key:
> 1. 访问 https://acemusic.ai/playground/api-key
> 2. 注册（免费）并创建 API Key
> 3. 终端环境变量: `export ACE_MUSIC_API_KEY="你的Key"`
> 4. 配置完成后重新发起生成请求
# ...
### Step 3: 构造参数并执行
- prompt 必填,描述风格/情绪/乐器
- lyrics 可选,推荐使用 `[Verse]`/`[Chorus]` 标签模式
- duration 不填则由 AI 决定
# ...
### Step 4: 解码与落盘
- 脚本自动完成 base64 解码与 MP3 落盘
- 将文件路径回传给用户
# ...
#
## 案例展示
# ...
### 案例1: 基础文本生成
**场景**: 用户需要快速生成一段 30 秒的夏日主题流行歌
# ...
```bash
（请参考skill目录中的脚本文件） "upbeat pop song about summer, sunny beach, upbeat tempo" \
  --duration 30 --output summer.mp3
```
# ...
**输出**: `summer.mp3` 文件路径
# ...
**说明**: 通过 prompt 描述风格与情绪,`--duration 30` 控制时长。适合快速原型与试听.
# ...
### 案例2: 带歌词的人声生成
**场景**: 创作者需要生成一首带歌词的民谣
# ...
```bash
（请参考skill目录中的脚本文件） "gentle acoustic ballad, female vocal, fingerstyle guitar" \
  --lyrics "[Verse 1]\nSunlight through the window\nCoffee getting cold\n\n[Chorus]\nWe are the dreamers\nChasing after light" \
  --duration 60 --output ballad.mp3
```
# ...
**输出**: `ballad.mp3` 文件路径
# ...
**说明**: `--lyrics` 使用 `[Verse]`/`[Chorus]` 标签模式确保段落结构清晰。AI 会根据歌词内容自动匹配旋律与人声.
# ...
## 错误处理
# ...
# ...
| 错误场景 | 错误信息 | 原因分析 | 处理方式 |
|:------|------:|:------|:------|
| missing_api_key | `ACE_MUSIC_API_KEY missing` | 环境变量未设置 | 不调 API,引导用户访问 acemusic.ai 注册并配置 Key |
| 401 unauthorized | `{"error":"invalid_api_key"}` | Key 格式错误或已失效 | 检查网络连接和配置后重试,引导用户重新生成 Key |
| 429 rate_limited | `{"error":"rate_limited"}` | 短时间内请求过多 | 等待 2 秒后检查网络连接和配置后重试,最多 3 次 |
| 400 invalid_duration | `{"error":"duration_out_of_range"}` | duration 超出支持范围 | 检查网络连接和配置后重试,提示用户调整时长（5-300 秒） |
| 400 invalid_lyrics | `{"error":"lyrics_format_error"}` | lyrics 含非法字符或格式错误 | 检查网络连接和配置后重试,引导用户使用 `[Verse]`/`[Chorus]` 标签 |
| 5xx server_error | HTTP 500/502/503 | ACE Music 服务端错误 | 等待后检查网络连接和配置后重试,最多 2 次 |
# ...
## 常见问题
# ...
### Q1: ACE Music API 真的免费吗?
A: ACE Music 团队确认 API 需付费订阅,详见定价方案。基础地址 `https://api.acemusic.ai`。如遇未来政策调整,以 ACE Music 官方公告为准.
# ...
### Q2: 生成的歌曲时长有什么限制?
A: `--duration` 参数控制生成时长（秒）。不填则由 AI 根据内容自动决定。建议从 30-60 秒开始尝试.
# ...
### Q3: 如何使用自定义歌词?
A: 通过 `--lyrics` 参数传入,推荐使用 `[Verse 1]`、`[Chorus]` 等标签,换行分隔歌词行。标签模式能让 AI 更准确理解歌曲结构.
# ...
### Q4: 免费版和付费版有什么区别?
A: 免费版（LITE）支持文本转音乐、自定义歌词、纯音乐三种基础能力。付费版（ace-music）额外提供:
- 翻唱（cover）与片段重绘（repaint）任务
- 批量生成（--batch）与种子复现（--seed）
- BPM/调性/语言精确控制（--bpm/--key/--language）
- 采样模式（--sample-mode,AI 自动生成歌词）
- 3 个完整案例（vs 免费版 2 个基础案例）
- 9 种错误处理（vs 免费版 6 种）
# ...
## 已知限制
# ...
1. **基础任务**: 仅支持 text2music,不支持 cover/repaint（需升级付费版）
2. **基础参数**: 仅支持 duration/lyrics/instrumental,不支持 bpm/key/language/seed/batch
3. **需 API Key**: 必须配置 `ACE_MUSIC_API_KEY`
4. **API 基础地址固定**: `https://api.acemusic.ai`,不支持自建部署
5. **生成质量取决于 prompt 描述**: 风格描述越具体,结果越符合预期
# ...
---
# ...
> **想要翻唱、批量生成、精确 BPM 控制?** 升级到 [ace-music 付费版](#) 解锁全部高级能力.
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    "result": "ACE Music AI音乐LITE处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ace-music"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
# ...