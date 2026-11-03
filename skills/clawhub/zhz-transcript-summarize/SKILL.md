---
name: zhz-transcript-summarize
description: "本地音视频转文字 + 要点摘要。转录稿按内容哈希缓存，可换角度反复总结而无需重新转录。触发词：转录音频、转录视频、语音转文字、音频总结、会议纪要、录音摘要、总结视频内容、transcribe、transcript、summarize podcast。Use when user asks to transcribe a local audio/video file and summarize its key points, or to re-summarize the same recording from a different angle."
homepage: http://openclaw.bjbook.net/
---

# 本地转写 + 要点摘要（两阶段）

把本地视频、音频或播客文件在本机转成文字，再提炼成要点摘要。转录稿按内容哈希缓存，换角度重新总结时完全跳过转录阶段。

## 环境依赖

| 依赖 | 用途 | 版本 |
|------|------|------|
| Python | 运行脚本 | 3.12+ |
| ffmpeg | 提取音频 | 6.1.1 |
| faster-whisper | 语音识别（本地） | 1.2.1（脚本自动安装） |

脚本独立于大模型运行：转录阶段音频永不离开本机，无需任何 API key。

## 文件结构

```
skills/zhz-transcript-summarize/
├── SKILL.md
├── scripts/
│   ├── transcribe.py      # 阶段一：转写 + 缓存
│   ├── summarize.py       # 阶段二：准备摘要输入（术语纠错/时间轴/字幕/上下文）
│   └── render_html.py     # 阶段二：把摘要 Markdown 渲染成可独立打开的 HTML
├── templates/
│   ├── meeting.md         # 会议记录模板
│   ├── key_summary.md     # 关键摘要模板（默认）
│   └── analysis.md        # 分析报告模板
└── examples/
    └── glossary.example.txt
```

缓存目录：`~/.cache/zhz-transcript/`（Windows 即 `C:\Users\<user>\.cache\zhz-transcript\`）。

## 两阶段流程

### 阶段一：转录（缓存命中则跳过）

**完成标准：** 得到转录稿 JSON（`~/.cache/zhz-transcript/<内容哈希>-<model>.json`）。

```bash
python "{baseDir}/scripts/transcribe.py" "<音频/视频路径>" [--model base] [--lang auto] [--force]
```

- 缓存键 = 文件内容 SHA-256 + 模型名。同一文件重复运行直接命中，除非 `--force`。
- 语言自动检测（`--lang zh/en/...` 可强制）。
- `--print` 把转录全文打印到 stdout。
- 支持 GPU：`--device cuda`（`faster-whisper` 自动用 CTranslate2）。
- 输出：缓存 JSON（含元数据、全文、带时间戳 segments）、同目录 `.txt` 纯文本。

**模型选择：** `base` 适合多数场景；长内容/要求更高准确度用 `small` 或 `medium`。首次运行自动下载模型到 `~/.cache/huggingface/`（脚本已设 HF 镜像）。

### 阶段二：摘要 / 总结

**完成标准：** 生成摘要文件 `summaries/<name>/summary.md`。

**换角度重新总结只需重跑本阶段**，用不同 `--focus` / `--format` / `--length` 等参数，完全跳过转录。

第一步：准备摘要输入（确定性步骤，不做摘要生成）

```bash
python "{baseDir}/scripts/summarize.py" "<原始文件路径>" \
  --focus "云原生架构选型理由与踩坑经验" \
  --audience "开发者" \
  --format key_summary \
  --length medium \
  --lang zh \
  [--glossary glossary.txt] [--format-sub srt] [--out-dir DIR]
```

这一步在 `summaries/<name>/` 下产出：

| 文件 | 说明 |
|------|------|
| `context.md` | 转录稿全文（已按术语表更正，若提供术语表） |
| `summary_prompt.md` | 模板 + 本次参数（焦点/受众/长度/语言） |
| `glossary_changes.md` | 术语更正记录（仅当提供术语表且有命中） |
| `timeline.md` | 时间轴骨架（>20 分钟自动生成，分段待补要点） |
| `subtitles.srt` / `.vtt` | 字幕（仅当 `--format-sub`，基于原始转录稿） |

第二步：生成摘要

1. 读取 `summaries/<name>/context.md`（全文）。
2. 读取 `summaries/<name>/summary_prompt.md`（模板与参数）。
3. 由当前代理会话的模型按模板生成摘要。
4. 用 `write` 工具写入 `summaries/<name>/summary.md`。

第三步（可选）：输出 HTML

```bash
python "{baseDir}/scripts/render_html.py" "summaries/<name>/summary.md" --title "会议记录"
```

- 把摘要渲染成同目录同名的 `.html`，双击即可用浏览器独立打开。
- 纯 Python 标准库，内联 CSS、无外部依赖，离线可用。
- `--out` 指定输出路径，`--title` 指定标题（默认取第一个一级标题或文件名），`--meta` 指定标题下方元信息。

**隐私说明：** 转录阶段音频不出本机；摘要阶段默认把转录文本发送到当前代理会话的模型，这是用户预期的行为。

## 脚本用法速查

三个脚本的全部参数列在下方，使用时不需再打开脚本源码确认。

### transcribe.py（阶段一：转写 + 缓存）

```bash
python "{baseDir}/scripts/transcribe.py" <音频/视频路径> [选项]
```

| 选项 | 默认 | 说明 |
|------|------|------|
| `--model` | `base` | Whisper 模型：tiny / base / small / medium / large-v3 |
| `--lang` | `auto` | 强制语言（zh/en/...）；auto 自动检测 |
| `--force` | — | 忽略缓存，强制重新转录 |
| `--device` | `auto` | auto / cpu / cuda；auto 自动探测 GPU，失败回退 CPU |
| `--print` | — | 把转录全文打印到 stdout |
| `--cache-dir` | `~/.cache/zhz-transcript` | 缓存目录 |

### summarize.py（阶段二：准备摘要输入）

```bash
python "{baseDir}/scripts/summarize.py" <原始文件路径> [选项]
```

| 选项 | 默认 | 说明 |
|------|------|------|
| `--model` | `base` | 用于定位缓存的模型名，须与转录时一致 |
| `--focus` | 空 | 总结焦点（空表示全面总结） |
| `--audience` | `通用读者` | 目标受众 |
| `--format` | `key_summary` | 摘要模板：key_summary / meeting / analysis / custom |
| `--template` | — | 自定义模板文件（`--format custom` 时必填） |
| `--length` | `medium` | 摘要长度：short / medium / detailed |
| `--lang` | `zh` | 摘要输出语言：zh / en |
| `--glossary` | — | 术语表 glossary.txt 路径 |
| `--timeline` | `auto` | on / off / auto；auto 表示 >20 分钟自动生成 |
| `--format-sub` | — | 导出字幕：srt / vtt（基于原始转录稿） |
| `--out-dir` | `summaries/<name>/` | 输出目录 |
| `--cache-json` | — | 直接指定转录稿 JSON 路径（跳过内容哈希） |
| `--cache-dir` | `~/.cache/zhz-transcript` | 缓存目录 |

> **缓存定位**：summarize.py 默认按「文件内容 SHA-256 + 模型名」找缓存；精确模型名不存在时，会回退到同内容哈希的任一缓存。因此转录用 `--model small` 时，总结也应传 `--model small`，否则可能命中其他模型的缓存。

### render_html.py（摘要转 HTML）

```bash
python "{baseDir}/scripts/render_html.py" <summary.md> [选项]
```

| 选项 | 默认 | 说明 |
|------|------|------|
| `--title` | 第一个一级标题或文件名 | 页面标题 |
| `--out` | 同目录同名 `.html` | 输出 HTML 路径 |
| `--meta` | — | 标题下方元信息 |
| `--lang` | `zh` | HTML lang 属性 |

## 术语表 glossary.txt

格式：每行一条 `错误词 -> 正确词`，`#` 开头为注释。支持分隔符：Tab、`->`、`=>`、`→`、`=`、`：`（全角冒号）。示例见 `examples/glossary.example.txt`。

关键约束：**术语表只更正摘要用的文本，不改原始转录稿缓存**；所有更改记录在 `glossary_changes.md`。

## 长内容时间轴

内容 >20 分钟自动生成 `timeline.md`（5 分钟一段的骨架）。生成摘要时，为每个时间段补一句要点，使长内容摘要带时间定位。

## 典型用法

```bash
# 1) 转写并缓存（首次）
python "{baseDir}/scripts/transcribe.py" "D:/pony/podcast-ep12.mp3" --model small

# 2) 总结（聚焦云原生选型与踩坑）
python "{baseDir}/scripts/summarize.py" "D:/pony/podcast-ep12.mp3" \
  --focus "云原生架构选型理由与踩坑经验" --format key_summary --lang zh

# 3) 换角度（只提取行动项），完全跳过转录
python "{baseDir}/scripts/summarize.py" "D:/pony/podcast-ep12.mp3" \
  --focus "只提取行动项" --format meeting --glossary glossary.txt --format-sub srt

# 4) 摘要转 HTML（可独立打开）
python "{baseDir}/scripts/render_html.py" "summaries/podcast-ep12/summary.md"
```

每次换角度总结，脚本都会从缓存命中转录稿，只用修改 `--focus` / `--format` / `--length` 重跑 `summarize.py` 即可。

技能主页：http://openclaw.bjbook.net/

## 注意事项

- 脚本用 Python `logging` 输出，`[错误]` 前缀表示 stderr 错误。
- Windows 下子进程用 `CREATE_NO_WINDOW` 隐藏 ffmpeg 窗口。
- 缓存按内容哈希，文件改名或移动不影响命中；改内容（重新编辑/裁剪）会生成新哈希。
- 转录稿缓存永久保留，`~/.cache/zhz-transcript/` 可手动清理。
