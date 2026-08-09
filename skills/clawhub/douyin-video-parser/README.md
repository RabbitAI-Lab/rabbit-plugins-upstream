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

> 把抖音视频链接转成中文字幕稿，并自动做重点总结和结构抓取——完全本地、免费、不需要任何 API key。

## 安装

```bash
pip install faster-whisper
```

首次运行会自动从 HuggingFace 下载 base 模型（~74 MB），之后不再联网。

## 使用

```bash
python scripts/transcribe.py "https://www.douyin.com/video/7634579290163531035"

# 短链也支持
python scripts/transcribe.py "https://v.douyin.com/xa-wFiDUVVs/"

# 更高精度
python scripts/transcribe.py "<链接>" --model small
```

## 输出

| 文件 | 说明 |
|------|------|
| `MMDD-<video_id>-逐字稿.txt` | 带时间戳的完整转写 |
| `MMDD-<video_id>-连贯稿.txt` | 无时间戳的流畅文本 |
| 终端输出 | 连贯稿全文，供 AI 直接读取做后处理 |

## 后处理

AI 拿到连贯稿后会输出：

- 一句话总结
- 3~5 条核心观点
- 结构拆解（口播/营销/教程自适应）
- 金句提取
- 内容判断（立场/可信度/可借鉴点）

## 技术原理

```
抖音链接 → video_id → iesdouyin share API → mp4 直链 → 下载 → faster-whisper 转写
```

纯 CPU 运行，int8 量化，不依赖 ffmpeg / yt-dlp / cookie / 登录。

## 许可

MIT © 斑斑
*（内容由AI生成，仅供参考）*
