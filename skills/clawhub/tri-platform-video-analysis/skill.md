# 三平台视频解析

> 丢个视频链接，还你字幕稿、结构化分析和可视化 HTML 报告。支持 B站 / 抖音 / 小红书。

## 安装前须知

- 本脚本依赖 `yt-dlp`、`faster-whisper`、`openai`（仅 `--analyze` 时）。默认**不会**自动安装，缺依赖时会提示你手动执行 `pip install`。
- 如需自动安装，加 `--auto-install` 参数：`python scripts/parse.py "<链接>" --auto-install`
- whisper base 模型首次运行时自动从 HuggingFace 下载（~74 MB），之后不再联网。

## 这条 skill 解决什么

一条命令把任何平台视频变成字幕稿 + 结构化分析。不需要 API Key（转写完全本地），不需要手动听视频做笔记。

核心流程：

1. `yt-dlp` 下载视频（B站/抖音/小红书 全兼容）
2. `faster-whisper` 本地离线转写（CPU、int8、base 模型）
3. 输出逐字稿（带时间戳）+ 连贯稿（无时间戳）
4. **可选**：配 `LLM_API_KEY` 后自动调用 LLM 做结构化分析
5. 始终生成一份可打开直接看的 HTML 报告

## 环境准备

手动安装依赖：

```bash
pip install faster-whisper yt-dlp openai
```

或者初次运行时加 `--auto-install` 让脚本自动处理。

> 首次运行会自动从 HuggingFace 下载 whisper base 模型（~74 MB），之后不再联网。

## 用法

```bash
# 基础转写（B站）
python scripts/parse.py "https://www.bilibili.com/video/BV1xxxx"

# 基础转写（抖音短链）
python scripts/parse.py "https://v.douyin.com/xxxxx"

# 小红书 — 必须使用「分享→复制链接」获取的完整链接（含 xsec_token=）
python scripts/parse.py "https://www.xiaohongshu.com/discovery/item/xxx?xsec_token=..."

# 转写 + LLM 深度分析
python scripts/parse.py "https://www.bilibili.com/video/BV1xxxx" --analyze

# 更高精度
python scripts/parse.py "<链接>" --model small --analyze
```

> **小红书注意**：地址栏直接复制的 URL 不含 `xsec_token` 参数，无法下载。必须通过 APP/网页端「分享」按钮 →「复制链接」获取完整链接。

## 输出

| 文件 | 说明 |
|------|------|
| `MMDD-平台-标题-逐字稿.txt` | 带时间戳的完整转写 |
| `MMDD-平台-标题-连贯稿.txt` | 无时间戳流畅文本 |
| `MMDD-平台-标题-分析.json` | 结构化分析（需 `--analyze`） |
| `MMDD-平台-标题-报告.html` | 可视化 HTML 报告（始终生成） |

## LLM 分析配置（可选）

脚本通过 OpenAI 兼容接口调用 LLM，兼容 90% 以上模型：

```bash
export LLM_API_KEY=sk-xxx
export LLM_BASE_URL=https://api.openai.com/v1   # 默认
export LLM_MODEL=gpt-4o                          # 默认

python scripts/parse.py "<链接>" --analyze
```

也支持命令行传参：

```bash
python scripts/parse.py "<链接>" --analyze --api-key sk-xxx --api-base https://dashscope.aliyuncs.com/compatible-mode/v1 --api-model qwen-plus
```

## AI 分析结构

调用 `--analyze` 后输出：

- **一句话总结**：30 字内概括
- **核心观点**：3~5 条
- **结构拆解**：自适应识别口播/营销/教程类型
- **金句提取**：2~3 句可传播金句
- **内容判断**：立场 / 可信度 / 可借鉴点


## 隐私说明

- **基础转写完全本地**：不传 `--analyze` 时，下载、转写、输出全部在本地完成，不会向任何外部服务器发送数据。whisper 模型首次下载后离线运行。
- **LLM 分析会外发数据**：使用 `--analyze` 时，转写文本会发送到你配置的 LLM API 地址（`LLM_BASE_URL`）。建议使用私有部署或信任的服务商。
- 运行 `--analyze` 时脚本会打印目标 API 地址，让你在数据发出前知晓去向。

## 支持的平台

| 平台 | 链接格式 | 状态 |
|------|---------|------|
| B站 | bilibili.com/video/BVxxx | 已实测 |
| 抖音 | douyin.com/video/xxx, v.douyin.com/xxx | 已实测 |
| 小红书 | xiaohongshu.com/discovery/item/xxx | 已实测（需分享链接含 xsec_token） |

## 案例展示

以下截图均为本工具解析真实视频后生成的 HTML 分析页。

**B站 — 一次性看完地球ONLINE · 十大神级悖论**

![B站案例](screenshots/screenshot_bilibili.png)

**抖音 — 人一旦开窍做什么都顺**

![抖音案例](screenshots/screenshot_douyin.png)

**小红书 — 哑铃单臂划船精讲**

![小红书案例](screenshots/screenshot_xiaohongshu.png)

## 已知限制

- whisper base 模型繁简体会随机选，理解不受影响，如需更高精度用 `--model small`
- 视频时长 >10 分钟建议用 `--model small` 或 `medium`
- 视频号无公开下载接口，暂不支持
- 小红书链接**必须**通过「分享→复制链接」获取（含 `xsec_token=` 参数），地址栏直复的 URL 不含此凭证，yt-dlp 无法提取视频
- yt-dlp 偶遇平台反爬更新，如失败请尝试升级：`pip install -U yt-dlp`
*（内容由AI生成，仅供参考）*
