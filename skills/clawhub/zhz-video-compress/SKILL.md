---
name: zhz-video-compress
description: 视频整理与高效压缩。递归扫描目录或处理单个视频，用 ffmpeg 转 H.265(默认)/H.264 大幅压缩体积，自动跳过已压缩文件（comment 标志 + 台账记录 + 低码率/小文件过滤），压缩后校验时长与流，无收益或失败自动保留原片。支持 dry-run 预览、默认保留原片（输出到同目录 _compressed 文件或 `--out-dir`）、`--replace` 原地替换、按拍摄年月归档整理。当用户要求"压缩视频""视频瘦身""整理视频目录""video compress""批量转 H265""节省磁盘空间"时使用。Use when user asks to compress videos, batch-transcode a video folder, or organize/slim down video files.
homepage: http://openclaw.bjbook.net/
---

# 视频整理与高效压缩

核心脚本 `scripts/video_compress.py` 是**纯 Python 标准库**实现，只依赖系统里的 `ffmpeg`/`ffprobe`，
**可脱离 OpenClaw 独立运行**（直接 `python video_compress.py <路径>` 即可）。

## 前置检查

1. 确认 ffmpeg 可用：`ffmpeg -version`。缺失则先安装（Windows: `winget install ffmpeg`），或用环境变量 `FFMPEG_PATH`/`FFPROBE_PATH` 指定可执行文件。
   - **完成标准**：`ffmpeg -version` 与 `ffprobe -version` 均能输出版本号。
2. 确认目标路径存在，且有足够磁盘空间（保留原片输出时需约等于源文件大小的临时空间；`--replace` 原地替换也需约等于源文件大小的临时空间）。

## 标准流程

始终**先 dry-run 预览，确认无误再实际执行**。脚本路径相对本 SKILL.md 解析。

1. 预览将要处理的文件：

   ```
   python {baseDir}/scripts/video_compress.py "D:\Videos" --dry-run
   ```

   - **完成标准**：打印出待压缩 / 跳过清单及每个文件的分辨率、编码、体积、码率。

2. 与用户确认参数后正式执行（**默认保留原片**：输出到同目录 `*_compressed` 文件，或用 `--out-dir` 指定输出目录；**不会替换原视频**）：

   ```
   python {baseDir}/scripts/video_compress.py "D:\Videos"
   # 输出到指定目录（原片保留不动）
   python {baseDir}/scripts/video_compress.py "D:\Videos" --out-dir "E:\Compressed"
   # 只有显式要求原地替换时才用 --replace（会覆盖原片）
   python {baseDir}/scripts/video_compress.py "D:\Videos" --replace
   ```

   - **完成标准**：进程退出码 0，汇总行显示"压缩完成 N | 跳过 M | 失败 0"，并打印节省的总空间。

3. 报告结果：转述汇总（完成/跳过/无收益/失败数量、总节省空间与百分比、耗时）。

## 关键行为（无需额外配置即生效）

- **已压缩不再压缩**：三重判定，命中任一即跳过
  - **comment 标志**（最可靠）：压缩时向文件 metadata 的 `comment` 字段追加
    `zhz-video-compress|v1|h265|crf28|preset|时间戳`（原有 comment 内容会保留，用 `;` 拼接；
    `--force` 重压只更新标志、不重复堆叠）。comment 跟随文件本身，MP4/MOV/MKV 均原生支持，
    跨目录/跨机器也能识别；
  - 台账 `.video_compress_ledger.json`（记录于扫描根目录）中已有该文件的 size+duration 指纹；
  - 文件小于 `--min-size`（默认 10MB）或码率低于 `--skip-below-kbps`（默认 300kbps）。
- **安全优先**：先写临时文件 `.vcompress_tmp_*`，压缩后校验（能否解析、是否含视频流、时长是否一致），
  通过才落盘；失败或**压缩收益 <5%** 一律保留原片。中途 Ctrl+C 不会损坏原件。
  **默认保留原片**，不会替换原视频；只有 `--replace` 才会原地替换原片（且仍需临时文件校验通过才覆盖）。
- 音频为 AAC/MP3 时直接复制不转码，其余转 AAC；字幕在 MP4 中转 mov_text，MKV 中直接复制。
- 支持 15 种常见视频扩展名，含 `.dav` 等可用 `--extensions` 追加。

## 画质与速度档位

压缩必须重新编码视频。脚本把底层编码参数封装成语义化档位，无需了解 ffmpeg 选项：

| 场景 | 命令片段 |
|------|----------|
| 体积优先（默认，最常用） | `--quality small`（H265） |
| 画质与体积平衡 | `--quality balanced`（H265） |
| 最小体积 | `--quality smallest`（H265） |
| 最佳画质（兼容性也最好） | `--quality best`（H264） |
| 压缩更快，体积略增 | `--speed fast` |
| 更省体积，耗时更长 | `--speed slow` |

> 高级用户仍可用 `--codec` / `--crf` / `--preset` 覆盖档位，但一般无需使用。

## 常用参数选择

| 场景 | 命令片段 |
|------|----------|
| 4K 降到 1080p | `--max-height 1080` |
| 输出到指定目录（默认保留原片） | `--out-dir "E:\Compressed"` |
| 原地替换原片（谨慎，会覆盖原视频） | `--replace` |
| 按拍摄年月整理归档 | `--organize`（结果进 `YYYY-MM/` 子目录） |
| 强制重压已跳过的文件 | `--force`（忽略 comment 标志与台账） |
| 查看文件是否已被压缩过 | `ffprobe -v quiet -show_entries format_tags=comment -of csv=p=0 文件.mp4` |

## 注意事项

- H.265 压缩速度约为 H.264 的 1/2~1/3，大量视频建议后台运行，用 `exec` 起任务后通过 `process poll` 跟进，不要空转轮询。
- 长任务先告知用户预计耗时（可从 dry-run 的文件总体积估算），再开始执行。
- `--replace` 原地替换模式下若源容器与目标不一致（如 `.avi`→`.mp4`），原文件会被替换为新扩展名的文件。默认（不 `--replace`）时原片始终保留，不会替换。
- `--out-dir` 不能位于扫描目录内部（脚本会拒绝，避免重复扫描输出）。
- 台账文件请勿删除，它是本目录压缩历史的记忆；但即使丢失，文件 comment 标志仍可保证"已压缩不再压缩"。
- 注意：若用第三方工具重新转码压缩过的文件，comment 可能被去掉或保留，行为取决于该工具；必要时用 `--force` 显式控制。

## 验证

任务结束后确认：
1. 汇总行无"失败"，或失败项已逐条说明原因（原片均完好）。
2. 再次以相同命令运行一遍，应全部显示"跳过"（幂等性验证）。
