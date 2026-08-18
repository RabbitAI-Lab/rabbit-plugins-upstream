---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 6cd650e537163cc145060d4639d0c5ad_78755056917c11f1bafa525400287e28
    ReservedCode1: Ds+qdYEadoaQsZxHhJXYTMTLzHu0hWIdYQUTWZMCPdSbuIR9+fdDbaHCaiIsuQdpVu4BqIPJ52og68InYsm25Bg1KjWBefXngaGfs7fXLoZyaxwYH36ah/fP4m0hyO2jt5ONUHbCxEZ5VdZfJ1TBZQL+uqd8Ljlbb2+NSdMt4bUWijt/Lpeldy/T5cg=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 6cd650e537163cc145060d4639d0c5ad_78755056917c11f1bafa525400287e28
    ReservedCode2: Ds+qdYEadoaQsZxHhJXYTMTLzHu0hWIdYQUTWZMCPdSbuIR9+fdDbaHCaiIsuQdpVu4BqIPJ52og68InYsm25Bg1KjWBefXngaGfs7fXLoZyaxwYH36ah/fP4m0hyO2jt5ONUHbCxEZ5VdZfJ1TBZQL+uqd8Ljlbb2+NSdMt4bUWijt/Lpeldy/T5cg=
---

# 抖音视频解析（本地版）

> 把抖音视频链接转成中文字幕稿，并自动做重点总结和结构抓取——免费、不需要任何 API key。

> ⚠️ **联网说明**：本技能**需要联网**。运行时会访问抖音/iesdouyin 获取视频并下载 mp4，首次运行还会从 HuggingFace 下载 whisper 模型（~74 MB）。不是纯离线工具。请在明确授权且隐私可控的环境中，解析你拥有或获准使用的视频。

## 安装

```bash
pip install faster-whisper
```

首次运行会自动从 HuggingFace 下载 base 模型（~74 MB），之后缓存到本地不再重复下载。

## 使用

```bash
python scripts/transcribe.py "https://www.douyin.com/video/7634579290163531035"

# 短链也支持
python scripts/transcribe.py "https://v.douyin.com/xa-wFiDUUvVs/"

# 更高精度
python scripts/transcribe.py "<链接>" --model small

# 控制输出目录（推荐）
python scripts/transcribe.py "<链接>" --out-dir ./outputs

# 如需把连贯稿全文打印到终端（默认只打印摘要）
python scripts/transcribe.py "<链接>" --print-transcript
```

## 输出

| 文件 | 说明 |
|------|------|
| `MMDD-<video_id>-逐字稿.txt` | 带时间戳的完整转写 |
| `MMDD-<video_id>-连贯稿.txt` | 无时间戳的流畅文本 |
| `MMDD-<video_id>-报告.html` | 交互式 HTML 分析报告（六大模块） |
| 终端输出 | 连贯稿前 500 字摘要 + 文件路径（默认，不含全文） |

## 后处理

AI 拿到连贯稿文件后会输出：

- 一句话总结
- 3~5 条核心观点
- 结构拆解（口播/营销/教程自适应）
- 金句提取
- 内容判断（立场/可信度/可借鉴点）

## 技术原理

```
抖音链接 → video_id → iesdouyin share API → mp4 直链 → 下载 → faster-whisper 转写
```

纯 CPU 运行，int8 量化，不依赖 ffmpeg / yt-dlp / curl / cookie / 登录。网络请求全部使用 Python 标准库 urllib。

## 安全与隐私声明

- **联网行为**：仅访问 iesdouyin.com（获取视频信息）和抖音视频 CDN（下载 mp4），首次运行从 HuggingFace 下载模型；不向任何第三方发送数据
- **数据落盘**：转写内容会写入本地 txt 和 HTML 文件；视频标题/链接会出现在终端输出中
- **终端输出**：默认只打印连贯稿摘要（前 500 字），不打印全文；确需全文时显式加 `--print-transcript`
- **建议**：避免在共享/受监控环境解析隐私敏感视频；用 `--out-dir` 指定受控输出目录
- **无 API Key**：整个流程不需要任何 API key、cookie 或登录态

## 许可

MIT © 斑斑
*（内容由AI生成，仅供参考）*
