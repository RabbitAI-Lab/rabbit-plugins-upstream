# 视频精修 / Video Enhance

脚本：`scripts/video_enhance.py`

画面内容不变，只让成片更干净。要**改动画面里的元素**（换人、换语言）属于另一个域，见 `adsturbo-video-transform`。

## 命令一览

| 命令 | 做什么 | 接口线 |
|---|---|---|
| `upscale` | 提升分辨率 / 4K | v1 |
| `remove-object` | 去水印、去 logo、去杂物 | v1 |
| `subtitle` | 加字幕、翻译字幕 | v1 |
| `enhance` | 提升分辨率，可显式指定目标分辨率 | v2beta |
| `erase` | 消除，额外支持去硬字幕 | v2beta |

## upscale / enhance — 提升分辨率

```bash
python3 scripts/video_enhance.py upscale --video-url https://.../clip.mp4

# 想指定目标分辨率时用 v2beta 线
python3 scripts/video_enhance.py enhance --video-url https://.../clip.mp4 \
  --resolution 4k --duration 15
```

两条线做的是同一件事。`upscale` 参数最少，交给服务端定；`enhance` 多了 `--resolution` 和 `--duration`（源视频时长，用于计费预估）。默认选 `upscale`，用户明确要 2K/4K 时用 `enhance`。

## remove-object / erase — 消除

```bash
# 去水印
python3 scripts/video_enhance.py remove-object --video-url https://.../clip.mp4

# 去硬字幕（烧死在画面里的字幕）
python3 scripts/video_enhance.py erase --video-url https://.../clip.mp4 --method rm_subtitle
```

`erase --method` 两个取值：

- `inpainting`（默认）——去水印、logo、杂物，与 `remove-object` 等价
- `rm_subtitle`——**去掉烧进画面的硬字幕**，这是 v1 线没有的能力

去硬字幕后常接 `subtitle` 换一版新语言的字幕，这是视频出海的常规组合。

## subtitle — 加/翻译字幕

```bash
python3 scripts/video_enhance.py subtitle --video-url https://.../clip.mp4 \
  --source-language zh --translate-language en
```

- `--source-language` 源语言，留空则自动识别
- `--translate-language` 目标语言，留空则只加原文字幕不翻译
- `--subtitle-format` 字幕格式
- `--style-type` 字幕样式

只换语言的**配音**而不是字幕，用 `adsturbo-video-transform` 的 `translate`。

## 用 workspace_id 串联

所有命令都可以用 `--workspace-id` 代替 `--video-url`，直接拿上一个任务的产物当输入，省掉中转下载：

```bash
python3 scripts/video_enhance.py erase --workspace-id ws_abc --method rm_subtitle --no-wait
python3 scripts/video_enhance.py subtitle --workspace-id ws_def --translate-language en
```

## 素材必须是公网 URL

```bash
python3 scripts/upload.py file ./clip.mp4
```

## 耗时参考

| 操作 | 预计 |
|---|---|
| `upscale` / `enhance` | 3–5 分钟 |
| `remove-object` / `erase` | 2–5 分钟 |
| `subtitle` | 2–5 分钟 |

耗时随视频时长增长。默认自动轮询；超时用 `query --workspace-id <id>` 续等。
