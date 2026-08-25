---
name: adsturbo-video-enhance
description: Clean up a video without changing its content: remove watermarks, logos and burnt-in subtitles, upscale to 2K/4K, add or translate subtitles. 画面内容不变，只让成片更干净：去水印、去 logo、去硬字幕、提升分辨率到 2K/4K、添加或翻译字幕。
---
# AdsTurbo 视频精修

画面内容不动，只让成片更干净：去水印、提分辨率、处理字幕。

## 什么时候用这个 skill

用户说「去水印」「去 logo」「去字幕」「4K」「提升画质」「高清化」「超分」「加字幕」「字幕翻译」时用它。

要**改掉画面里的元素**（换人、换语言配音）用 `adsturbo-video-transform`——那是改内容，这里只做清理。

## 前置条件

- Python 3.8+，`pip install -r scripts/requirements.txt`
- 环境变量 `ADSTURBO_API_KEY`（在 https://www.adsturbo.ai 获取）
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
