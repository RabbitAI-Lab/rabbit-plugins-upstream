---
name: zhz-video-logo
description: 视频批量加 logo/水印。递归扫描目录或处理单个视频，用 ffmpeg 把公司 logo 或文字水印叠加到固定位置，标识内容来源与版权、防止盗用。水印来源支持图片（PNG/JPG）或文字（用 Pillow 渲染，支持中文）。位置可指定（四角/四边/居中 9 个预设方位或自定义 x,y 像素坐标），透明度可调（0~100%），尺寸可按像素或视频宽度百分比缩放（随分辨率自适应）。自动跳过已加过水印的文件（comment 标志 + 台账记录），先写临时文件校验通过才落盘，默认保留原片（不替换），失败保留原件。支持 dry-run 预览、`--out-dir` 输出到指定目录、`--replace` 原地替换。当用户要求"给视频加logo""加水印""视频打水印""批量加水印""文字水印""版权标识""video logo""watermark"时使用。Use when user asks to add a logo, text watermark, or copyright mark to videos, batch-brand a video folder, or protect course/product videos from reuse.
homepage: http://openclaw.bjbook.net/
---

# 视频批量加 logo/水印

制作了一系列教学视频或产品介绍视频后，通常需要在视频的固定位置加上公司 logo 或水印。
这既能标识内容的来源和版权，也能防止被盗用。手动逐个处理既费时又容易出错，用本脚本一键完成。

**水印来源支持两种：图片 logo（PNG/JPG）或文字水印（如"张老师课程""内部资料""©2026"），文字模式用 Pillow 渲染成透明 PNG 再叠加，支持中文。**

核心脚本 `scripts/video_logo.py` 是**纯 Python 标准库**实现，只依赖系统里的 `ffmpeg`/`ffprobe`（文字模式额外需要 Pillow），
**可脱离 OpenClaw 独立运行**（直接 `python video_logo.py <路径> --logo <图片>` 或 `--text <文字>` 即可）。

## 前置检查

1. 确认 ffmpeg 可用：`ffmpeg -version`（本机为 6.1.1）。缺失则先安装（Windows: `winget install ffmpeg`），或用环境变量 `FFMPEG_PATH`/`FFPROBE_PATH` 指定可执行文件。
   - **完成标准**：`ffmpeg -version` 与 `ffprobe -version` 均能输出版本号。
2. 确认水印来源：
   - **图片**：logo 文件存在，扩展名属于 `.png .jpg .jpeg .bmp .webp .tif .tiff`。强烈推荐带透明通道的 PNG，否则会有一块不透明底色盖住画面。
   - **文字**：`python -c "import PIL"` 能通过（本机 Pillow 12.3.0）。缺失则 `pip install pillow`。
   - **完成标准**：图片能用 `ffprobe` 读尺寸；文字模式能 import PIL 且能找到中文字体（脚本自动探测微软雅黑/黑体/等线等）。
3. 确认目标路径存在，且有足够磁盘空间（保留原片输出时需约等于源文件大小的临时空间；`--replace` 原地替换也需约等于源文件大小的临时空间）。

## 标准流程

始终**先 dry-run 预览，确认无误再实际执行**。脚本路径相对本 SKILL.md 解析。

1. 先问清三件事：**用图片还是文字、放哪个位置、要多透明**。用户没说就用默认（图片右下角 / 文字右下角、100% 不透明、原始大小）。

2. 预览将要处理的文件：

   ```
   # 图片 logo
   python {baseDir}/scripts/video_logo.py "D:\Videos" --logo "D:\assets\company.png" --dry-run
   # 文字水印
   python {baseDir}/scripts/video_logo.py "D:\Videos" --text "张老师课程" --dry-run
   ```

   - **完成标准**：打印出待加水印 / 跳过清单及每个文件的分辨率、编码、体积、时长，首行显示生效的水印来源、位置与透明度。

3. 与用户确认参数后正式执行（**默认保留原片**：输出到同目录 `*_watermark` 文件，或用 `--out-dir` 指定输出目录；**不会替换原视频**）：

   ```
   python {baseDir}/scripts/video_logo.py "D:\Videos" --logo "D:\assets\company.png" --position bottomright --opacity 70
   # 或文字水印
   python {baseDir}/scripts/video_logo.py "D:\Videos" --text "内部资料" --position center --opacity 25
   # 输出到指定目录（原片保留不动）
   python {baseDir}/scripts/video_logo.py "D:\Videos" --logo "D:\assets\company.png" --out-dir "E:\Branded"
   # 只有显式要求原地替换时才用 --replace（会覆盖原片）
   python {baseDir}/scripts/video_logo.py "D:\Videos" --logo "D:\assets\company.png" --replace
   ```

   - **完成标准**：进程退出码 0，汇总行显示"完成 N | 跳过 M | 失败 0"。

4. 报告结果：转述汇总（完成/跳过/失败数量、体积变化、耗时），并说明 logo 位置与透明度。

## 关键行为（无需额外配置即生效）

- **已加过水印不再重复加**：双重判定，命中任一即跳过
  - **comment 标志**（最可靠）：处理时向文件 metadata 的 `comment` 字段追加
    `zhz-video-logo|v2|text|topleft|op60.0|h264|crf20|时间戳`（原有 comment 内容保留，用 `;` 拼接；
    `--force` 重跑只更新标志、不重复堆叠）。标志跟随文件本身，MP4/MOV/MKV 均原生支持，
    跨目录/跨机器也能识别；
  - 台账 `.video_logo_ledger.json`（记录于扫描根目录）中已有该文件的 size+duration 指纹。
- **安全优先**：先写临时文件 `.vlogo_tmp_*`，完成后校验（能否解析、是否含视频流、时长是否一致），
  通过才落盘；失败一律保留原片。中途 Ctrl+C 不会损坏原件。
  **默认保留原片**，不会替换原视频；只有 `--replace` 才会原地替换原片（且仍需临时文件校验通过才覆盖）。
- 音轨为 AAC/MP3 时直接复制不转码，其余转 AAC；字幕在 MP4 中转 mov_text，MKV 中直接复制。
- 支持 14 种常见视频扩展名，其他可用 `--extensions` 追加。

## 位置与透明度参数

| 场景 | 命令片段 |
|------|----------|
| 右下角（默认，最常用） | `--position bottomright` |
| 左上角 | `--position topleft` |
| 居中水印（半透明覆盖） | `--position center --opacity 25` |
| 精确像素坐标 | `--position 100,50`（相对左上角） |
| 调整与边缘的距离 | `--margin 20`（预设方位生效，默认 12px） |
| 半透明水印 | `--opacity 50`（0~100，100=不透明） |
| 水印缩放为固定宽度 | `--logo-width 160` |
| 水印随视频分辨率自适应 | `--logo-scale 12`（宽=视频宽的 12%，优先于 `--logo-width`） |

**9 个预设方位**：`topleft` `top` `topright` `left` `center` `right` `bottomleft` `bottom` `bottomright`

## 文字水印参数

文字模式用 `--text` 指定内容（此时忽略 `--logo`），支持中文。脚本用 Pillow 把文字渲染成带透明通道的 PNG 再叠加，
**不依赖 ffmpeg 的 fontconfig**（本机 fontconfig 已损坏，drawtext 会崩溃，故走 Pillow 路线）。

| 场景 | 命令片段 |
|------|----------|
| 基本文字水印 | `--text "张老师课程"` |
| 指定字体 | `--font C:/Windows/Fonts/simhei.ttf` |
| 指定字号 | `--font-size 64` |
| 指定颜色 | `--font-color yellow` 或 `--font-color #FF0000` 或 `--font-color 255,0,0,128` |
| 版权符号 | `--text "©2026 公司名"` |

字体未指定时自动探测：微软雅黑(msyh.ttc) → 雅黑粗体 → 黑体(simhei) → 等线(Deng) → 宋体(simsun) → Arial，
跨平台兼容（macOS 用 PingFang，Linux 用 Noto CJK）。

## 画质档位

加水印必须重新编码视频。脚本把底层编码参数封装成语义化画质档位，无需了解 ffmpeg 选项：

| 场景 | 命令片段 |
|------|----------|
| 最佳画质 | `--quality best`（H264，画质优先） |
| 默认平衡（兼容性最好） | `--quality balanced`（H264，默认） |
| 体积优先 | `--quality small`（H265） |
| 最小体积 | `--quality smallest`（H265） |

> 高级用户仍可用 `--codec` / `--crf` / `--preset` 覆盖档位，但一般无需使用。

## 其他参数

| 场景 | 命令片段 |
|------|----------|
| 输出到指定目录（默认保留原片） | `--out-dir "D:\Branded"` |
| 原地替换原片（谨慎，会覆盖原视频） | `--replace` |
| 强制重加水印 | `--force`（忽略 comment 标志与台账） |
| 查看文件是否已加过水印 | `ffprobe -v quiet -show_entries format_tags=comment -of csv=p=0 文件.mp4` |

## 注意事项

- **加水印必须重新编码视频**，无法像压缩那样只复制流，因此每个文件都要完整转码一遍，耗时明显长于纯压缩。
  大量视频建议后台运行，用 `exec` 起任务后通过 `process poll` 跟进，不要空转轮询。
- 默认画质档位 `--quality balanced`（H264），目的是**尽量不损失画质**（水印是版权标识，画质优先于体积）。
  若同时要瘦身，可改 `--quality small` 或 `--quality smallest`，或直接配合 `zhz-video-compress` 技能分两步做。
- `--logo-scale` 用 `scale2ref` 按主视频宽度换算，能保证 1080p 和 4K 视频上水印视觉比例一致；
  混有不同分辨率的素材时优先用它，而不是固定 `--logo-width`。
- 水印尺寸大于视频时会盖住大部分画面，建议水印宽度不超过视频宽度的 1/4。
- 文字水印的字号是固定像素值（`--font-size`），不会随视频分辨率缩放；跨分辨率批量加水印时，
  建议改用 `--logo-scale`（先把文字渲染成大图再按比例缩，或直接对不同分辨率分两批处理）。
- `--out-dir` 不能位于扫描目录内部（脚本会拒绝，避免重复扫描输出）。
- `--replace` 原地替换模式下若源容器与目标不一致（如 `.avi`→`.mp4`），原文件会被替换为新扩展名的文件。默认（不 `--replace`）时原片始终保留，不会替换。
- 台账文件请勿删除，它是本目录处理历史的记忆；但即使丢失，文件 comment 标志仍可保证"已加过不再加"。
- 若用第三方工具重新转码处理过的文件，comment 可能被去掉或保留，行为取决于该工具；必要时用 `--force` 显式控制。

## 验证

任务结束后确认：
1. 汇总行无"失败"，或失败项已逐条说明原因（原片均完好）。
2. 抽一个输出文件确认 logo 真的可见（不能只看退出码）：截取一帧查看

   ```
   ffmpeg -y -v error -ss 2 -i "输出文件.mp4" -frames:v 1 "$env:TEMP\check.png"
   ```

   然后用 `read` 工具查看该 PNG，确认 logo 位置与透明度符合预期。
3. 再次以相同命令运行一遍，应全部显示"跳过"（幂等性验证）。
