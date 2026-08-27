---
name: adsturbo-video-enhance
description: Clean up a video without changing its content: remove watermarks, logos and burnt-in subtitles, upscale to 2K/4K, add or translate subtitles. 画面内容不变，只让成片更干净：去水印、去 logo、去硬字幕、提升分辨率到 2K/4K、添加或翻译字幕。
---
# AdsTurbo Video Enhance

Leaves the picture content unchanged and just makes the final cut cleaner: watermark removal, resolution upscaling, subtitle handling.

## When to use this skill

Use it when the user says "remove watermark," "remove logo," "remove subtitles," "4K," "improve quality," "upscale," "enhance resolution," "add subtitles," or "translate subtitles."

To **change elements in the picture** (swap the person, dub into another language) use `adsturbo-video-transform` instead — that changes content, this skill only cleans up.

## Prerequisites

- Python 3.8+, `pip install -r scripts/requirements.txt`
- Environment variable `ADSTURBO_API_KEY` (obtain it from https://adsturbo.ai?channel=clawhub)
- Optional `ADSTURBO_BASE_URL`, defaults to `https://adsturbo.ai/klian/novartapi`

## Choosing a command

```
What does the user want to process?
├─ Watermark / logo / clutter        → remove-object
├─ Hardcoded subtitles burned in     → erase --method rm_subtitle
├─ Blurry footage, need 2K/4K        → upscale (or enhance --resolution 4k)
└─ Add subtitles / translate them    → subtitle
```

```bash
python3 scripts/video_enhance.py remove-object --video-url https://.../clip.mp4
python3 scripts/video_enhance.py erase --video-url https://.../clip.mp4 --method rm_subtitle
python3 scripts/video_enhance.py upscale --video-url https://.../clip.mp4
python3 scripts/video_enhance.py subtitle --video-url https://.../clip.mp4 \
  --source-language zh --translate-language en
```

Watch out for two similarly-named concepts:

- **Remove hardcoded subtitles** (`erase --method rm_subtitle`) = erase subtitles already burned into the picture
- **Add subtitles** (`subtitle`) = generate new subtitles; `--translate-language` translates the subtitles, it does not re-dub the audio

The standard combo for localizing a video is `erase --method rm_subtitle` first, then `subtitle --translate-language en`.

Full parameter reference: [references/video_enhance.md](references/video_enhance.md).

## Hard constraint: only public URLs are accepted

`--video-url` **does not accept local file paths**:

```bash
python3 scripts/upload.py file ./clip.mp4
```

You can also use `--workspace-id` to feed the output of a previous task directly as input, skipping the download-then-upload step. See [references/upload.md](references/upload.md) for details.

## Handling async tasks

Everything is async; by default the script submits the job and polls automatically until the result is ready.

- On timeout: run `query --workspace-id <id>` and keep waiting — **do not resubmit**. The task is still running, and resubmitting will double-charge.
- To submit without waiting: use `--no-wait`.

See [references/work.md](references/work.md) for details.

## When replying to the user

- Give the video link directly; don't mention script names, command lines, JSON, or exit codes
- After submitting, state the expected duration: upscaling 3–5 minutes, removal 2–5 minutes, subtitles 2–5 minutes, longer for longer videos
- When the user says "remove subtitles," confirm first whether they mean erasing existing hardcoded subtitles or skipping new subtitles — these are very different things

## Capability boundaries

| User wants | Use |
|---|---|
| Swap out the person on screen | `adsturbo-video-transform` |
| Video translation (re-dub with lip sync) | `adsturbo-video-transform` |
| Generate a new video | `adsturbo-video-generation` |
| Replicate a reference video | `adsturbo-ad-clone` |
| Digital human voiceover | `adsturbo-digital-human` |
| Image watermark removal / image upscaling | `adsturbo-image` |

---

# AdsTurbo 视频精修

画面内容不动，只让成片更干净：去水印、提分辨率、处理字幕。

## 什么时候用这个 skill

用户说「去水印」「去 logo」「去字幕」「4K」「提升画质」「高清化」「超分」「加字幕」「字幕翻译」时用它。

要**改掉画面里的元素**（换人、换语言配音）用 `adsturbo-video-transform`——那是改内容，这里只做清理。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://adsturbo.ai?channel=clawhub 获取）
- 可选 `ADSTURBO_BASE_URL`，默认 `https://adsturbo.ai/klian/novartapi`

## 命令怎么选

```
用户要处理什么？
├─ 水印 / logo / 杂物      → remove-object
├─ 烧死在画面里的硬字幕     → erase --method rm_subtitle
├─ 画质太糊、要 2K/4K      → upscale（或 enhance --resolution 4k）
└─ 要加字幕 / 翻译字幕      → subtitle
```

```bash
python3 scripts/video_enhance.py remove-object --video-url https://.../clip.mp4
python3 scripts/video_enhance.py erase --video-url https://.../clip.mp4 --method rm_subtitle
python3 scripts/video_enhance.py upscale --video-url https://.../clip.mp4
python3 scripts/video_enhance.py subtitle --video-url https://.../clip.mp4 \
  --source-language zh --translate-language en
```

注意区分两组同名概念：

- **去硬字幕**（`erase --method rm_subtitle`）= 抹掉已经烧进画面的字幕
- **加字幕**（`subtitle`）= 生成新字幕；`--translate-language` 是翻译字幕，不是重新配音

视频出海的常规组合是先 `erase --method rm_subtitle` 再 `subtitle --translate-language en`。

完整参数见 [references/video_enhance.md](references/video_enhance.md)。

## 硬约束：素材只收公网 URL

`--video-url` **不接受本地文件路径**：

```bash
python3 scripts/upload.py file ./clip.mp4
```

也可以用 `--workspace-id` 直接拿上一个任务的产物当输入，省掉下载再上传。详见 [references/upload.md](references/upload.md)。

## 异步任务怎么处理

全部异步，脚本默认提交后自动轮询到出结果。

- 超时了：`query --workspace-id <id>` 接着等，**不要重新提交**——任务还在跑，重交会重复扣费
- 只想提交不等：`--no-wait`

详见 [references/work.md](references/work.md)。

## 回复用户时

- 直接给视频链接，不要提脚本名、命令行、JSON 或退出码
- 提交后说一句预计时长：超分 3–5 分钟，消除 2–5 分钟，字幕 2–5 分钟，长视频更久
- 用户说「去字幕」时先确认是抹掉原有硬字幕还是不要新字幕——这两件事差别很大

## 能力边界

| 用户想要 | 该用 |
|---|---|
| 换掉出镜的人 | `adsturbo-video-transform` |
| 视频翻译（重新配音对口型） | `adsturbo-video-transform` |
| 生成新视频 | `adsturbo-video-generation` |
| 照着参考视频复刻 | `adsturbo-ad-clone` |
| 数字人口播 | `adsturbo-digital-human` |
| 图片去水印 / 图片高清放大 | `adsturbo-image` |
