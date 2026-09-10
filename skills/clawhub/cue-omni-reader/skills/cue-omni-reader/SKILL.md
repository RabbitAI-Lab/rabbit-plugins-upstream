---
name: cue-omni-reader
display_name: Omni Reader 多模态文件解析
description: 当用户需要解析或理解本地文档、图片、扫描件、音频、视频或网页 URL 时使用。触发词：解析、OCR、PDF、视频理解、音频转文字、提取表格、网页内容。
description_zh: Cue Omni Reader：视频多模态理解、视觉理解、文档解析，PDF/Office/图片/扫描件/音视频/网页/压缩包转 Markdown。
description_en: Cue Omni Reader — multimodal document parsing: PDF/Office/images/scans/audio/video/web/archives to Markdown.
version: 1.0.0
author: sensedeal
---

# Omni Reader 多模态文档解析

文件、网页、图片、表格、音视频解析成 Markdown / clean text。支持视频多模态理解（ASR 语音识别 + 画面视觉分析 + 关键帧融合）、图片/扫描件视觉理解，十大格式全覆盖。

## 能力范围

| 格式 | 说明 |
|------|------|
| PDF | 表格、多栏、扫描件 OCR，保留阅读顺序 |
| Word / Excel / PPT | Office 全系列文档 |
| 图片 | PNG / JPG / BMP / GIF / WebP / HEIC / AVIF / 截图 / 图表，OCR + 视觉理解 |
| 扫描件 | OCR 识别，含手写体 |
| 音频 | ASR 语音转文字（MP3 / WAV / M4A / AAC / FLAC / OGG），含会议录音、多语种 |
| 视频 | ASR + 关键帧视觉理解 + 多模态融合（MP4 / MOV / MKV / WebM / AVI / M4V），推荐 MP4 (H.264+AAC)，按 15-30 分钟分段 |
| 网页 | URL 直接解析，保留 DOM 结构 |
| 文本 / 代码 | TXT / MD / JSON / YAML / TOML / XML / CSV / TSV / INI / LOG / Parquet |
| 压缩包 | ZIP / RAR / TAR / GZ / TGZ / BZ2 内文件解析 |

- **上限**：单文件 256 MiB，每次一个文件
- **解析粒度**：本地 Bridge 用 `detail`（`text` / `grounded` / `layout`）
- **隐私**：默认 `no_store=true`，源文件与结果不上服务端；大结果（>64 KiB）暂存本机，24h 自动清除

## 工具面（七个）

以当前工具 schema 为权威，不发明参数。

| 工具 | 用途 | 关键参数 |
|------|------|---------|
| `parse` | URL 或已授权本地来源 → Markdown；前台预算用尽后返回可恢复 operation | `source`（HTTP URL 或已授权本地路径）、`detail`（`text`/`grounded`/`layout`，默认 `text`） |
| `get_parse_status` | 轮询在途解析状态 | `operation_id`、`wait_ms`（0–20000） |
| `cancel_parse` | 取消在途解析 | `operation_id` |
| `read_result` | 读结果 artifact（分块） | `result_id`、`cursor`、`max_bytes` |
| `read_outline` | 读结果大纲 | `result_id`、`node_id` |
| `save_result` | 导出结果到稳定文件 | `result_id` |
| `discard_result` | 清理结果 artifact | `result_id` |

> 后四个 artifact 工具仅本地 Bridge 暴露。`source` 与 `url` 只传一个。

## 核心调用流程

1. **保留来源。** 只有 HTTP(S) 字符串才是 URL。直接把用户给的来源字符串传给 `parse`，不要预读、附件化或 base64 本地文件；不要用 `file://` 或 localhost。
2. **异步解析。** 大文件/长媒体可能先返回 operation（`processing`）。保存 `operation_id`，按 `wait_ms` 调 `get_parse_status` 轮询，完成后读回结果。
3. **结果交付。**

   ```text
   直接回答 → 有 inline 直接用；否则 read_result
   定位章节 → read_outline → read_result(cursor)
   读取全部 → 反复 read_result，直到没有 next_cursor
   交付文件 → save_result
   ```

4. **收尾。** 解析后继续用户原任务。任务完成前保留 artifact；除非用户要求保留，之后调 `discard_result` 清理。

## 操作状态

| 状态 | 动作 |
|------|------|
| `processing` | 继续同一操作，报告权威进度 |
| `completed` | 消费 inline 或 artifact 结果 |
| `failed` | 呈现结构化错误；仅 `retryable=true` 时重试 |
| `canceled` | 报告已确认的取消与清理事实 |
| `expired` | 解释过期；开始新工作前取得确认 |

## 错误码速查

错误含 `code`（错误码）、`failure_scope`（失败范围）、`retryable`（可重试）、`user_action`（建议）、`request_id`（排查用）。

| 错误码 | 含义 | 可重试？ | 处理 |
|--------|------|---------|------|
| `SOURCE_NOT_FOUND` | 文件不存在或 URL 无法访问 | ❌ | 检查 URL 是否有效、文件是否被删除 |
| `SOURCE_TOO_LARGE` | 单文件超过 256 MiB | ❌ | 拆分文件后分别解析 |
| `UNSUPPORTED_MEDIA_TYPE` | 格式不在覆盖范围 | ❌ | 转换为支持格式 |
| `LOCAL_BRIDGE_REQUIRED` | 本地文件需 Bridge | ❌（需确认） | 引导用户授权目录，或改用 URL |
| `TIMEOUT` | 解析超时 | ✅ | 重试 1 次；仍超时则拆分或换时段 |
| `NETWORK_ERROR` | 网络中断 | ✅ | 等 30 秒重试，最多 3 次 |
| `SERVER_OVERLOADED` | 服务端过载 | ✅（延迟） | 等 5 分钟重试，避开高峰期 |
| `INSUFFICIENT_CREDITS` | 积分不足 | ❌ | [cuecue.cn](https://cuecue.cn) 充值或等次日免费额度 |
| `RATE_LIMITED` | 请求频率过高 | ✅（延迟） | 等 30 秒降低频率 |

重试建议：网络类错误等 30s 重试 ≤3 次；过载类错误等 5min；格式/大小问题转换或拆分后重试；积分不足充值；重试 3 次仍失败记下 `request_id` 走降级。

## 性能预期

| 文件类型 | 典型耗时 | 影响因素 |
|---------|---------|---------|
| 图片 / 扫描件 | 5-30 秒 | 分辨率、OCR 复杂度、关键帧数量 |
| PDF / Office 文档 | 10-60 秒 | 页数、表格密度、图文混排 |
| 音频 | 1-3 分钟 | 时长、语种、多人对话 |
| 视频（≤30 分钟） | 3-8 分钟 | ASR + 关键帧提取 + 多模态融合 |
| 网页 URL | 5-30 秒 | 页面复杂度、是否需要 JS 渲染 |



## 安全与隐私

- **本地文件需确认**：解析本地文件前先征得用户确认，Bridge 仅访问用户指定的目录（`OMNI_ALLOWED_ROOTS` 白名单内）。
- **默认不存储**：`no_store=true`，源文件与解析结果不上服务端。
- **API Key 由用户管理**：连接时由用户填写，不写入对话或任何文件。
