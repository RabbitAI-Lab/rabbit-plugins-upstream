---
name: tinrec-audio2text
description: 支持 MP3、WAV、M4A 等本地音频的云端转写，也可解析受支持平台的公开分享链接，自动下载媒体并导入转写。支持发言人区分，并生成 AI 摘要、会议纪要、章节要点、待办事项和推荐提示词。可浏览 Tinrec 的录音列表和文件夹，按需查看录音详情或逐字稿，上传和导入时可指定文件夹。
---

## 准备

使用 Python 3.9 或更新版本。用户可在自己的站点创建密钥。[CN 版 API Keys](https://tinrec.cn/api-keys) · [海外版 API Keys](https://tinrec.com/api-keys)

将密钥保存到技能目录外的本地文件，每行一个 Key，CLI 读取第一行非空、非注释内容。以下命令在技能目录中执行，并在命令末尾追加 `--api-keys-file /path/to/api-keys`。

直接配置 Key 即可。`mt-cn-` 自动使用 `https://api.tinrec.cn/api`，`mt-global-` 自动使用 `https://api.tinrec.com/api`。历史 `mt-` Key 会先用只读请求识别地区，再执行命令。需要指定测试或自定义环境时，可用 `--base-url` 显式覆盖。

## 浏览录音

当用户想了解 Tinrec 里有哪些内容时，先提供两个入口。用户已指定录音 ID 或文件夹时，可直接打开对应层级。

- **录音列表** → 查看录音概览 → 按录音 ID 查看详情或逐字稿。
- **文件夹列表** → 选择文件夹并查看其中的录音概览 → 按录音 ID 查看详情或逐字稿。

| 用户意图 | 命令 | 返回内容 |
| --- | --- | --- |
| 查看录音列表 | `python3 script/audio2text_cli.py list-recordings` | 录音 ID、文件名、AI 标题、时长、创建时间、来源、所属文件夹和分页 |
| 查看文件夹列表 | `python3 script/audio2text_cli.py list-folders` | 文件夹 ID、名称、录音数量、最近添加的录音和分页 |
| 查看某个文件夹的录音 | `python3 script/audio2text_cli.py list-recordings --folder-id 123` | 与录音列表相同的概览字段，范围限于该文件夹 |
| 查看单条录音的 AI 产出与状态 | `python3 script/audio2text_cli.py detail 456` | 录音详情、AI 总结、章节、待办、推荐提示词及处理状态 |
| 查看逐字稿或谁说了什么 | `python3 script/audio2text_cli.py transcript 456` | 转写正文、发言人标识和发言人信息 |

列表按页返回 JSON，使用 `--page`、`--page-size` 翻页。录音列表可通过 `--filename "项目评审"` 搜索文件名、AI 标题和主题。引用录音或文件夹时优先使用结果中的 `public_id`，也可使用数字 `id`。列表请求使用 `GET /api/audio-list/simple` 和 `GET /api/folders`。只有当用户需要具体内容时，再按目标录音调用 `GET /api/audio-detail/{id}` 或 `GET /api/transcript/{id}`。

## 上传和网络导入

- **本地文件**。运行 `python3 script/audio2text_cli.py upload /path/to/meeting.mp3 --folder-id 123`。支持常见音频格式和有音轨的视频。旧用法 `python3 script/audio2text_cli.py /path/to/meeting.mp3` 仍可使用。
- **分享链接**。运行 `python3 script/audio2text_cli.py import-url "分享链接或含链接的分享文案" --folder-id 123`。适用于 Tinrec 支持的公开平台链接，例如 YouTube、抖音、TikTok、小红书、Bilibili、Instagram、Facebook、X 和快手。

`--folder-id` 可省略。如用户指定的是文件夹名称，先从文件夹列表确认 ID，再提交导入。两个命令默认等待转写和 AI 处理，追加 `--json` 可获得结构化结果，包含总结、章节、待办、推荐提示词、逐字稿、发言人和状态。只需提交时追加 `--no-wait`，获得 `audio_id` 后可用 `detail` 查看进度。

网络导入调用 `POST /api/network-download/resolve` 取得媒体地址和网络任务 ID。CLI 将可下载的音视频文件保存到本地临时目录，上传到 Tinrec 的对象存储，再通过 `POST /api/upload-v2` 提交录音并携带网络任务 ID 和可选的文件夹 ID。处理结束后会清理临时文件。
