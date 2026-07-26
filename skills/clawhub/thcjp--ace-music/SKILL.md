---
slug: "ace-music"
name: "ace-music"
version: 1.0.1
displayName: "AI音乐创作翻唱工坊"
summary: "版权音乐太贵?ACE-Step 1.5一键生成带人声歌曲,付费版独享翻唱、片段重绘、批量生成,精确控制BPM与调性,输出MP3"
license: "Proprietary"
description: |-
  ACE Music AI 音乐生成客户端。通过 ACE-Step 1.5 模型生成完整带人声的歌曲,
  支持文本转音乐、自定义歌词、纯音乐、采样模式、翻唱与片段重绘等多种任务类型.
  支持时长、BPM、调性、语言、种子、批量等参数控制,音频以 base64 MP3 返回并由脚本自动解码为本地 MP3 文件.
  付费版独享翻唱、片段重绘、批量生成、精确BPM/调性控制等高级能力。适用于独立开发者、内容创作者、自动化音乐生产工作流场景.
tags:
  - Creative
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# ACE Music

ACE Music 是基于 ACE-Step 1.5 模型的 AI 音乐生成客户端,生成完整带人声的歌曲。付费版独享翻唱、片段重绘、批量生成、精确BPM/调性控制等高级能力。API 基础地址固定为 `https://api.acemusic.ai`.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 文本转音乐(text2music) | 支持 | 支持 |
| 翻唱已有歌曲(cover) | 不支持 | 支持 |
| 片段重绘(repaint) | 不支持 | 支持 |
| 批量生成(--batch) | 不支持 | 支持 |
| 精确BPM/调性控制 | 不支持 | 支持 |
| 种子复现(--seed) | 不支持 | 支持 |
| 多语言人声(--language) | 仅英文 | zh/en/ja/ko等 |

**范围外**: 模型微调训练、本地推理部署、商业分发渠道对接、版权登记与授权.
## 依赖说明

- **运行环境**: Windows/macOS/Linux,支持SKILL.md的任意AI Agent(Claude Code/Cursor/Codex等)
- **依赖项**: LLM API(由Agent内置提供)
- **API Key配置**: `export ACE_MUSIC_API_KEY="your_key"`,配置后重启会话生效,避免泄露到版本控制
- **可用性分类**: MD+EXEC

## 核心能力

### 任务类型

ACE Music API 支持三种核心任务,通过请求体的 `task_type` 字段切换:

| 任务类型 | 用途 | 是否需要音频输入 |
|---:|---:|---:|
| `text2music`（默认） | 文本/歌词生成新音乐 | 否 |
| `cover` | 翻唱已有歌曲,保留旋律替换音色 | 是 |
| `repaint` | 修改已有音频的指定片段 | 是 |

`cover` 与 `repaint` 任务需提供音频输入（URL 或 base64）,详见 `references/api-docs.md`.
## 快速生成

优先使用封装脚本完成一站式生成。脚本将生成的文件路径输出到 stdout,Agent 应将文件发送给用户.

**基础用法**:
- 文本生成: `脚本 "upbeat pop song about summer" --duration 30 --output summer.mp3`
- 自定义歌词: `脚本 "ballad" --lyrics "[Verse 1]\n...\n[Chorus]\n..." --duration 60`
- 纯音乐: `脚本 "lo-fi hip hop" --instrumental --duration 120`
- 采样模式: `脚本 "jazz song" --sample-mode`
- 精确控制: `脚本 "rock anthem" --bpm 140 --key "E minor" --language en --seed 42`
- 批量生成: `脚本 "edm track" --batch 3 --output edm.mp3`

## 参数指南

| 想要 | 参数 |
|:---:|:---:|
| 特定风格 | 在 prompt 中描述: "jazz, saxophone, smoky bar" |
| 自定义歌词 | `--lyrics "[Verse]...[Chorus]..."` |
| AI 全自动 | `--sample-mode` |
| 无人声 | `--instrumental` |
| 更长歌曲 | `--duration 120`（秒,5-300） |
| 特定节奏 | `--bpm 120` |
| 特定调性 | `--key "C major"` |
| 多个输出 | `--batch 3` |
| 可复现 | `--seed 42` |
| 非英文人声 | `--language ja`（zh/en/ja/ko 等） |

## 直接调用 API

如需 cover/repaint 或音频输入等高级用法,可绕过脚本直接调 API,完整规范见 `references/api-docs.md`.

基础请求结构: POST `https://api.acemusic.ai/v1/generate`,Header 需 `Authorization: Bearer ${ACE_MUSIC_API_KEY}`。请求体关键字段: `task_type`、`prompt`(必填,描述风格/情绪/乐器)、`lyrics`、`duration`(5-300秒)、`bpm`、`key`、`language`、`instrumental`、`sample_mode`、`seed`、`batch_size`。响应体中音频以 base64 编码 MP3 返回,需解码后写入本地文件: `base64 -d > output.mp3`.

## 适用场景

| 场景 | 输出 | 涉及参数 |
|:------|:------|:------|
| 带歌词完整人声歌曲 | 完整 MP3(人声+伴奏) | prompt + lyrics + duration |
| 纯音乐节拍制作 | 无人声 MP3 | prompt + instrumental + duration |
| 多版本批量生成与复现 | 多个 MP3 | prompt + batch + seed |
| 已有音频翻唱与片段重绘 | 翻唱/重绘后 MP3 | task_type=cover/repaint + audio |

**不适用于**: 模型微调训练、本地推理部署、商业音乐分发、版权登记.
## 使用流程

1. **校验 API Key**: `[ -n "${ACE_MUSIC_API_KEY:-}" ] && echo ok || echo missing`
2. **缺失时引导配置**: 访问 https://acemusic.ai/playground/api-key 注册创建Key,设置环境变量后重新请求
3. **选择任务类型**: text2music(默认)/cover(翻唱)/repaint(片段重绘,需音频输入)
4. **构造参数并执行**: prompt必填,lyrics可选(推荐`[Verse]`/`[Chorus]`标签),duration不填则AI决定
5. **解码与落盘**: 脚本自动完成base64解码与MP3落盘,直接调API时需手动`base64 -d`

## 案例展示

### 案例: 流派风格化批量生成

**场景**: 制作团队需要 3 个版本的电子舞曲,且希望后续能复现相同结果

```bash
脚本 "electronic dance track, festival energy" \
  --batch 3 --seed 42 --duration 120 --output edm.mp3
```

**输出**: 3 个 MP3 文件路径(edm_1.mp3 / edm_2.mp3 / edm_3.mp3)

**说明**: `--seed 42` 确保相同参数下结果可复现;`--batch 3` 一次请求生成多个版本,适合 A/B 试听选曲。注意 batch 模式下每个版本会消耗独立 API 调用.
## 错误处理

| 错误场景 | 错误信息 | 原因 | 处理方式 |
|---:|:---|---:|---:|
| missing_api_key | `ACE_MUSIC_API_KEY missing` | 环境变量未设置 | 不调 API,引导用户配置 Key |
| 401 unauthorized | `invalid_api_key` | Key 失效 | 引导用户重新生成 Key 后重试 |
| 429 rate_limited | `rate_limited` | 请求过多 | 指数退避重试(2s/4s/8s),最多3次 |
| 400 invalid_duration | `duration_out_of_range` | duration超出5-300秒 | 提示用户调整时长范围 |
| 5xx server_error | HTTP 500/502/503 | 服务端错误 | 指数退避重试最多2次;持续失败记录请求ID联系团队 |

## 常见问题

### Q1: 付费版有哪些独享能力?
A: 付费版独享翻唱(cover)、片段重绘(repaint)、批量生成(--batch)、精确BPM/调性控制、种子复现(--seed)和多语言人声等高级能力。免费版仅支持基础文本转音乐.

### Q2: 支持哪些语言的人声?如何复现结果?
A: 支持 zh/en/ja/ko 等主流语言,通过 `--language` 参数指定。使用 `--seed` 参数(如 `--seed 42`)可获得可复现结果,相同 seed+参数组合产生相同结果.

### Q3: cover 和 repaint 任务有什么区别?歌词格式有要求?
A: `cover` 对整首歌翻唱保留旋律替换音色;`repaint` 仅修改指定片段。两者都需提供音频输入(audio_url 或 audio_base64)。歌词推荐使用标签模式(`[Verse]`/`[Chorus]`/`[Bridge]`),换行分隔歌词行.

## 已知限制

1. **需 API Key**: 必须配置 `ACE_MUSIC_API_KEY`,无 Key 环境无法使用
2. **API 基础地址固定**: `https://api.acemusic.ai`,不支持自建/私有部署
3. **cover/repaint 需音频输入**: 不能凭空翻唱,需提供已有音频
4. **长时长生成耗时较长**: 120 秒以上生成可能需要 30-60 秒等待
5. **批量生成独立调用**: batch=N 会产生 N 次 API 调用,消耗较多时间
