---
name: adsturbo-video-transform
description: Swap out one element of a video: replace the on-screen person, drive a static portrait with a reference video's motion, or translate the whole video into another language. 换掉视频里的某个元素：把出镜人物换成另一个人、用参考视频的动作驱动静态人像、把整条视频翻译成另一种语言。
---
# AdsTurbo Video Transform

Replace an element in a video: the person, the motion, or the language.

## When to use this skill

Use it when the user says "swap the character", "swap the person", "face swap", "translate the video", "translate to English", "motion control", or "make this photo move".

For pure quality, watermark, or subtitle issues, use `adsturbo-video-enhance` instead — that's cleanup, this is content transformation.

## Prerequisites

- Python 3.8+, `pip install -r scripts/requirements.txt`
- Environment variable `ADSTURBO_API_KEY` (obtain at https://adsturbo.ai?channel=clawhub)
- Optional `ADSTURBO_BASE_URL`, defaults to `https://adsturbo.ai/klian/novartapi`

## Choosing a command

```
What does the user want to replace?
├─ The on-screen person (keep the motion/scene) → character-swap
├─ Make a still portrait perform a reference motion → motion-control
└─ The language (re-dub with lip sync)            → translate
```

```bash
python3 scripts/video_transform.py character-swap \
  --video-url https://.../original.mp4 --image-url https://.../new-person.jpg

python3 scripts/video_transform.py motion-control \
  --video-url https://.../dance.mp4 --image-url https://.../portrait.jpg

python3 scripts/video_transform.py translate \
  --video-url https://.../clip.mp4 --target-lang en
```

`character-swap` and `motion-control` take similar-looking parameters with opposite meanings — don't mix them up:

| | Video provides | Image provides |
|---|---|---|
| `character-swap` | Scene and footage | The new person |
| `motion-control` | The motion | The portrait to be driven |

Full parameter reference: [references/video_transform.md](references/video_transform.md).

## Hard constraint: assets must be public URLs

`--video-url` and `--image-url` **do not accept local file paths**:

```bash
python3 scripts/upload.py file ./clip.mp4
python3 scripts/upload.py image ./person.jpg
```

You can also chain a previous task's output via `--workspace-id`. See [references/upload.md](references/upload.md) for details.

## Handling async tasks

Everything is async; by default the script submits and then auto-polls until the result is ready.

- On timeout: run `query --workspace-id <id>` to keep waiting — **do not resubmit**. The task is still running, and resubmitting will double-charge credits.
- To submit without waiting: use `--no-wait`.

See [references/work.md](references/work.md) for details.

## When replying to the user

- Give the video link directly — don't mention script names, command lines, JSON, or exit codes
- After submitting, state an estimated duration: character swap and motion control take 3-5 minutes, translation takes 5-10 minutes
- For character swap, if the source has multiple shots or the same person changing outfits, later shots may not swap cleanly — in that case, suggest the user split the video into single shots and process them separately; this works better than rerunning the whole clip
- When the user says "translate the video", confirm whether they want re-dubbing (this skill) or just adding foreign-language subtitles (`subtitle` in `adsturbo-video-enhance`)

## Capability boundaries

| What the user wants | Use |
|---|---|
| Remove watermark / 4K / add subtitles | `adsturbo-video-enhance` |
| Generate a new video | `adsturbo-video-generation` |
| Replicate a reference video | `adsturbo-ad-clone` |
| Digital human voiceover / lip sync | `adsturbo-digital-human` |
| Swap a character in an image | `adsturbo-image` |

---

# AdsTurbo 视频改造

换掉视频里的某个元素：人物、动作、语言。

## 什么时候用这个 skill

用户说「换角色」「换个人」「换脸」「视频翻译」「翻译成英文」「动作控制」「让这张照片动起来」时用它。

只是画质、水印、字幕的问题用 `adsturbo-video-enhance`——那是清理，这里是改内容。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://adsturbo.ai?channel=clawhub 获取）
- 可选 `ADSTURBO_BASE_URL`，默认 `https://adsturbo.ai/klian/novartapi`

## 命令怎么选

```
用户要换掉什么？
├─ 出镜的人（保留动作场景）  → character-swap
├─ 让静态人像做出参考动作    → motion-control
└─ 语言（重新配音对口型）    → translate
```

```bash
python3 scripts/video_transform.py character-swap \
  --video-url https://.../original.mp4 --image-url https://.../new-person.jpg

python3 scripts/video_transform.py motion-control \
  --video-url https://.../dance.mp4 --image-url https://.../portrait.jpg

python3 scripts/video_transform.py translate \
  --video-url https://.../clip.mp4 --target-lang en
```

`character-swap` 和 `motion-control` 参数长得一样但含义相反，别搞混：

| | 视频提供 | 图片提供 |
|---|---|---|
| `character-swap` | 画面与场景 | 新的人 |
| `motion-control` | 动作 | 被驱动的人像 |

完整参数见 [references/video_transform.md](references/video_transform.md)。

## 硬约束：素材只收公网 URL

`--video-url` `--image-url` **不接受本地文件路径**：

```bash
python3 scripts/upload.py file ./clip.mp4
python3 scripts/upload.py image ./person.jpg
```

也可以用 `--workspace-id` 接上一个任务的产物。详见 [references/upload.md](references/upload.md)。

## 异步任务怎么处理

全部异步，脚本默认提交后自动轮询到出结果。

- 超时了：`query --workspace-id <id>` 接着等，**不要重新提交**——任务还在跑，重交会重复扣费
- 只想提交不等：`--no-wait`

详见 [references/work.md](references/work.md)。

## 回复用户时

- 直接给视频链接，不要提脚本名、命令行、JSON 或退出码
- 提交后说一句预计时长：换角色和动作控制 3–5 分钟，翻译 5–10 分钟
- 换角色遇到多镜头、同一人换装出现的素材，后段镜头可能换不干净——这时建议用户把视频裁成单镜头分别处理，比重跑整条更有效
- 用户说「翻译视频」时确认要的是重新配音（这里）还是只加外语字幕（`adsturbo-video-enhance` 的 `subtitle`）

## 能力边界

| 用户想要 | 该用 |
|---|---|
| 去水印 / 4K / 加字幕 | `adsturbo-video-enhance` |
| 生成新视频 | `adsturbo-video-generation` |
| 照着参考视频复刻 | `adsturbo-ad-clone` |
| 数字人口播 / 对口型 | `adsturbo-digital-human` |
| 图片换角色 | `adsturbo-image` |
