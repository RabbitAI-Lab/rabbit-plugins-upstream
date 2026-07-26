---
slug: "azure-ai-transcription-py"
name: "azure-ai-transcription-py"
version: 0.1.1
displayName: "Azure语音转文字SDK"
summary: "Azure AI Transcription Python SDK,支持实时与批量语音转文字,含说话人分离与时间戳"
license: "Proprietary"
description: |-
  Azure AI Transcription 的 Python 客户端库,覆盖实时流式与批量两种语音转文字模式.
  批量模式适合存储在 Blob 中的长音频,支持说话人分离(diarization)与多通道;
  实时模式通过流式会话边录边转,适合会议同传与字幕生成。使用订阅密钥认证,
  通过 TRANSCRIPTION_ENDPOINT 与 TRANSCRIPTION_KEY 环境变量配置资源。提供时间戳
  捕获、语言指定、流式背压处理与会话关闭等实践要点.
tags:
  - 系统运维
  - Speech
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Azure Ai Transcription Py

Azure AI Transcription(speech-to-text)的 Python 客户端库,支持实时与批量转写.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure语音转文字SDK处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 安装

```bash
pip install azure-ai-transcription
```

## 环境变量

```bash
TRANSCRIPTION_ENDPOINT=https://<resource>.cognitiveservices.azure.com
TRANSCRIPTION_KEY=API_KEY
```

`TRANSCRIPTION_ENDPOINT` 为 Azure AI 资源的终结点 URL,形如 `https://<resource>.cognitiveservices.azure.com`,与资源所在区域一致。`TRANSCRIPTION_KEY` 为该资源的订阅密钥(primary 或 secondary 均可),用于鉴权。两个变量都不要硬编码进源码,建议放入 `.env` 或系统环境变量;密钥泄漏后须在门户轮换并更新变量.
## 认证

使用订阅密钥认证(此客户端不支持 DefaultAzureCredential):

```python
import os
from azure.ai.transcription import TranscriptionClient
# ...
client = TranscriptionClient(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    credential=os.environ["TRANSCRIPTION_KEY"]
)
```

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

- 批量转写:对存储在 Blob 中的长音频文件提交转写作业,支持说话人分离与多通道
- 实时转写:通过流式会话边录边转,逐事件输出识别文本,适合会议同传与字幕生成
- 说话人分离:开启 `diarization_enabled` 区分多说话人,标注每段发言归属
- 时间戳捕获:为识别结果附带时间戳,用于字幕对齐与片段定位
- 语言指定:通过 `locale` 指定识别语言(如 `en-US`、`zh-CN`),提升识别准确率
- 流式背压处理:实时转写时处理发送速率与识别速率不匹配,避免缓冲堆积
- 会话管理:转写完成后关闭会话,释放服务端资源
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`azure-ai-transcription-py`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 批量转写

```python
job = client.begin_transcription(
    name="meeting-transcription",
    locale="en-US",
    content_urls=["https://<storage>/audio.wav"],
    diarization_enabled=True
)
result = job.result()
print(result.status)
```

`begin_transcription` 提交一个批量转写作业并立即返回作业句柄;`job.result()` 阻塞等待作业完成并返回结果。`content_urls` 指向可公开访问或带 SAS 的音频 URL。开启 `diarization_enabled` 后结果中会标注每段发言的说话人标识.
长音频建议优先用批量模式:服务端异步处理,不受客户端连接时长限制;结果可包含分通道、分说话人的完整文稿.
## 实时转写

```python
stream = client.begin_stream_transcription(locale="en-US")
stream.send_audio_file("audio.wav")
for event in stream:
    print(event.text)
```

`begin_stream_transcription` 建立一个流式会话;`send_audio_file` 把本地音频文件按块送入会话;迭代 `stream` 逐事件获取识别结果(含中间结果与最终结果)。适合会议同传、字幕生成、语音助手等需要低延迟反馈的场景.
实时转写对音频输入速率敏感:发送速率远超识别速率会产生背压,建议按块限速使其接近真实音频时长。中间结果会在最终结果到达后被覆盖,渲染字幕时须区分中间结果与最终结果,避免重复显示.
## 结果与状态

`job.result()` 返回结果对象,包含作业状态与转写内容。常见状态值:

- `Running`:作业仍在处理,继续轮询等待
- `Succeeded`:作业成功完成,可取回完整文稿
- `Failed`:作业失败,需检查 `content_urls` 可达性、`locale` 合法性与配额

结果内容按识别片段组织,每个片段含文本、起止时间戳与(开启时)说话人标识。批量结果可按通道、按说话人分组导出;实时结果按事件顺序累积,中间结果会被最终结果覆盖。导出 SRT/VTT 字幕时,把每个片段起止时间戳格式化为时间码(形如 `00:00:01,000 至 00:00:03,000`)与文本拼接成字幕条目;导出纯文稿时按片段顺序拼接文本并丢弃时间戳.
## 实践要点

1. 多说话人场景开启 `diarization`,结果中标注每段发言归属
2. 存储在 Blob 中的长文件用批量转写,避免客户端连接时长限制
3. 捕获时间戳用于字幕对齐与片段定位
4. 指定 `locale` 提升识别准确率,避免语言误判
5. 实时转写时处理流式背压,控制 `send_audio_file` 发送速率,避免缓冲堆积
6. 转写完成后关闭会话,释放服务端资源与连接配额

## 依赖

- Python 3.8 及以上
- `azure-ai-transcription` 包(通过 `pip install azure-ai-transcription` 安装)
- 已部署的 Azure AI 资源,获得 `TRANSCRIPTION_ENDPOINT` 与 `TRANSCRIPTION_KEY`
- 批量转写的音频须可通过 HTTPS 公开访问或附 SAS 令牌;实时转写的本地音频须为支持的格式(WAV / MP3 等)

## 适用场景

### 会议录音批量转写
将会议录音(WAV/MP3)上传至 Blob 存储并生成 SAS URL,提交批量转写作业并开启说话人分离,异步等待作业完成后取回分说话人的完整会议文稿。适合长会议、离线归档、会议纪要生成.
### 实时会议同传与字幕
建立流式会话,边采集音频边送入 `send_audio_file`,迭代事件流获取识别文本并实时渲染字幕。适合线上会议同传、直播字幕、语音助手等低延迟场景.
### 多说话人分离转写
对含多位发言人的音频(如圆桌讨论、访谈)开启 `diarization_enabled`,结果中标注每段发言的说话人标识,便于区分发言人、生成发言人维度统计。批量与实时模式均可使用.
### 字幕生成与片段定位
为识别结果启用时间戳捕获,把时间戳与文本对齐导出为 SRT/VTT 字幕格式;也可按时间戳定位关键片段做摘要或剪辑。适合视频字幕、播客归档、媒体资产管理.
## 案例

### 批量转写会议录音并分离说话人
用户有一段 90 分钟的会议录音 `meeting.wav` 已上传至 Blob 并得到 SAS URL。先配置环境变量 `TRANSCRIPTION_ENDPOINT` 与 `TRANSCRIPTION_KEY`,实例化 `TranscriptionClient`。调用 `begin_transcription(name="meeting-20260406", locale="zh-CN", content_urls=["https://<storage>/meeting.wav?<sas>"], diarization_enabled=True)`。`job.result()` 阻塞等待,完成后从 `result` 取回分说话人的完整文稿,每段发言附带说话人标识与时间戳。导出为会议纪要后关闭会话.
### 实时流式转写本地音频
用户需要把一段本地 `audio.wav` 实时转写为字幕。建立流式会话 `stream = client.begin_stream_transcription(locale="en-US")`,调用 `stream.send_audio_file("audio.wav")` 按块送入音频,迭代 `for event in stream` 获取识别事件,把 `event.text` 实时渲染到字幕层。处理流式背压避免发送速率过快,转写结束后关闭会话释放资源.
### 指定语言生成带时间戳字幕
用户有一段英文播客 `podcast.wav`,需要生成 SRT 字幕。批量提交 `begin_transcription(locale="en-US", content_urls=[...], diarization_enabled=False)`,在结果处理中提取每个识别片段的起始与结束时间戳,按 SRT 格式拼接序号、时间码与文本后写入 `podcast.srt`。指定 `en-US` 后专有名词识别准确率明显提升.
## 异常处理

### TRANSCRIPTION_ENDPOINT 未设置
实例化 `TranscriptionClient` 时 `os.environ["TRANSCRIPTION_ENDPOINT"]` 抛 `KeyError`。检查环境变量是否已导出(常见为 `https://<resource>.cognitiveservices.azure.com`),在 shell 或 `.env` 中配置后。不要把 endpoint 硬编码进源码.
### TRANSCRIPTION_KEY 无效(401/403)
调用转写接口返回 401 或 403。核对 `TRANSCRIPTION_KEY` 是否为该资源的有效订阅密钥(primary 或 secondary 均可),确认 endpoint 与 key 属于同一资源同一区域。密钥泄漏或轮换后旧 key 会失效,需更新环境变量.
### DefaultAzureCredential 不被支持
尝试用 `DefaultAzureCredential` 认证时报错。此客户端仅支持订阅密钥认证,改用 `credential=os.environ["TRANSCRIPTION_KEY"]` 传入订阅密钥。不要尝试用托管标识或工作负载标识.
### content_urls 不可访问
批量转写作业提交后长时间不返回或返回失败。确认 `content_urls` 指向的 URL 可被服务端公开访问或附带了未过期的 SAS 令牌;Blob 容器若为私有须生成只读 SAS;URL 协议须为 HTTPS.
### locale 不被支持
指定 `locale` 后识别准确率低或报错语言不支持。核对 locale 是否在 Azure AI Speech 支持的语言列表内(如 `en-US`、`zh-CN`、`ja-JP`),多语言音频可考虑自动语言识别或分段指定.
### 流式背压导致缓冲堆积
实时转写时 `send_audio_file` 发送速率过快,事件流消费不及时导致内存或缓冲堆积。控制发送速率使其接近真实音频时长(可按块限速),或在消费者侧异步处理事件;避免一次性灌入超长音频.
### 会话未关闭导致资源泄漏
实时转写结束后未关闭会话,服务端连接与配额未释放。转写完成后显式关闭会话(如 `stream.close()` 或使用 `with` 上下文管理),避免连接配额耗尽影响后续转写.
### 限流(429)
短时间内提交过多批量作业或并发流式会话触发服务限流。收到 429 时按 `Retry-After` 头退避后;对批量作业做队列化与并发上限控制;实时会话控制同时在线数.
## 常见问题

### Q1:批量转写与实时转写如何选择?
长音频(数十分钟以上)、已存储在 Blob、可离线处理、需要分说话人完整文稿的场景用批量转写;需要低延迟反馈、边录边出文字、会议同传与直播字幕场景用实时转写。两者都支持说话人分离与时间戳.
### Q2:如何认证?
此客户端仅支持订阅密钥认证,通过 `TRANSCRIPTION_ENDPOINT` 与 `TRANSCRIPTION_KEY` 环境变量配置资源,实例化时传入 `credential=os.environ["TRANSCRIPTION_KEY"]`。不支持 `DefaultAzureCredential`.
### Q3:如何开启说话人分离?
批量模式在 `begin_transcription` 中设置 `diarization_enabled=True`;实时模式按会话配置开启。开启后结果中标注每段发言的说话人标识。多说话人场景建议开启,单人录音可关闭以降低成本.
### Q4:locale 怎么填?
填 BCP-47 语言标签,如 `en-US`、`zh-CN`、`ja-JP`、`en-GB`。指定与音频一致的语言可显著提升识别准确率,避免语言误判。多语言音频可考虑自动语言识别或分段指定.
### Q5:如何处理长文件?
长文件优先用批量转写并存储在 Blob 中,服务端异步处理不受客户端连接时长限制;`job.result()` 阻塞等待完成。不要用实时流式会话处理超长音频,容易触发背压与超时.
### Q6:会话怎么管理?
实时转写完成后显式关闭会话释放服务端资源与连接配额,建议使用 `with` 上下文管理或 `try/finally` 确保异常路径也会关闭。批量作业通过轮询 `job.result()` 等待完成,无须显式关闭会话.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务,需要网络连接,断网时无法转写
- 仅支持订阅密钥认证,不支持 DefaultAzureCredential、托管标识等
- 批量转写要求音频可通过公开 URL 或 SAS 访问,纯本地文件须先上传
- 实时转写对超长音频容易触发背压,长文件建议用批量模式
- 识别准确率受音频质量、背景噪声、口音与 locale 匹配度影响
- 说话人分离为基于声纹的启发式标注,不保证完全准确,跨频道同说话人可能合并
- 服务端有并发与限流配额,高频提交需做队列化与退避
