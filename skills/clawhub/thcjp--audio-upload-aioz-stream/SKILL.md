---
slug: "audio-upload-aioz-stream"
name: "audio-upload-aioz-stream"
version: 1.0.2
displayName: "AIOZ音频上传"
summary: "通过AIOZ Stream API快速上传音频文件，支持默认与自定义编码配置，返回HLS/DASH流媒体链接。"
license: "Proprietary"
description: |-
  基于 AIOZ Stream API 的音频上传技能，通过三步流程
  (Create → Upload Part → Complete) 将本地音频文件上传至
  AIOZ 流媒体平台。支持默认快速上传与自定义编码配置
  (质量预设、码率、采样率、标签、元数据)，上传完成后触发
  服务端转码并返回 HLS/DASH 流媒体播放链接。使用 API Key
  (stream-public-key/stream-secret-key) 认证。适用于播客
  发布、音乐分发、语音内容托管等场景.
tags:
  - Creative
  - Audio
  - Streaming
  - Upload
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# AIOZ 音频上传

通过 AIOZ Stream API 将本地音频文件上传至 AIOZ 流媒体平台。完整上传流程包含三次 API 调用：创建音频对象 → 上传文件分片 → 完成上传。上传完成后服务端自动触发转码，最终返回 HLS/DASH 流媒体播放链接.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | AIOZ音频上传处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| AIOZ音频上传默认与自定义编码配置 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 认证配置

本技能使用 API Key 认证，用户需提供以下两个密钥，作为 HTTP 请求头附加到所有 API 调用：

- `stream-public-key`：AIOZ Stream 公钥
- `stream-secret-key`：AIOZ Stream 私钥

若用户未提供密钥，主动询问获取。密钥通过 AIOZ Stream 控制台创建与管理.
## 上传方式选择

用户发起上传请求时，询问选择以下方式：

**默认上传（快速）**：仅提供标题即可创建音频对象并上传，使用默认编码配置，适合快速发布场景.
**自定义上传（高级）**：完整配置编码参数，包括质量预设、码率、采样率、标签、元数据等，适合对音质有明确要求的发布场景.
## 完整上传流程

### 第一步：创建音频对象

**默认上传**：仅需标题与类型.
```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: YOUR_PUBLIC_KEY' \
  -H 'stream-secret-key: YOUR_SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "AUDIO_TITLE",
    "type": "audio"
  }'
```

**自定义上传**：包含完整编码配置.
```bash
curl -s -X POST 'https://api-w3stream.attoaioz.cyou/api/videos/create' \
  -H 'stream-public-key: YOUR_PUBLIC_KEY' \
  -H 'stream-secret-key: YOUR_SECRET_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "AUDIO_TITLE",
    "type": "audio",
    "description": "DESCRIPTION",
    "is_public": true,
    "tags": ["tag1", "tag2"],
    "metadata": [
      {"key": "KEY", "value": "VALUE"}
    ],
    "qualities": [
      {
        "resolution": "highest",
        "type": "hls",
        "container_type": "mpegts",
        "audio_config": {
          "codec": "aac",
          "bitrate": 320000,
          "channels": "2",
          "sample_rate": 48000,
          "language": "en",
          "index": 0
        }
      },
      {
        "resolution": "standard",
        "type": "hls",
        "container_type": "mpegts",
        "audio_config": {
          "codec": "aac",
          "bitrate": 128000,
          "channels": "2",
          "sample_rate": 44100,
          "language": "en",
          "index": 0
        }
      }
    ]
  }'
```

从响应中提取 `data.id`，作为后续步骤的 `AUDIO_ID`.
### 第二步：上传文件分片

上传音频文件二进制数据到创建的音频对象。首先获取文件大小并计算 MD5 哈希：

```bash
FILE_SIZE=$(stat -f%z /path/to/audio.mp3 2>/dev/null || stat -c%s /path/to/audio.mp3)
END_POS=$((FILE_SIZE - 1))
# ...
HASH=$(md5sum /path/to/audio.mp3 | awk '{print $1}')
```

然后通过 multipart form-data 上传，必须包含 `Content-Range` 请求头：

```bash
curl -s -X POST "https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/part" \
  -H 'stream-public-key: YOUR_PUBLIC_KEY' \
  -H 'stream-secret-key: YOUR_SECRET_KEY' \
  -H "Content-Range: bytes 0-$END_POS/$FILE_SIZE" \
  -F "file=@/path/to/audio.mp3" \
  -F "index=0" \
  -F "hash=$HASH"
```

`Content-Range` 头格式为 `bytes {start}-{end}/{total_size}`。单分片上传时 `start=0`、`end=file_size-1`、`total_size=file_size`；多分片上传时按分片调整 start/end 位置。表单字段：`file` 为音频文件二进制，`index` 为分片序号（单分片为 0），`hash` 为分片的 MD5 哈希.
### 第三步：完成上传

文件分片上传完成后调用完成接口触发转码：

```bash
curl -s -X GET "https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID/complete" \
  -H 'accept: application/json' \
  -H 'stream-public-key: YOUR_PUBLIC_KEY' \
  -H 'stream-secret-key: YOUR_SECRET_KEY'
```

调用后上传流程结束，服务端开始转码.
### 获取播放链接

上传完成后获取音频详情以取得流媒体链接：

```bash
curl -s 'https://api-w3stream.attoaioz.cyou/api/videos/AUDIO_ID' \
  -H 'stream-public-key: YOUR_PUBLIC_KEY' \
  -H 'stream-secret-key: YOUR_SECRET_KEY'
```

从响应的 `assets` 或 `hls` 字段解析 HLS 流媒体链接返回给用户。音频输出没有 `mp4_url` 字段，仅提供 HLS/DASH 流媒体链接.
## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

- **三步上传流程**：Create → Upload Part → Complete 的标准化上传流程，支持单分片与多分片上传
- **默认与自定义编码配置**：默认上传快速发布，自定义上传精细控制质量预设、码率、采样率、声道、语言标签
- **HLS/DASH 流媒体输出**：上传完成后服务端转码为 HLS 或 DASH 格式，返回自适应流媒体播放链接
- **多质量预设支持**：standard、good、highest、lossless 四档质量预设，适配不同播放场景
- **元数据与标签管理**：支持自定义标签与键值对元数据，便于音频内容分类与检索
- **分片上传与断点续传**：通过 Content-Range 头实现多分片上传，支持大文件分块传输
### 三步上传流程

针对三步上传流程,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供三步上传流程相关的配置参数、输入数据和处理选项.
**输出**: 返回三步上传流程的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`三步上传流程`的配置文档进行参数调优
### 默认与自定义编码配置

针对默认与自定义编码,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供默认与自定义编码配置相关的配置参数、输入数据和处理选项.
**输出**: 返回默认与自定义编码配置的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`默认与自定义编码配置`的配置文档进行参数调优
### HLS/DASH 流媒体输出

针对HLS/DASH 流媒体输出,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供HLS/DASH 流媒体输出相关的配置参数、输入数据和处理选项.
**输出**: 返回HLS/DASH 流媒体输出的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`HLS/DASH 流媒体输出`的配置文档进行参数调优
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`audio-upload-aioz-stream`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 编码配置参考

### 质量预设（resolution 字段）

- `standard`：标准质量，适合语音类内容
- `good`：良好质量，适合日常音乐播放
- `highest`：最高质量，适合高品质音乐发行
- `lossless`：无损质量，适合母带级存档

### 流媒体格式（type 字段）

- `hls`：HTTP Live Streaming，容器格式为 `mpegts` 或 `mp4`
- `dash`：Dynamic Adaptive Streaming，容器格式为 `fmp4`

### 音频编码参数

- `codec`：仅支持 `aac`
- `bitrate`：整数，单位 bits/sec（如 128000、256000、320000）
- `channels`：声道数，`"2"` 表示立体声
- `sample_rate`：采样率，可选值 8000、11025、16000、22050、32000、44100、48000、88200、96000
- `language`：BCP 47 语言代码（如 `en`、`zh`）
- `index`：音频流索引，默认 0

### 推荐码率

- 播客/语音：64000 - 128000 bps
- 标准音乐：128000 - 192000 bps
- 高品质音乐：192000 - 256000 bps
- 最高品质音乐：256000 - 320000 bps

### 推荐采样率

- 语音内容：22050 或 32000
- 音乐内容：44100 或 48000

## 适用场景

### 场景一：播客节目快速发布

播客创作者需要将录制好的音频节目快速上传到流媒体平台分发。使用默认上传方式，仅提供节目标题即可完成上传并获取 HLS 播放链接，嵌入播客网站或分发给订阅者。适合追求发布效率、对编码参数无特殊要求的日常更新场景.
### 场景二：音乐作品高品质发行

音乐人或厂牌需要将音乐作品以高品质编码上传发布。使用自定义上传方式，配置 highest 质量预设、320kbps 码率、48000Hz 采样率，确保流媒体播放音质满足发行标准。同时通过 tags 与 metadata 字段标注曲目信息、专辑归属、版权声明，便于内容管理与检索.
### 场景三：语音内容多档位托管

教育或媒体机构需要为同一份语音内容提供多档位质量，适配不同网络环境的听众。使用自定义上传的 qualities 数组配置 standard 与 highest 两档 HLS 输出，低带宽听众播放标准档，高带宽听众播放高品质档，由播放器自适应切换.
### 场景四：音频内容批量归档

企业或机构需要将大量历史音频资料批量上传至流媒体平台归档托管。通过脚本化调用三步上传流程，配合 metadata 字段记录原始日期、来源、分类等归档元数据，实现音频资产的结构化托管与检索.
## 使用案例

### 案例一：播客节目默认上传

用户提供音频文件路径与节目标题"科技脱口秀第50期"，选择默认上传方式。流程执行：调用 create 接口创建 type 为 audio 的音频对象，获取 AUDIO_ID；计算文件 MD5 哈希与大小，通过 part 接口上传文件分片；调用 complete 接口触发转码；查询音频详情获取 HLS 播放链接返回用户。用户将链接嵌入播客网站供订阅者收听.
### 案例二：音乐单曲自定义上传

用户提供音乐文件路径，要求以最高品质 HLS 格式上传，码率 320kbps，采样率 48000Hz，标签为"pop,2024"。流程执行：调用 create 接口，请求体包含 qualities 数组配置 highest 预设与完整 audio_config，tags 字段设为指定标签；获取 AUDIO_ID 后上传文件分片并完成转码；返回 HLS 播放链接。用户在音乐平台嵌入该链接供听众高品质播放.
### 案例三：有声书多档位上传

用户提供有声书音频文件，要求同时生成标准与最高两档 HLS 输出以适配不同网络环境。流程执行：调用 create 接口，qualities 数组包含两个质量配置（standard 档 128kbps/44100Hz，highest 档 256kbps/48000Hz），metadata 字段记录书籍章节信息；上传完成后返回 HLS 播放链接，播放器根据听众网络状况自适应选择档位.
## 响应处理规范

1. 解析 create 接口的 JSON 响应，提取 `data.id` 作为 AUDIO_ID
2. 计算音频文件的 MD5 哈希值
3. 通过 part 接口上传文件分片，附带 hash 与 Content-Range 头
4. 调用 complete 接口完成上传并触发转码
5. 查询音频详情获取流媒体播放链接
6. 将播放链接返回用户
7. 若音频仍在转码中（状态为 transcoding），告知用户稍后查询

## 异常处理

### 401 认证失败

API 返回 401 状态码，说明 stream-public-key 或 stream-secret-key 无效。处理方式：提示用户核对 AIOZ Stream 控制台中的公钥与私钥是否正确复制，确认密钥未过期或被撤销。重新提供正确的密钥后上传流程。密钥以 HTTP 请求头形式发送到所有 API 调用，需确保两个密钥均正确.
### 400 请求格式错误

API 返回 400 状态码，说明请求体格式不符合接口要求。处理方式：检查 create 接口的 JSON 请求体结构，确认 type 字段为 "audio"，qualities 数组中的 audio_config 字段完整且值合法。自定义上传时重点检查 bitrate 是否为整数、sample_rate 是否在支持的取值列表中、channels 是否为字符串格式.
### 500 服务器错误

API 返回 500 状态码，说明 AIOZ Stream 服务端内部错误。处理方式：稍后上传流程。若持续返回 500，记录完整的请求与响应信息，联系 AIOZ Stream 支持团队排查。时建议从 create 接口重新开始完整流程，避免使用可能已失效的 AUDIO_ID.
### Content-Range 头缺失或格式错误

上传分片时缺少 Content-Range 头或格式不符合 `bytes {start}-{end}/{total_size}` 规范，导致上传失败。处理方式：确认上传前正确计算 FILE_SIZE 与 END_POS，单分片上传时 start 为 0、end 为 file_size-1。多分片上传时按分片边界计算各分片的 start/end。重新构造请求头后上传.
### MD5 哈希不匹配

上传分片时服务端校验 MD5 哈希与实际文件内容不匹配，导致上传被拒绝。处理方式：重新计算文件 MD5 哈希，确认计算的是当前分片内容而非整个文件的哈希（多分片场景）。检查文件在上传过程中是否被修改，确保哈希计算与文件上传使用同一版本。重新计算后上传.
### 转码未完成

查询音频详情时状态为 transcoding，尚未生成流媒体播放链接。处理方式：告知用户音频正在转码中，播放链接需等待转码完成后才能获取。建议用户间隔一段时间后重新查询音频详情。转码耗时取决于音频时长与服务端负载，通常数分钟内完成.
### 文件路径不存在或不可读

上传分片时无法读取本地音频文件，通常由文件路径错误或权限不足引起。处理方式：确认文件路径正确且当前用户有读取权限。使用 stat 命令验证文件存在且大小正常。macOS 使用 `stat -f%z`，Linux 使用 `stat -c%s` 获取文件大小，确保跨平台兼容.
### 网络超时或连接中断

上传过程中网络超时或连接中断，导致分片上传未完成。处理方式：，对大文件使用多分片上传减少单次传输量。中断后可从失败的分片重新上传，无需重新创建音频对象。确认 AIOZ Stream API 域名 `api-w3stream.attoaioz.cyou` 可达.
## 常见问题

### Q1：如何获取 AIOZ Stream 的 API 密钥？

注册并登录 AIOZ Stream 平台后，在控制台的 API 设置或开发者页面创建 API 密钥。系统会生成一对 stream-public-key（公钥）与 stream-secret-key（私钥）。公钥用于标识账户身份，私钥用于签名验证，两者均需妥善保管。密钥作为 HTTP 请求头（stream-public-key、stream-secret-key）附加到所有 API 调用中.
### Q2：音频上传后为什么没有 mp4_url 字段？

AIOZ Stream 的音频类型输出仅提供 HLS/DASH 流媒体链接，不生成 mp4_url 字段。这是因为音频内容以自适应流媒体格式分发，播放器根据网络状况动态选择码率档位。如需直接下载音频文件，需在本地保留原始文件，平台不提供音频文件的直接下载链接。视频类型上传后才会有 mp4_url 字段.
### Q3：单分片上传与多分片上传如何选择？

单分片上传适合小文件（通常 100MB 以下），一次上传整个文件，start=0、end=file_size-1。多分片上传适合大文件，将文件分割为多个分片分别上传，每个分片有独立的 index、Content-Range 与 hash。多分片上传支持断点续传，单个分片失败只需重传该分片。根据文件大小与网络稳定性选择上传方式.
### Q4：转码需要多长时间？

转码耗时取决于音频时长、编码配置复杂度与服务端负载。短音频（数分钟）通常在 1-2 分钟内完成转码；长音频（数小时如有声书）可能需要更长时间。多档位质量配置会增加转码工作量。上传完成后通过查询音频详情接口检查转码状态，状态从 transcoding 变为 ready 即表示完成，此时可获取播放链接.
### Q5：支持哪些音频输入格式？

AIOZ Stream 服务端转码接受常见音频格式输入，包括 MP3、WAV、FLAC、AAC、OGG 等。上传后服务端统一转码为配置的 HLS 或 DASH 输出格式，音频编码为 AAC。输入格式不影响输出格式，但建议使用无损或高码率源文件以保证转码后的音质。避免使用已高度压缩的低码率文件作为源，以免二次压缩导致音质损失.
### Q6：tags 与 metadata 字段有什么区别？

tags 是字符串数组，用于音频内容的分类标签，便于按主题检索与筛选，如 ["podcast", "tech"]。metadata 是键值对数组，每项包含 key 与 value 字段，用于记录结构化元数据，如章节信息、版权声明、原始日期等。tags 适合扁平分类，metadata 适合结构化属性记录。两者可在自定义上传时同时配置.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 音频输出仅提供 HLS/DASH 流媒体链接，不提供 mp4_url 直接下载链接
- 音频编码仅支持 AAC 编解码器，不支持其他编码格式
- 上传流程需要三次 API 调用，无法通过单次请求完成上传
- 转码在服务端异步进行，上传完成后需等待转码完成才能获取播放链接
- API 密钥以明文 HTTP 请求头传输，需确保调用环境的安全性
- 多分片上传需自行管理分片边界与序号，接口不提供分片管理能力
- 自定义编码配置的 qualities 数组中每个质量档位独立转码，增加转码耗时
- API 域名 `api-w3stream.attoaioz.cyou` 需网络可达，受限网络环境可能无法访问

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "AIOZ音频上传处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "audio-upload-aioz-stream"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
