---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 6cd650e537163cc145060d4639d0c5ad_8acf2cd2920911f1a102525400826444
    ReservedCode1: YKOfapIhQ+4dqS7fC9GboZ2JklfiMR3EKbnGETIWmmBNfeDDLiUD0q/SKiuZe25mO7WZxRNmzU9dTKeAfsOG2z7/vxYjsh5mXIZKVxmEbn/z6py9Msb6wU8StoCOzzvs2J0uvqAtk2ijDwy0v9ZQAVdKBdvx2k4QutwuexiztQ/erHZI49s1lMB0WFg=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 6cd650e537163cc145060d4639d0c5ad_8acf2cd2920911f1a102525400826444
    ReservedCode2: YKOfapIhQ+4dqS7fC9GboZ2JklfiMR3EKbnGETIWmmBNfeDDLiUD0q/SKiuZe25mO7WZxRNmzU9dTKeAfsOG2z7/vxYjsh5mXIZKVxmEbn/z6py9Msb6wU8StoCOzzvs2J0uvqAtk2ijDwy0v9ZQAVdKBdvx2k4QutwuexiztQ/erHZI49s1lMB0WFg=
---

# 三平台视频解析

> 丢个视频链接，还你字幕稿和结构化分析。支持 B站 / 抖音 / 小红书。

## 安装

```bash
pip install faster-whisper yt-dlp openai
```

或初次运行时加 `--auto-install` 让脚本自动安装缺失依赖。whisper base 模型首次运行时自动下载（~74 MB），之后离线。

## 隐私说明

- **基础转写 100% 本地**：不传 `--analyze` 时，所有数据在本地处理，无网络外发。
- **LLM 分析会发送数据**：使用 `--analyze` 时，转写文本会发往你配置的 LLM API。脚本会在发出前打印目标地址。

## 使用

```bash
# 基础转写
python scripts/parse.py "https://www.bilibili.com/video/BV1xxxx"

# 转写 + LLM 深度分析（需配 Key）
python scripts/parse.py "https://v.douyin.com/xxxxx" --analyze

# 更高精度
python scripts/parse.py "<链接>" --model small --analyze
```

## LLM 分析配置

```bash
export LLM_API_KEY=sk-xxx
export LLM_BASE_URL=https://api.openai.com/v1
export LLM_MODEL=gpt-4o
```

兼容 OpenAI / 通义千问 / DeepSeek / 智谱 / Moonshot 等所有 OpenAI 兼容接口。

## 输出

| 文件 | 说明 |
|------|------|
| `逐字稿.txt` | 带时间戳完整转写 |
| `连贯稿.txt` | 无时间戳流畅文本 |
| `分析.json` | 结构化分析（需 `--analyze`） |

## 许可

MIT © 小黑人
*（内容由AI生成，仅供参考）*
