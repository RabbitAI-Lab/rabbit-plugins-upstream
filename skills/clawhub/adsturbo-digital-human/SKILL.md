---
name: adsturbo-digital-human
description: Turn a script into a talking avatar: choose a platform digital human, clone a custom one from a photo and voice sample, or lip-sync a single portrait to an audio track. Includes TTS voiceover and avatar management. 让虚拟人把文案念出来：可选平台数字人形象、用照片+声音克隆专属形象，或直接给一张人像加一段音频做对口型。含 TTS 配音与形象管理。
---
# AdsTurbo 虚拟人口播

让一个虚拟人形象把文案念出来，产出口播视频。

## 什么时候用这个 skill

用户说「数字人」「口播」「让 XX 说这段话」「用我的照片做个数字人」「对口型」「配音」「克隆声音」时用它。

要凭空生成画面（不涉及人说话）用 `adsturbo-video-generation`；要把已有视频里的人换掉用 `adsturbo-video-transform`。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://www.adsturbo.ai 获取）
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
