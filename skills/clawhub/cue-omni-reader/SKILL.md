---
slug: cue-omni-reader
displayName: Omni Reader 多模态文档解析
description: 用 Cue Omni Reader 将任意文档解析为 Markdown——视频多模态理解（ASR+画面视觉分析+关键帧融合）、图片/扫描件视觉理解、PDF/Office/网页/音视频/压缩包全覆盖。支持 MCP 配置（Claude Desktop / Cursor / Cherry Studio / Trae）和 HTTP API（程序调用），Agent 原生消费。
description_zh: Cue Omni Reader：视频多模态理解、视觉理解、文档解析，PDF/Office/图片/扫描件/音视频/网页/压缩包转 Markdown，支持 MCP 与 HTTP API 两种接入方式。
version: 1.2.1
author: sensedeal
tags: [cue, omni-reader, video-understanding, vision, multimodal, ocr, document-parsing, mcp, 视频解析, 视觉理解, 多模态, 文档解析, OCR]
---

# Omni Reader 多模态文档解析

> 文件、网页、图片、表格、音视频解析成 Markdown / clean text，支持 Agent(MCP) 和 API 集成。视频多模态理解（ASR 语音识别 + 画面视觉分析 + 关键帧融合）、图片/扫描件视觉理解、十大格式全覆盖。

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
| 文本 / 代码 | 纯文本、Markdown、源代码文件（含 JSON / YAML / TOML / XML / Parquet / CSV / TSV / INI / LOG 等） |
| 压缩包 | ZIP / RAR / TAR / GZ / TGZ / BZ2 内文件解析 |

- **上限**：单文件 256 MiB，每次一个文件
- **输出**：`markdown`（默认）/ `hypertext` / `chunks`
- **隐私**：默认 `no_store=true`，源文件和解析结果不上服务端；大结果（>64 KiB）暂存本机，24h 后自动清除
- **进度**：支持 OCR 逐页、ASR 语音转写、关键帧画面识别等阶段进度回调

---

## 接入到你的 Agent / 程序

已有公开或签名 HTTPS URL 时，无需安装本地 Bridge，直接复制 MCP 配置即可使用。

- **在线体验**：网页版 → https://cuecue.cn/hub/omni-reader
- **Agent 集成**：下方 MCP 配置（Claude Desktop / Cursor / Cherry Studio / Trae 等均适用）
- **程序接入**：后端程序走 MCP-over-HTTP，见下方 HTTP API 部分

使用 `parse` 工具，远程 MCP 服务端走既有 `parse_url` 路径；**不要传裸 `oss://`，请先转换为可访问的签名 HTTPS URL。**

### MCP 配置（Claude Desktop / Cursor / Cherry Studio / Trae 等）

HTTPS URL 配置后即可使用，无需额外安装。告诉 Agent 文件 URL 即可。

```json
{
  "mcpServers": {
    "omni-reader": {
      "type": "streamable-http",
      "url": "https://mcp.cuecue.cn/api/omni-reader/mcp/",
      "headers": {
        "Authorization": "Bearer <your-api-key>"
      }
    }
  }
}
```

### HTTP API · curl（MCP-over-HTTP）

```bash
# HTTP API（用同一把 API Key，走 MCP-over-HTTP）
# 已有公开或签名 HTTPS URL 时，无需安装本地 Bridge。
# 远程 MCP 工具名仍为 parse，服务端走既有 parse_url 路径；不要传裸 oss://，请先转换为签名 HTTPS URL。
curl -X POST "https://mcp.cuecue.cn/api/omni-reader/mcp/" \
  -H "Authorization: Bearer <your-api-key>" \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call",
       "params":{"name":"parse","arguments":{"url":"https://...","output":"markdown"}}}'
```

### HTTP API · Python（MCP-over-HTTP）

```python
# HTTP API（MCP-over-HTTP）
# 已有公开或签名 HTTPS URL 时，无需安装本地 Bridge。
# 远程 MCP 工具名仍为 parse，服务端走既有 parse_url 路径；不要传裸 oss://，请先转换为签名 HTTPS URL。
import requests
r = requests.post("https://mcp.cuecue.cn/api/omni-reader/mcp/",
  headers={"Authorization": "Bearer <your-key>",
           "Accept": "application/json, text/event-stream"},
  json={"jsonrpc": "2.0", "id": 1, "method": "tools/call",
        "params": {"name": "parse", "arguments": {"url": "https://...", "output": "markdown"}}})
print(r.json())
```

### 本地文件解析

文件在本机时，Agent 会先说明并征得确认，然后自动安装官方 Bridge（stdio MCP，适用于桌面端 Agent）。Bridge 仅访问你指定的文件/目录。

**手动安装 Bridge（仅在需要时运行，不包含 API Key）：**

```bash
npx -y @cueai/omni-reader-mcp@1.1.0 setup
```

Agent 配置（`~/.claude/mcp.json`）：

```json
{
  "mcpServers": {
    "omni-reader": {
      "command": "npx",
      "args": ["-y", "@cueai/omni-reader-mcp@1.1.0"],
      "env": {
        "CUE_API_KEY": "<your-api-key>"
      }
    }
  }
}
```

配置后在对话中直接使用：

> "用 Omni 解析 ./report.pdf"

**更新与卸载：**

```bash
# 更新到最新版本（重跑 setup 即更新）
npx -y @cueai/omni-reader-mcp@1.1.0 setup

# 卸载 Bridge
npx -y @cueai/omni-reader-mcp uninstall
```

### 前置须知

本 Skill 是 Omni Reader MCP 服务的使用说明书，**实际解析由 Cue 远程服务完成**。以下情况非本 Skill 问题：

- 网络波动导致 MCP 超时 → 重试或换时段
- 服务端临时过载 → 等 5-15 分钟
- 外部数据源不响应 → Cue 会返回结构化错误而非静默失败

遇到问题时，Agent 会根据错误码自动判断是否能重试。详见下方错误码速查。

### 性能预期

| 文件类型 | 典型耗时 | 影响因素 |
|---------|---------|---------|
| 图片 / 扫描件 | 5-30 秒 | 分辨率、OCR 复杂度、关键帧数量 |
| PDF / Office 文档 | 10-60 秒 | 页数、表格密度、图文混排 |
| 音频 | 1-3 分钟 | 时长、语种、多人对话 |
| 视频（≤30 分钟） | 3-8 分钟 | ASR + 关键帧提取 + 多模态融合 |
| 网页 URL | 5-30 秒 | 页面复杂度、是否需要 JS 渲染 |

> 工作日 9:00-10:00 / 16:00-18:00 为高峰期，大文件可能排队 5-15 分钟。夜间和周末 Cue 后端可能有维护窗口。

### 错误码速查

Omni MCP 返回结构化错误，包含 `code`（错误码）、`failure_scope`（失败范围）、`retryable`（是否可重试）、`user_action`（操作建议）、`request_id`（请求 ID，排查用）。

| 错误码 | 含义 | 可重试？ | 处理 |
|--------|------|---------|------|
| `SOURCE_NOT_FOUND` | 文件不存在或 URL 无法访问 | ❌ | 检查 URL 是否有效、文件是否被删除 |
| `SOURCE_TOO_LARGE` | 单文件超过 256 MiB 上限 | ❌ | 拆分文件后分别解析 |
| `UNSUPPORTED_MEDIA_TYPE` | 文件格式不在覆盖范围 | ❌ | 转换为支持格式，参考能力范围表 |
| `LOCAL_BRIDGE_REQUIRED` | 本地文件需要安装 Bridge | ❌（需确认） | Agent 提示后自动安装，或手动 `npx setup` |
| `TIMEOUT` | 解析超时（>3 分钟无进度） | ✅ | 重试 1 次；仍超时则拆分文件或换时段 |
| `NETWORK_ERROR` | 网络连接中断 | ✅ | 等待 30 秒后重试，最多 3 次 |
| `SERVER_OVERLOADED` | 服务端过载 | ✅（延迟） | 等 5 分钟后重试，避开高峰期 |
| `INSUFFICIENT_CREDITS` | 积分不足 | ❌ | [cuecue.cn](https://cuecue.cn) 充值或等次日免费额度 |
| `RATE_LIMITED` | 请求频率过高 | ✅（延迟） | 等 30 秒降低频率 |

### 重试决策

```
收到错误
├─ retryable = true → 按 user_action 建议操作后重试
│   ├─ 网络类 → 等 30s，最多 3 次
│   └─ 过载类 → 等 5min，换时段
├─ retryable = false → 不要重试，改了条件再说
│   ├─ 格式/大小问题 → 转换或拆分文件
│   ├─ 积分不足 → 充值
│   └─ Bridge 未装 → Agent 自动安装
└─ 重试 3 次仍失败 → 记下 request_id，走降级方案
```

---

## 环境要求

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取，复用通用 Cue Key，无需创建 Omni 专用 Key。

MCP 服务目录：`GET https://cuecue.cn/api/mcp-catalog`

---

## 格式转换

Cue 输出 Markdown。安装 pandoc 后可转换为 Word 或 PDF：

```bash
# .md → .docx（Word）
pandoc report.md -o report.docx

# .md → .pdf
pandoc report.md -o report.pdf --pdf-engine=xelatex
```

输出文件与输入同目录、同名、不同后缀。

### 依赖安装

| 目标格式 | 依赖 | macOS | Ubuntu |
|----------|------|-------|--------|
| Word (.docx) | pandoc | `brew install pandoc` | `sudo apt install pandoc` |
| PDF (.pdf) | pandoc + LaTeX | `brew install --cask basictex` | `sudo apt install texlive-xetex` |

---

## 架构说明

本 Skill **不在本地执行解析**。流程是 Agent → Omni Reader MCP 桥接（streamable-http 或本地 npx）→ Cue 解析服务。解析质量和时效取决于 MCP 连接和 Cue 服务状态。

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 你 | 重新生成 Key，更新 `~/.cue/config.json` |
| MCP 连接（streamable-http） | Cue 运维 | 等恢复，或改用本地 npx Bridge |
| 本地 Bridge（npx） | 你 | `npx -y @cueai/omni-reader-mcp setup` 重装，确认 Node.js >= 18 |
| Cue 解析服务 | Cue 运维 | 等恢复，或走降级方案 |

---

## 健康检查

跑解析前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 MCP 连接 ===" && curl -sS --max-time 10 -X POST "https://mcp.cuecue.cn/api/omni-reader/mcp/" -H "Authorization: Bearer $CUE_KEY" -H "Content-Type: application/json" -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}' | python3 -c "import sys,json;r=json.load(sys.stdin);print('已连接 ('+str(len(r.get('result',{}).get('tools',[])))+' 工具)') if 'result' in r else print('连接失败')"
echo "=== 3/3 Node.js ===" && node -v 2>/dev/null && npx -v 2>/dev/null && echo "就绪" || echo "未安装！"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | [cuecue.cn/hub/api-key](https://cuecue.cn/hub/api-key) 重新生成 |
| MCP 连接 | `已连接 (3 工具)` | 等 5 分钟重试，检查网络/DNS |
| Node.js | `就绪` | `brew install node` 或 [nodejs.org](https://nodejs.org) |

---

## 自救指引

### 常见现象速查

Agent 已收到错误码时直接查阅上方"错误码速查"表。以下仅用于没有明确错误码的模糊场景：

| 现象 | 排查方向 | 处理 |
|------|---------|------|
| Agent 说连不上 Omni | MCP 服务是否正常运行 | 跑健康检查三段诊断 |
| 等很久没反应 | 大文件或高峰期 | 先跑诊断确认服务在线；超 15 分钟则重试 |
| 解析结果看起来缺内容 | 复杂排版/跨页切分 | 换 `hypertext` 输出，或分页解析 |
| 视频解析只有字幕没有画面描述 | 默认输出模式 | 指定 `output: "hypertext"` 获取关键帧视觉分析 |
| oss:// 链接报错 | 裸 oss URL | 先转换为签名 HTTPS URL 再传 |
| 已经在对话里发了文件但还是报错 | 文件路径未传递 | 把文件路径作为文本告诉 Agent，如 `./report.pdf` |

### 调度建议

| 时段 | 建议 |
|------|------|
| 工作日 10:00-16:00 | 最佳时段，3-8 分钟完成 |
| 工作日 9:00-10:00 / 16:00-18:00 | 高峰期，大文件（>100MiB）避开 |
| 夜间/周末 | 可能有维护，跑前先诊断 |
| 首次使用 | 跑健康检查三段诊断确认环境就绪 |
| 连续失败 ≥2 次 | 停 15 分钟，记下 request_id 后重试 |

---

## 降级方案

Cue Omni Reader 长时间不可达时的手动替代渠道：

| 渠道 | 覆盖 | 费用 |
|------|------|------|
| [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) | 图片/扫描件 OCR | 免费开源 |
| [SmallPDF](https://smallpdf.com) | PDF 转文本/Word | 部分免费 |
| macOS 预览 | PDF/图片文字复制 | 系统自带 |
| [iLovePDF](https://www.ilovepdf.com) | PDF 转换 | 部分免费 |
| 手动转录 | 音视频文字提取 | 免费 |

---

## FAQ

**Q: MCP 和 API 怎么选？**
A: Agent（Claude Desktop / Cursor / Cherry Studio / Trae 等）用 MCP 配置，复制 JSON 到 `mcp.json`；程序后端直接调 HTTP API，用 curl 或 Python。

**Q: 本地文件怎么解析？Bridge 安全吗？**
A: Agent 会先征得你确认，然后自动安装官方 Bridge。Bridge 仅访问你指定的文件/目录，不会扫描其他位置。本地模式下文件直传 III S，不经过 Cue 服务端。默认 `no_store=true`。

**Q: 解析失败了怎么办？**
A: MCP 返回结构化错误（含错误码、失败范围、是否可重试、用户操作建议），Agent 可根据错误类型自动决策——超时可重试、格式不支持则提示转换、积分不足则提示充值。不需要手动排查。

**Q: 怎么更新 Bridge？**
A: 重跑 `npx -y @cueai/omni-reader-mcp@1.1.0 setup` 即更新到最新版。卸载用 `npx -y @cueai/omni-reader-mcp uninstall`。

**Q: 为什么不能传 oss:// URL？**
A: 远程 MCP 服务端走 `parse_url` 路径，需要可公开访问的签名 HTTPS URL。裸 `oss://` 请先转换为签名 URL。

**Q: 解析大文件会超时吗？**
A: 单文件上限 256 MiB。PDF 建议按页拆分，单份不超过 200 MiB，避免在跨页表格中间切分。视频建议按 15-30 分钟分段，还能提高关键帧覆盖率；推荐 MP4 (H.264 + AAC)。

**Q: 支持哪些文件类型？**
A: PDF / Word / Excel / PPT / 图片（PNG/JPG/BMP/GIF/WebP/HEIC/AVIF）/ 音频（MP3/WAV/M4A/AAC/FLAC/OGG）/ 视频（MP4/MOV/MKV/WebM/AVI/M4V）/ 网页 / 文本与代码（TXT/MD/JSON/YAML/TOML/XML/CSV/TSV/INI/LOG/Parquet）/ 压缩包（ZIP/RAR/TAR/GZ/TGZ/BZ2）。
