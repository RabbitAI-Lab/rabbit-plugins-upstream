---
name: "zhz-subtitle"
homepage: http://openclaw.bjbook.net/
description: "音频转录和双语字幕生成。触发词：转录、transcribe、语音转文字、字幕、subtitle、双语字幕。"
---

# 音频转录与视频双语字幕生成器

为视频或音频文件生成转录文本，或自动生成中英文双语 SRT 字幕。

## 环境依赖

| 依赖 | 用途 | 安装方式 |
|------|------|----------|
| Python 3.10+ | 运行脚本 | 系统自带 |
| ffmpeg | 音频提取 | `winget install ffmpeg` / `brew install ffmpeg` |
| faster-whisper | 语音识别 | `pip install faster-whisper`（脚本自动安装） |

## 文件结构

输入文件：`{name}.{ext}`
工作目录：`subtitles/{name}/`（中间文件）
最终输出：`subtitles/{name}.srt`（双语字幕）

| 文件 | 位置 | 说明 |
|------|------|------|
| `{name}.mp3` | `subtitles/{name}/` | 提取的音频 |
| `{name}.transcript.json` | `subtitles/{name}/` | 转录结果（含时间戳） |
| `{name}_translated.json` | `subtitles/{name}/` | 翻译后的 JSON 段落 |
| `{name}.en.srt` | `subtitles/{name}/` | 英文字幕 |
| `{name}.chs.srt` | `subtitles/{name}/` | 中文字幕 |
| **`{name}.srt`** | **`subtitles/`** | **最终双语字幕文件** |

## 选项

| 选项 | 值 | 说明 |
|------|------|------|
| `--model` | tiny, base（默认）, small, medium, large-v3 | Whisper 模型大小 |
| `--lang` | zh, en, auto（默认） | 强制指定语言 |
| `--translated-first` | true / false（默认） | 译文是否排在前面 |
| `--audio-only` | — | 输入已是音频，跳过提取步骤 |

## 两条分支

根据用户需求选择分支：

| 用户请求 | 分支 | 步骤 |
|---------|------|------|
| 音频转文字（不需要字幕） | **转录分支** | 第一步 → 第三步 |
| 视频/音频配双语字幕 | **字幕分支** | 第一步 → 第八步 |

---

## 转录分支（音频转文字）

当用户只需要将音频转为文字，不需要生成字幕文件时使用。

**完成标准：** 输出转录文本。

```bash
python {baseDir}/scripts/transcribe.py "<音频路径>" [model_size] [language]
```

脚本输出 `.transcript.json` 和 `_original.srt`。读取 JSON 中的 segments，将 text 拼接输出给用户即可。

语言参数：`zh`（中文）、`en`（英文）、省略则自动检测。
模型选择：`base` 适合大多数场景，长音频建议 `small` 或 `medium`。

---

## 字幕分支（双语字幕生成）

### 工作流程

### 第一步：环境检查与验证

**完成标准：** 输入文件存在，依赖已就绪。

1. 验证输入文件存在（视频或音频）
2. 检查 ffmpeg 是否可用：`ffmpeg -version`
3. 检查 faster-whisper 是否可用（脚本会自动安装）
4. 创建工作目录 `subtitles/{name}/`
5. 提取输入文件的 name（不含扩展名），后续所有文件均使用此 name

### 第二步：提取音频（音频输入可跳过）

**完成标准：** MP3 音频文件已生成。

```bash
python {baseDir}/scripts/extract_audio.py "<视频路径>" "subtitles/{name}/{name}.mp3"
```

### 第三步：语音转文字

**完成标准：** 生成 `.transcript.json` 和 `_original.srt`。

```bash
python {baseDir}/scripts/transcribe.py "subtitles/{name}/{name}.mp3" [model_size] [language]
```

脚本自动输出到 `subtitles/{name}/` 目录：
- `{name}.transcript.json` — 含时间戳的转录数据
- 根据检测语言生成对应后缀的 SRT：
  - 英文原文 → `{name}.en.srt`
  - 中文原文 → `{name}.chs.srt`

**关键：** 记录检测到的语言（zh/en），第四步据此决定翻译方向。

### 第四步：翻译

**完成标准：** 生成 `{name}_translated.json`。

翻译方向：
- 原文为中文 (zh) → 翻译为英文 (en)
- 原文为英文 (en) → 翻译为中文 (zh)

**执行方式：**

1. Agent 读取转录 JSON，逐段翻译，保持相同的 JSON 结构（start、end、text 字段）
2. 将翻译结果写入 Python 脚本文件：`subtitles/{name}/{name}_translate.py`
3. 执行该脚本生成翻译 JSON：`python subtitles/{name}/{name}_translate.py`

**⛔ 必须通过 Python 脚本生成翻译 JSON：** 翻译文本常含中文引号（""）、书名号等标点，直接 `write` JSON 文件会导致解析失败；`exec -c` 内联 Python 代码会因 shell 转义崩溃。正确做法是将 `json.dump()` 调用写入 `.py` 文件再执行。

**脚本模板：**

```python
import json

data = {
    "language": "zh",  # 或 "en"
    "duration": <音频时长>,
    "segments": [
        {"start": 0.0, "end": 5.0, "text": "翻译文本"},
        # ... 更多段落
    ]
}

with open(r"subtitles/{name}/{name}_translated.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"翻译完成：{len(data['segments'])} 段")
```

**长视频分批翻译：** 当段落数超过 50 条时，将 JSON 中的 segments 拆成多批（每批 30-50 条）翻译，最后合并为完整的 `subtitles/{name}/{name}_translated.json`。避免单次上下文过长导致遗漏或出错。

**纯数字段落不翻译：** 如果某段的 text 是纯数字（如 "1"、"1-20"、"1, 2, 3"），翻译后的 text 保持原文不变。

翻译原则：
- 保持原文语义和语气
- 字幕翻译应简洁，避免过长
- 保留专有名词（人名、地名）
- 教育内容保持术语准确
- 纯数字不翻译，直接保留原文

### 第五步：生成翻译字幕

**完成标准：** 生成翻译语言的 SRT 到 `subtitles/{name}/` 目录。

- 英文翻译 → `subtitles/{name}/{name}.chs.srt`
- 中文翻译 → `subtitles/{name}/{name}.en.srt`

```bash
python {baseDir}/scripts/json_to_srt.py "subtitles/{name}/{name}_translated.json" "subtitles/{name}/{name}.chs.srt"
```

（中文翻译时后缀为 `.chs.srt`，英文翻译时为 `.en.srt`）

### 第六步：合并双语字幕

**完成标准：** 生成最终 `subtitles/{name}.srt`，条目数一致。

```bash
python {baseDir}/scripts/merge_srt.py "subtitles/{name}/{name}.en.srt" "subtitles/{name}/{name}.chs.srt" "subtitles/{name}.srt" [translated_first]
```

默认：英文在前，中文在后。每条字幕显示为两行。合并时自动校验条目数，不一致时输出警告。

**最终文件名与输入文件完全一致，仅后缀从 `.mp4`/`.mp3` 变为 `.srt`，放在 `subtitles/` 目录下。**

### 第七步：验证

**完成标准：** 字幕文件通过格式和双语验证。

```bash
python {baseDir}/scripts/verify_srt.py "subtitles/{name}.srt"
```

验证内容：SRT 格式正确、时间戳无重叠、包含中英文、条目数一致。有错误则修复后重新验证，有警告则报告给用户。

### 第八步：完成报告

```
✅ 双语字幕生成完成！
文件：subtitles/{name}.srt
条目：{count} 条双语字幕
语言：中文 ↔ English
时长：{duration}
原文语言：{original_lang}
```

## 进度清单

```
字幕生成进度：
- [ ] 第一步：环境检查与验证
- [ ] 第二步：提取音频
- [ ] 第三步：语音转文字
- [ ] 第四步：翻译（纯数字不翻译）
- [ ] 第五步：生成翻译字幕
- [ ] 第六步：合并双语字幕
- [ ] 第七步：验证
- [ ] 第八步：完成报告
```

## 注意事项

- HF 镜像：脚本自动设置 `HF_ENDPOINT=https://hf-mirror.com`，解决国内访问问题
- 首次运行自动下载 Whisper 模型到 `~/.cache/huggingface/`
- 模型选择：`base` 适合大多数场景，长视频建议 `small` 或 `medium`
- 支持所有 ffmpeg 能处理的音视频格式
