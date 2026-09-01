---
name: adsturbo-digital-human
description: Turn a script into a talking avatar: choose a platform digital human, clone a custom one from a photo and voice sample, or lip-sync a single portrait to an audio track. Includes TTS voiceover and avatar management. 让虚拟人把文案念出来：可选平台数字人形象、用照片+声音克隆专属形象，或直接给一张人像加一段音频做对口型。含 TTS 配音与形象管理。
---
# AdsTurbo Digital Human Voiceover

Have a virtual human avatar read a script aloud, producing a talking-head video.

## When to use this skill

Use it when the user says "digital human", "voiceover", "have XX say this", "make a digital human from my photo", "lip sync", "dub", or "clone a voice".

To generate footage out of thin air (with no one speaking) use `adsturbo-video-generation`; to swap out the person in an existing video use `adsturbo-video-transform`.

## Prerequisites

- Python 3.8+, `pip install -r scripts/requirements.txt`
- Environment variable `ADSTURBO_API_KEY` (get it at https://adsturbo.ai?channel=clawhub)
- Optional `ADSTURBO_BASE_URL`, default `https://adsturbo.ai/klian/novartapi`

## First decide where the avatar comes from

This is the single fork point for picking a command:

```
Who does the user want speaking?
├─ Doesn't matter, pick a good-looking one → choose from the actors list → perform
├─ Use my/our own person, reused repeatedly → persona-create to register → perform
└─ Just this one image, one-off             → lipsync
```

```bash
# Platform avatar
python3 scripts/digital_human.py actors --gender female --limit 10
python3 scripts/digital_human.py perform --actor-id act_123 --script "script content"

# Dedicated avatar (photo + optional voice cloning)
python3 scripts/digital_human.py persona-create --photo-url https://.../me.jpg --voice-audio-url https://.../voice.mp3
python3 scripts/digital_human.py perform --actor-id <returned actor_id> --script "script content"

# One-off lip sync
python3 scripts/digital_human.py lipsync --avatar-url https://.../face.jpg --audio-url https://.../voice.mp3
```

Full parameters in [references/digital_human.md](references/digital_human.md).

## Hard constraint: assets must be public URLs only

None of the `--photo-url`, `--avatar-url`, `--audio-url` parameters **accept local file paths**. When the user provides a local file, upload it first:

```bash
python3 scripts/upload.py image ./portrait.jpg
python3 scripts/upload.py audio ./voice.mp3
```

See [references/upload.md](references/upload.md) for details.

## Handling async tasks

`perform` / `persona-create` / `lipsync` are all asynchronous. The scripts poll automatically after submission until a result is ready, so under normal conditions you can just wait.

- On timeout: use `query --workspace-id <id>` to keep waiting — **do not resubmit**. The task is still running, and resubmitting will double-charge.
- To submit without waiting: add `--no-wait`
- To check progress on a batch: `python3 scripts/work.py batch --workspace-ids ws_a ws_b`

See [references/work.md](references/work.md) for details.

## When replying to the user

- Give the result link directly — don't mention script names, command lines, JSON, or exit codes
- After submission, tell the user roughly how long to expect: `perform` 2–5 minutes, `persona-create` 1–3 minutes, `lipsync` 2–5 minutes
- On error, explain the problem in one sentence, then ask whether to retry
- `perform` will fail before `persona-create` completes — check `persona-status` first in that case

## Scope boundaries

This skill only handles "making a digital human speak". The following are out of scope — don't promise them to the user:

| User wants | Use instead |
|---|---|
| Text-to-video / image-to-video | `adsturbo-video-generation` |
| Replicate an existing ad | `adsturbo-ad-clone` |
| Watermark removal / 4K / subtitles | `adsturbo-video-enhance` |
| Character swap / video translation / motion control | `adsturbo-video-transform` |
| Image generation / e-commerce images | `adsturbo-image` |

---

# AdsTurbo 虚拟人口播

让一个虚拟人形象把文案念出来，产出口播视频。

## 什么时候用这个 skill

用户说「数字人」「口播」「让 XX 说这段话」「用我的照片做个数字人」「对口型」「配音」「克隆声音」时用它。

要凭空生成画面（不涉及人说话）用 `adsturbo-video-generation`；要把已有视频里的人换掉用 `adsturbo-video-transform`。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://adsturbo.ai?channel=clawhub 获取）
- 可选 `ADSTURBO_BASE_URL`，默认 `https://adsturbo.ai/klian/novartapi`

## 先判断形象从哪来

这是选命令的唯一分岔点：

```
用户想让谁来说？
├─ 无所谓，挑个好看的        → actors 列表里选 → perform
├─ 用我/我们的人，要反复用   → persona-create 建号 → perform
└─ 就这张图，一次性          → lipsync
```

```bash
# 平台形象
python3 scripts/digital_human.py actors --gender female --limit 10
python3 scripts/digital_human.py perform --actor-id act_123 --script "文案内容"

# 专属形象（照片 + 可选声音克隆）
python3 scripts/digital_human.py persona-create --photo-url https://.../me.jpg --voice-audio-url https://.../voice.mp3
python3 scripts/digital_human.py perform --actor-id <返回的 actor_id> --script "文案内容"

# 一次性对口型
python3 scripts/digital_human.py lipsync --avatar-url https://.../face.jpg --audio-url https://.../voice.mp3
```

完整参数见 [references/digital_human.md](references/digital_human.md)。

## 硬约束：素材只收公网 URL

所有 `--photo-url` `--avatar-url` `--audio-url` 参数**不接受本地文件路径**。用户给本地文件时先上传：

```bash
python3 scripts/upload.py image ./portrait.jpg
python3 scripts/upload.py audio ./voice.mp3
```

详见 [references/upload.md](references/upload.md)。

## 异步任务怎么处理

`perform` / `persona-create` / `lipsync` 都是异步的，脚本默认提交后自动轮询到出结果，正常情况直接等即可。

- 超时了：用 `query --workspace-id <id>` 接着等，**不要重新提交**——任务还在跑，重交会重复扣费
- 只想提交不等：加 `--no-wait`
- 批量查进度：`python3 scripts/work.py batch --workspace-ids ws_a ws_b`

详见 [references/work.md](references/work.md)。

## 回复用户时

- 直接给结果链接，不要提脚本名、命令行、JSON 或退出码
- 提交后告诉用户大概要等多久：`perform` 2–5 分钟，`persona-create` 1–3 分钟，`lipsync` 2–5 分钟
- 出错时用一句话说清是什么问题，再问要不要重试
- `persona-create` 完成前 `perform` 会失败，这时先查 `persona-status`

## 能力边界

这个 skill 只做「让虚拟人说话」。以下不在范围内，不要向用户承诺：

| 用户想要 | 该用 |
|---|---|
| 文生视频 / 图生视频 | `adsturbo-video-generation` |
| 照着一条广告复刻 | `adsturbo-ad-clone` |
| 去水印 / 4K / 字幕 | `adsturbo-video-enhance` |
| 换角色 / 视频翻译 / 动作控制 | `adsturbo-video-transform` |
| 生成图片 / 电商图 | `adsturbo-image` |
