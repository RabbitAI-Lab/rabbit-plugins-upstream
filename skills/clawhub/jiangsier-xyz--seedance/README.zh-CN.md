# seedance

一个 Agent 技能，使用 **doubao-seedance-2.0** 模型生成视频（文生视频、图生视频、首尾帧生视频）。当你提出“生成视频”或提到“seedance”时触发，从你的请求中提取选项、与你确认后，调用同步封装脚本：创建任务、轮询直到完成、返回视频地址。

它是一个标准的 `SKILL.md` 技能，可运行于任何兼容的 Agent 运行时（Claude Code、OpenClaw 等）。

视频生成在后端是异步的（提交任务 → 轮询状态直到完成），本技能把它封装成一次调用。

## 目录结构

```
seedance/
├── SKILL.md            # 技能定义 + Agent 指引
├── scripts/
│   ├── seedance        # venv 入口封装（自动创建 .venv 并运行 seedance.py）
│   ├── seedance.py     # 同步封装脚本（仅依赖 Python 标准库）
│   └── test_seedance.py
├── reference.md        # 火山方舟官方视频生成文档
├── requirements.txt    # alibabacloud_oss_v2（仅本地图片上传需要）
├── README.md           # 英文 README
└── README.zh-CN.md     # 中文 README（本文件）
```

技能中的脚本路径均相对于技能目录（即包含 `SKILL.md` 的文件夹）。

## 依赖

- **Python 3.11+**。无需手动选择解释器：`scripts/seedance` 封装脚本会自动优先使用 `python3.11`/`python3.12`（部分 OpenAI 风格代理的 TLS 证书链会被 Python 3.14 以更严格的 CA keyUsage 校验拒绝），仅在这些不可用时回退到 `python3`。
- 该封装脚本会在首次运行时于 `.venv/`（与 `SKILL.md` 同级）创建隔离虚拟环境，并自动安装 `requirements.txt`——无需手动 `pip install`。唯一的第三方依赖 `alibabacloud_oss_v2` 仅在传入**本地图片文件**（`-i`/`-f`/`-l`，上传到阿里云 OSS 换取短时签名 URL）时需要。文生视频或使用在线图片 URL 不需要任何第三方依赖。
- 可用 `SKILL_VENV_DIR=<path>` 覆盖 venv 位置。生成的 `.venv/` 是构建产物——请加入 gitignore，切勿提交。

## 环境变量

可在真实环境或 `.env` 中配置（自动加载，真实环境变量优先于文件）：

| 变量 | 必填 | 说明 |
|---|---|---|
| `ARK_API_KEY` | 是 | 模型调用 API Key |
| `ARK_ENDPOINT` | 否 | 接入地址，默认 `https://ark.cn-beijing.volces.com/api/v3` |
| `ARK_API_TYPE` | 否 | `ark` / `openai-video` / `openai`（优先级低于 `--api-type`） |
| `ARK_MODEL` | 否 | 模型 ID（优先级低于 `-m`） |
| `ARK_INSECURE` | 否 | `1` 跳过 TLS 校验（见 TLS 注意事项） |
| `OSS_ACCESS_KEY_ID` | 本地图片时必填 | 阿里云 AccessKey ID |
| `OSS_ACCESS_KEY_SECRET` | 本地图片时必填 | 阿里云 AccessKey Secret |
| `OSS_ENDPOINT` | 否 | OSS 区域或完整域名，如 `cn-beijing` 或 `oss-cn-beijing.aliyuncs.com` |
| `OSS_BUCKET` | 否 | bucket（默认 `jiangsier`） |
| `OSS_KEY_PREFIX` | 否 | 对象 key 前缀（默认 `dev/`） |

切勿提交 `.env`——其中含真实密钥（已被 gitignore）。

## 使用技能

直接用自然语言提需求即可，例如：

- “生成一段 5 秒的视频：蓝天下的雏菊花田，镜头逐渐拉近”
- “用 ./fox.png 做个视频——镜头缓缓拉出，头发被风吹动”
- “在 ./first.jpeg 和 ./last.jpeg 之间做 360 度环绕运镜的动画”

技能会提取选项、询问缺失或含糊的部分，并在运行前与你确认（生成消耗配额且耗时数分钟）。

## 命令行参考

也可通过 `scripts/seedance` 封装脚本直接运行，它会自建隔离 venv（解释器自动选择，见 TLS 注意事项）：

```bash
# 文生视频（Ark，默认）
scripts/seedance -t "蓝天下的雏菊花田，镜头逐渐拉近"

# 图生视频（本地图片 → 上传 OSS）
scripts/seedance -t "镜头缓缓拉出" -i ./fox.png --ratio adaptive

# 首尾帧
scripts/seedance -t "360 度环绕运镜" -f ./first.jpeg -l ./last.jpeg --ratio adaptive

# 在线图片 URL
scripts/seedance -t "镜头缓缓拉出" --image-url https://example.com/fox.png

# openai-video（mini）——同一封装，传 --api-type 即可
scripts/seedance --api-type openai-video -t "蓝天下的雏菊花田，镜头逐渐拉近"

# openai（full，Ark 风格请求体）
scripts/seedance --api-type openai -t "蓝天下的雏菊花田，镜头逐渐拉近"
```

### 参数

| 参数 | 说明 | 默认 |
|---|---|---|
| `-t / --text` | 提示词（必填） | — |
| `-i / --image` | 本地参考图片文件 | — |
| `--image-url` | 在线参考图片 URL（与 `--image` 互斥） | — |
| `-f / --first-frame` | 本地首帧图片文件 | — |
| `--first-frame-url` | 在线首帧图片 URL | — |
| `-l / --last-frame` | 本地尾帧图片文件（需配合 `--first-frame`） | — |
| `--last-frame-url` | 在线尾帧图片 URL | — |
| `--duration` | 时长（秒） | `5` |
| `--ratio` | 宽高比（`16:9`/`9:16`/`1:1`/…；`adaptive` 跟随输入图片） | `16:9` |
| `--resolution` | `480p`/`720p`/`1080p`/`4k` | `720p` |
| `-m / --model` | 模型 ID（CLI > `ARK_MODEL` 环境变量 > 各类型默认值） | ark → `doubao-seedance-2-0-260128`；openai-video → `doubao-seedance-2.0-mini`；openai → `doubao-seedance-2.0` |
| `--api-type` | `ark` / `openai-video` / `openai`（CLI > `ARK_API_TYPE` 环境变量 > `ark`） | `ark` |
| `--seed` | 随机种子（仅 ark/openai；openai-video 忽略） | — |
| `--save` | 将生成的 mp4 下载到该路径 | — |
| `--poll-interval` | 轮询间隔（秒） | `10` |
| `--timeout` | 等待完成的最长秒数 | `1800` |
| `--endpoint` | 覆盖 `ARK_ENDPOINT` | — |
| `--insecure` | 跳过 TLS 校验 | 关 |
| `--env-file` | `.env` 文件路径 | `.env` |

固定参数（按规格，ark + openai 路径）：`generate_audio=true`、`watermark=false`。openai-video 请求体不含这些参数。openai-video 与 openai 路径在该后端均产出**无声视频**——如需音频请用 `ark`。

### 冲突校验（运行前强制）

- `--image` 与 `--image-url`（以及 `--first-frame` 与 `--first-frame-url`、`--last-frame` 与 `--last-frame-url`）不能同时指定。
- 参考图（`--image`/`--image-url`）不能与显式首尾帧同时使用。
- `--last-frame` 必须配合 `--first-frame`。
- `--ratio adaptive` 必须有图片输入。

## 三种接入协议（`--api-type`，默认 `ark`）

| | `openai-video` | `openai` | `ark` |
|---|---|---|---|
| 创建任务 | `POST /video/generations` | `POST /video/generations` | `POST /contents/generations/tasks` |
| 请求体 | `{model, prompt, seconds(字符串,4/8/12), size(WxH), input_reference?(逗号拼接的 URL)}` | `{model, prompt, generate_audio, ratio, duration, watermark, resolution, image?, first_frame?, last_frame?, seed?}` | `{model, content:[{type:text},{type:image_url,role}], …}` |
| 轮询 | `GET /video/generations/{id}` | `GET /video/generations/{id}` | `GET /contents/generations/tasks/{id}` |
| 状态取值 | `queued` / `IN_PROGRESS` / `SUCCESS` | `queued` / `IN_PROGRESS` / `SUCCESS` | `queued` / `running` / `succeeded` |
| 视频地址 | `data.result_url` | `data.result_url` | `content.video_url` |
| 默认模型 | `doubao-seedance-2.0-mini` | `doubao-seedance-2.0` | `doubao-seedance-2-0-260128` |
| 音频 | 无 | 无 | 有 |

`reference.md` 是火山方舟官方文档，`ark` 路径遵循它。`openai-video` 与 `openai` 共用 `/video/generations` 传输与 `{code, data:{…}}` 响应，仅请求体与默认模型不同。

- **`openai-video`**——OpenAI-video 风格请求体（`seconds`/`size`/`input_reference`），模型 `doubao-seedance-2.0-mini`。**`seconds` 必须是字符串**（由 `--duration` 归整到 `{4,8,12}`）；**`input_reference` 是逗号拼接的 URL 字符串**（单个 = 参考图 / 首帧；两个 = 首尾帧）。`--ratio`/`--resolution` 映射为 `size`；`--seed` 被忽略。
- **`openai`**——代理的 “openai”（聊天镜像）入口，Ark 风格请求体（`image`/`first_frame`/`last_frame`/`generate_audio`/`ratio`/`duration`/`watermark`/`resolution`/`seed`），模型 `doubao-seedance-2.0`（full）。市场标注为 `/v1/chat/completions`，但该路径在本账号返回 `unsupported_model_endpoint`，故 full 模型经 `/video/generations` 调用。`--seed` 支持。
- **`ark`**——火山方舟原生 API；唯一产出**音频**的路径。

## TLS 注意事项（环境相关）

部分 OpenAI 风格代理通过负载均衡分发到多个后端节点，其中部分节点会返回中间 CA 证书缺少 `keyUsage` 扩展的证书链。CPython 3.14 会拒绝这些节点；3.11 则能接受全部。封装脚本内置重试逻辑以在 3.14 下尽量撑过去，但 `openai-video` / `openai` 路径**推荐用 `python3.11`**。走 `ark` 路径时 `python3` 即可。`scripts/seedance` 封装脚本会自动优先使用 `python3.11`/`python3.12`，无需手动处理。`--insecure`/`ARK_INSECURE` 可跳过校验，但许多代理的 WAF 会对未校验 TLS 的握手返回 403，因此通常无济于事。

## 测试

```bash
scripts/seedance test_seedance.py                                                   # 离线全套（无需 Key/网络）
cd scripts && ../.venv/bin/python -m unittest test_seedance.OpenaiTransportTests   # 单个类
cd scripts && ../.venv/bin/python -m unittest test_seedance.GenerateVideoSyncTests.test_text_to_video_polls_until_succeeded  # 单个用例
```

`scripts/seedance test_seedance.py` 在封装脚本的 venv 中跑完整离线套件（首次运行会创建 `.venv/`）；单个类/用例则直接驱动该 venv 的解释器用 `python -m unittest` 运行。离线套件 mock 了 HTTP 层并注入假的 OSS 客户端与假的 `alibabacloud_oss_v2` 模块，无需网络、Key 或 OSS SDK。真实联调测试（消耗配额）在未设置 `ARK_API_KEY` 时自动跳过。
