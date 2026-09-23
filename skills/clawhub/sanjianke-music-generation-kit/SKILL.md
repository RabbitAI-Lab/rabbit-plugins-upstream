---
name: music-generation-kit
slug: sanjianke-music-generation-kit
displayName: 三剪客 · 音乐生成
description: "音乐生成应用，支持歌曲生成、歌词生成、参考音频、声音克隆、音频导出和分轨处理。支持 歌词混合、人声处理、优化音乐风格、导出 MIDI、歌词时间轴、导出 MP4、导出 WAV、声音克隆。使用时需要你自己的 api.a7w.cn API Key。遇到问题可加技术微信 9872659。"
version: 1.0.5
summary: "「音乐生成」的完整调用封装：13 个接口的官方文档、参数表与一个零依赖客户端。需要自带 api.a7w.cn 的 API Key，调用按点数计费。遇到问题可加技术微信 9872659。"
license: MIT
tags:
  - 三剪客
  - 设计多媒体
  - 音乐生成
  - 音频
---

# 音乐生成

音乐生成应用，支持歌曲生成、歌词生成、参考音频、声音克隆、音频导出和分轨处理。

## 权限与用途说明

| 能力 | 是否申请 | 用途 |
|---|---|---|
| 网络访问 | **申请** | 调用 `api.a7w.cn` 的插件接口（本 Skill 唯一的联网行为） |
| 读取文件 | 仅读取用户指定的输入文件（图片/音频/视频） | 作为接口的素材入参 |
| 写入文件 | 仅在传入 `--out` 时 | 保存接口返回的 JSON 结果 |
| 凭证 | 读取**使用者自己**提供的 API Key | 从 `~/.a7w/config.json` 或环境变量读取 |
| 子进程 / 后台常驻 | 不申请 | 脚本执行完即退出 |

**不内嵌任何密钥。** 脚本只把 Key 发往 `api.a7w.cn`，不发送到其他任何地址。

## 快速开始

```bash
# 1. 配置你自己的 api.a7w.cn API Key（只需一次）
python3 scripts/client.py login --key sk-你的key

# 2. 看这个插件的接口与参数
python3 scripts/client.py schema music_generation

# 3. 调用（示例）
python3 scripts/client.py call music_generation mashup_lyrics --json '{}'
```

> **没有 Key？** 见 `references/getting-started.md`——注册、充值、取 Key 的完整步骤。也可以直接去 [算力集市](https://api.a7w.cn/) 注册。

## 接口一览

| 接口 | 名称 | 模式 | 计费 | 说明 |
|---|---|---|---|---|
| `mashup_lyrics` | 歌词混合 | 同步 | 按次固定价 12.0000 点 | 将两段歌词融合为新的混合版本。 |
| `vox` | 人声处理 | 异步（需轮询） | 按次固定价 14.0000 点 | 基于音频 ID 提取指定片段的人声或伴奏处理结果。 |
| `style` | 优化音乐风格 | 同步 | 按次固定价 14.0000 点 | 根据提示词生成更完整的音乐风格描述。 |
| `midi` | 导出 MIDI | 异步（需轮询） | 按次固定价 14.0000 点 | 基于音频 ID 提取 MIDI 文件。 |
| `timing` | 歌词时间轴 | 同步 | 免费（查询类接口） | 基于音频 ID 获取歌词与音频时间轴信息。 |
| `mp4` | 导出 MP4 | 同步 | 按次固定价 20.0000 点 | 基于音频 ID 获取视频文件链接。 |
| `wav` | 导出 WAV | 异步（需轮询） | 按次固定价 14.0000 点 | 基于音频 ID 导出高质量 WAV 文件。 |
| `voice_clone` | 声音克隆 | 同步 | 按次固定价 20.0000 点 | 基于清晰人声音频创建私有声音风格 ID。 |
| `persona` | 创建歌手风格 | 同步 | 按次固定价 12.0000 点 | 基于已生成歌曲创建可复用的歌手风格 ID。 |
| `upload_audio` | 上传参考音频 | 同步 | 按次固定价 13.0000 点 | 提交可访问的音频地址并返回可用于后续创作的音频 ID。 |
| `lyrics` | 生成歌词 | 同步 | 按次固定价 12.0000 点 | 根据主题或风格描述生成结构化歌词。 |
| `query` | 查询音乐任务 | 同步 | 免费（查询类接口） | 按平台任务 ID 查询任务状态与结果。 |
| `create` | 创建音乐任务 | 异步（需轮询） | 按次固定价 65.0000 点 | 提交音乐生成、续写、翻唱、分轨或混音任务，返回平台任务 ID。 |

## 接口详情

### `mashup_lyrics` · 歌词混合

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 12.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/mashup_lyrics`

将两段歌词融合为新的混合版本。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `lyrics_a` | string | 是 | 第一段歌词文本。 |
| `lyrics_b` | string | 是 | 第二段歌词文本。 |

完整文档（含请求/响应示例）：[`references/api-mashup_lyrics.md`](references/api-mashup_lyrics.md)

### `vox` · 人声处理

**模式**：异步（提交后轮询任务） ｜ **计费**：按次固定价 14.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/vox`

基于音频 ID 提取指定片段的人声或伴奏处理结果。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_id` | string | 是 | 音频 ID，用于定位已生成或已上传的音频片段。（示例：audio_xxxxxxxxxxxx） |
| `vocal_end` | number | 否 | 人声提取结束时间，单位秒。 |
| `vocal_start` | number | 否 | 人声提取开始时间，单位秒。 |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址。 |

完整文档（含请求/响应示例）：[`references/api-vox.md`](references/api-vox.md)

### `style` · 优化音乐风格

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 14.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/style`

根据提示词生成更完整的音乐风格描述。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `prompt` | string | 是 | 需要优化的风格提示词。（示例：warm electronic pop with female vocal） |

完整文档（含请求/响应示例）：[`references/api-style.md`](references/api-style.md)

### `midi` · 导出 MIDI

**模式**：异步（提交后轮询任务） ｜ **计费**：按次固定价 14.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/midi`

基于音频 ID 提取 MIDI 文件。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_id` | string | 是 | 音频 ID，用于定位已生成或已上传的音频片段。（示例：audio_xxxxxxxxxxxx） |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址；同步接口可不传。 |

完整文档（含请求/响应示例）：[`references/api-midi.md`](references/api-midi.md)

### `timing` · 歌词时间轴

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`POST /api/v1/apps/music_generation/timing`

基于音频 ID 获取歌词与音频时间轴信息。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_id` | string | 是 | 音频 ID，用于定位已生成或已上传的音频片段。（示例：audio_xxxxxxxxxxxx） |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址；同步接口可不传。 |

完整文档（含请求/响应示例）：[`references/api-timing.md`](references/api-timing.md)

### `mp4` · 导出 MP4

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 20.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/mp4`

基于音频 ID 获取视频文件链接。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_id` | string | 是 | 音频 ID，用于定位已生成或已上传的音频片段。（示例：audio_xxxxxxxxxxxx） |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址；同步接口可不传。 |

完整文档（含请求/响应示例）：[`references/api-mp4.md`](references/api-mp4.md)

### `wav` · 导出 WAV

**模式**：异步（提交后轮询任务） ｜ **计费**：按次固定价 14.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/wav`

基于音频 ID 导出高质量 WAV 文件。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_id` | string | 是 | 音频 ID，用于定位已生成或已上传的音频片段。（示例：audio_xxxxxxxxxxxx） |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址；同步接口可不传。 |

完整文档（含请求/响应示例）：[`references/api-wav.md`](references/api-wav.md)

### `voice_clone` · 声音克隆

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 20.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/voice_clone`

基于清晰人声音频创建私有声音风格 ID。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 否 | 自定义声音风格名称。（示例：My Voice） |
| `audio_url` | string | 是 | 可公开访问的 MP3 或 WAV 人声音频 URL。音频至少 10 秒，建议单人清晰人声，尽量避免背景噪音或背景音乐。（示例：https://example.com/voice.mp3） |
| `description` | string | 否 | 自定义声音风格描述。 |

完整文档（含请求/响应示例）：[`references/api-voice_clone.md`](references/api-voice_clone.md)

### `persona` · 创建歌手风格

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 12.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/persona`

基于已生成歌曲创建可复用的歌手风格 ID。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `name` | string | 是 | 歌手风格名称。（示例：My Singer Style） |
| `audio_id` | string | 是 | 音频 ID，用于定位已生成或已上传的音频片段。（示例：audio_xxxxxxxxxxxx） |
| `vocal_end` | number | 否 | 人声片段结束时间，单位秒。 |
| `description` | string | 否 | 歌手风格的文字描述。 |
| `vocal_start` | number | 否 | 人声片段开始时间，单位秒。 |
| `vox_audio_id` | string | 否 | 用于创建新歌手风格的人声参考音频 ID。 |

完整文档（含请求/响应示例）：[`references/api-persona.md`](references/api-persona.md)

### `upload_audio` · 上传参考音频

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 13.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/upload_audio`

提交可访问的音频地址并返回可用于后续创作的音频 ID。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `audio_url` | string | 是 | 可公开访问的音频文件 URL，用于生成后续创作需要的音频 ID。（示例：https://example.com/ref.mp3） |

完整文档（含请求/响应示例）：[`references/api-upload_audio.md`](references/api-upload_audio.md)

### `lyrics` · 生成歌词

**模式**：同步（直接返回结果） ｜ **计费**：按次固定价 12.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/lyrics`

根据主题或风格描述生成结构化歌词。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `prompt` | string | 是 | 歌词生成提示词，用于描述歌词主题、情绪或风格。（示例：A song about winter） |

完整文档（含请求/响应示例）：[`references/api-lyrics.md`](references/api-lyrics.md)

### `query` · 查询音乐任务

**模式**：同步（直接返回结果） ｜ **计费**：免费（查询类接口） ｜ **请求**：`GET /api/v1/apps/music_generation/query`

按平台任务 ID 查询任务状态与结果。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `task_id` | string | 是 | 创建任务后返回的平台任务 ID。（示例：task_xxxxxxxxxxxx） |

完整文档（含请求/响应示例）：[`references/api-query.md`](references/api-query.md)

### `create` · 创建音乐任务

**模式**：异步（提交后轮询任务） ｜ **计费**：按次固定价 65.0000 点 ｜ **请求**：`POST /api/v1/apps/music_generation/create`

提交音乐生成、续写、翻唱、分轨或混音任务，返回平台任务 ID。

| 参数 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `type` | enum | 否 | 可选值：generate / extend / upload_extend / upload_cover / concat / cover / artist_consistency / artist_consistency_vox / stems / all_stems / replace_section / underpainting；操作类型。generate 根据提示生成音乐；extend 基于已有音频续写；concat 拼接音频片段；cover 参考既有曲风重新演绎；upload_cover 对上传音频进行风格翻唱；upload_extend 续写上传音频；art…（示例：generate） |
| `lyric` | string | 否 | 自定义模式下使用的歌词。常规模型最多 3000 字符，高质量模型最多 5000 字符。 |
| `style` | string | 否 | 音乐风格描述。常规模型最多 200 字符，高质量模型最多 1000 字符。（示例：dream pop, warm synth, mellow vocal） |
| `title` | string | 否 | 自定义模式下的歌曲标题。常规模型最多 80 字符，高质量模型最多 100 字符。（示例：Neon Night） |
| `custom` | boolean | 否 | 是否启用自定义模式。请使用 JSON boolean；平台也兼容 true/false、1/0、yes/no、on/off 字符串。为 true 时按歌词和风格生成；为 false 时按提示词生成。 |
| `prompt` | string | 否 | 生成音乐的提示词。灵感模式下不超过 500 个字符；自定义歌词模式请优先使用 lyric 和 style。（示例：A warm synth-pop song about city nights） |
| `audio_id` | string | 否 | 已有音频 ID。extend、concat 等基于已有音频的操作需要填写。 |
| `weirdness` | number | 否 | 创意实验强度，范围 0 到 1；数值越高结果越开放，仅在自定义模式下生效。 |
| `audio_urls` | array | 否 | 参考音频 URL 列表。inspo 类型要求 1 到 4 个可公开访问的音频地址。（示例：['https://example.com/ref.mp3']） |
| `persona_id` | string | 否 | 歌手或声音风格 ID，用于让生成歌曲采用指定风格。 |
| `continue_at` | number | 否 | 从已有音频的指定秒数位置继续生成。例如 213.5 表示从 3 分 33.5 秒处续写。 |
| `samples_end` | number | 否 | 添加采样的结束时间，单位秒，需小于歌曲总时长。 |
| `audio_weight` | number | 否 | 参考音频权重，范围 0 到 1；数值越高越依赖参考音频，主要用于翻唱类操作。 |
| `callback_url` | string | 否 | 任务完成或失败时由平台主动通知的 HTTPS 地址。 |
| `instrumental` | boolean | 否 | 纯伴奏模式。请使用 JSON boolean；平台也兼容 true/false、1/0、yes/no、on/off 字符串。开启后将忽略歌词内容。 |
| `lyric_prompt` | string | 否 | 自动生成歌词的提示词，仅在 custom 为 true 且 lyric 为空时生效。 |
| `vocal_gender` | enum | 否 | 可选值：m / f；人声性别偏好，m 表示男声，f 表示女声。该参数用于提高目标音色概率，但不保证严格符合。 |
| `samples_start` | number | 否 | 添加采样的开始时间，单位秒，默认 0。 |
| `style_negative` | string | 否 | 不希望出现在音乐中的风格描述。 |
| `style_influence` | number | 否 | 风格影响强度，范围 0 到 1；数值越高越贴近填写的风格，仅在自定义模式下生效。 |
| `mashup_audio_ids` | array | 否 | 用于混合的音频 ID 列表。mashup 类型需要填写。 |
| `overpainting_end` | number | 否 | 添加人声的结束时间，单位秒，需小于歌曲总时长。 |
| `underpainting_end` | number | 否 | 添加伴奏的结束时间，单位秒，需小于歌曲总时长。 |
| `overpainting_start` | number | 否 | 添加人声的开始时间，单位秒，默认 0。 |
| `variation_category` | enum | 否 | 可选值：high / normal / subtle；变化强度，可选 high、normal、subtle。 |
| `replace_section_end` | number | 否 | replace_section 类型中需要替换片段的结束时间，单位秒。 |
| `underpainting_start` | number | 否 | 添加伴奏的开始时间，单位秒，默认 0。 |
| `replace_section_start` | number | 否 | replace_section 类型中需要替换片段的开始时间，单位秒。 |

完整文档（含请求/响应示例）：[`references/api-create.md`](references/api-create.md)

## 关于异步任务

标记为「异步」的接口是**任务制**：提交后返回 `task_id`，需要轮询到完成。
`client.py call` 默认**自动轮询到结束**再返回，你也可以手动控制：

```bash
# 只提交，不等结果
python3 scripts/client.py call music_generation <api> --json '{...}' --no-wait

# 之后用 task_id 查状态
python3 scripts/client.py task <task_id>
```

异步任务在**提交时会预冻结点数**，任务完成后按实际用量结算。
**不要重复提交同一个任务**——每次提交都可能产生费用。

## 常见错误

| 返回 | 含义 | 处理 |
|---|---|---|
| HTTP 401 | Key 无效或过期 | 重新创建 Key 后 `login` |
| HTTP 402 / `code:402` | 点数不足 | 去算力中心充值；错误信息里有本次所需点数 |
| `Invalid.Params` | 参数不合法 | 用 `schema music_generation` 核对参数与必填项 |
| 任务 `status: failed` | 上游处理失败 | 看 `error.message`；换素材或稍后重试 |

## 能力边界

- **不提供 API Key**：Key 必须由使用者自己获取
- **不代付费用**：调用消耗的是使用者自己账号的点数
- **不保证可用性**：接口由第三方平台提供，可用性、限流与计费以站内为准
- **不替代内容合规审查**：生成内容的合规责任由使用者承担

## 参考文件

| 文件 | 用途 |
|---|---|
| `references/getting-started.md` | 注册、充值、获取与配置 API Key |
| `references/api-mashup_lyrics.md` | `mashup_lyrics` 的官方文档 |
| `references/api-vox.md` | `vox` 的官方文档 |
| `references/api-style.md` | `style` 的官方文档 |
| `references/api-midi.md` | `midi` 的官方文档 |
| `references/api-timing.md` | `timing` 的官方文档 |
| `references/api-mp4.md` | `mp4` 的官方文档 |
| `references/api-wav.md` | `wav` 的官方文档 |
| `references/api-voice_clone.md` | `voice_clone` 的官方文档 |
| `references/api-persona.md` | `persona` 的官方文档 |
| `references/api-upload_audio.md` | `upload_audio` 的官方文档 |
| `references/api-lyrics.md` | `lyrics` 的官方文档 |
| `references/api-query.md` | `query` 的官方文档 |
| `references/api-create.md` | `create` 的官方文档 |
| `scripts/client.py` | 通用客户端（零依赖） |

---

## 联系我们

- **技术微信：9872659** —— 加好友时说一下是从哪个 Skill 找过来的，直接给你配套的 API Key 与能跑的示例。
- **要算力 / 要 API Key**：[算力集市 · 注册领 API Key](https://api.a7w.cn/) —— 一个 Key 调用全部 AI 算力，注册、充值、创建 Key 都在这里。
- **更多 AI 插件与接口**：[AI 插件市场](https://aigc.a7w.cn/)。

---

## 相关链接

| 链接 | 地址 | 说明 |
|---|---|---|
| [算力集市 · 注册领 API Key](https://api.a7w.cn/) | api.a7w.cn | 一个 Key 调用全部 AI 算力；注册、充值、创建 Key 都在这 |
| [AI 插件市场](https://aigc.a7w.cn/) | aigc.a7w.cn | 浏览全部 AI 插件与接口说明 |
| [三剪客 · 一句话批量出片](https://ks.a7w.cn/) | ks.a7w.cn | 短剧二创 / 影视解说 / 矩阵号批量混剪桌面客户端 |
| [视频超清 · 在线批量超分](https://vr.a7w.cn/) | vr.a7w.cn | 网页版视频超分，批量处理，最高 4K |
| [0人公司 · AI Agent 平台](https://a7w.cn/) | a7w.cn | 主站，了解整套 AI Agent 生态 |
