---
slug: "azure-ai-voicelive-py"
name: "azure-ai-voicelive-py"
version: 0.1.1
displayName: "Azure实时语音AI开发"
summary: "基于Azure VoiceLive SDK构建实时双向语音AI应用,支持流式音频、转写、函数调用与多语音模型。"
license: "Proprietary"
description: |-
  面向Azure VoiceLive SDK的实时语音AI开发技能,覆盖WebSocket双向通信、流式音频输入输出、
  实时转写、会话管理、VAD端点检测、函数调用工具集成与多语音模型选择。适用于构建语音助手、
  客服对话、实时翻译、会议转写等场景。支持DefaultAzureCredential与API Key两种认证方式,
  兼容pcm16、g711等多种音频格式,适配24kHz高保真与8kHz电话场景.
tags:
  - 通用办公
  - voice
  - azure
  - realtime
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Azure VoiceLive 实时语音AI开发

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure实时语音AI开发处理的输入数据或指令 |
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

- 通过 `azure.ai.voicelive.aio.connect` 建立与Azure认知服务的WebSocket双向流式连接,使用 `gpt-4o-realtime-preview` 等实时模型进行低延迟语音对话
- 管理 `VoiceLiveConnection` 的六大资源: `session`(会话配置)、`response`(模型响应)、`input_audio_buffer`(音频输入)、`output_audio_buffer`(音频输出)、`conversation`(对话状态)、`transcription_session`(转写配置)
- 支持服务端VAD (`server_vad`) 与Azure语义VAD (`azure_semantic_vad` / `azure_semantic_vad_en` / `azure_semantic_vad_multilingual`) 多种端点检测模式,可调阈值、静音时长与前缀填充
- 内置 `alloy`、`echo`、`shimmer`、`sage`、`coral`、`ash`、`ballad`、`verse` 八种OpenAI音色,以及 `AzureStandardVoice`、`AzureCustomVoice`、`AzurePersonalVoice` 三类Azure原生语音
- 支持函数调用 (`FunctionTool`): 模型生成调用参数后通过 `conversation.item.create` 回填JSON输出并触发 `response.create` 完成多轮工具链
- 支持中断处理: 监听 `input_audio_buffer.speech_started` 事件后调用 `response.cancel` 与 `output_audio_buffer.clear` 实现用户打断响应
- 兼容 `pcm16` (24kHz默认)、`pcm16-8000hz`、`pcm16-16000hz`、`g711_ulaw`、`g711_alaw` 多种音频格式,适配电话、语音助手、高保真等场景
- 双重认证: `DefaultAzureCredential`(托管身份/AAD令牌)与 `AzureKeyCredential`(API密钥),前者通过 `credential_scopes` 指定作用域
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`azure-ai-voicelive-py`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 适用场景

- **实时语音助手**: 构建可中断、可工具调用的低延迟语音对话应用,适用于智能硬件、车载、客服前置等
- **会议实时转写**: 通过 `transcription_session` 持续输出 `conversation.item.input_audio_transcription.delta` 与 `completed` 事件,生成可读字幕流
- **电话客服IVR**: 使用 `g711_ulaw`/`g711_alaw` 8kHz格式接入SIP/PSTN电话网络,搭配 `azure_semantic_vad` 处理短促话音
- **多模态交互机器人**: 同一会话内文本与音频混合输入,通过 `conversation.item.create` 注入历史上下文,实现长程记忆对话

## 安装与环境

```bash
pip install azure-ai-voicelive aiohttp azure-identity
```

必要环境变量:
```bash
AZURE_COGNITIVE_SERVICES_ENDPOINT=https://<region>.api.cognitive.microsoft.com
AZURE_COGNITIVE_SERVICES_KEY=<api-key>
```

## 认证方式

**DefaultAzureCredential (推荐,生产环境)**:
```python
from azure.ai.voicelive.aio import connect
from azure.identity.aio import DefaultAzureCredential
# ...
async with connect(
    endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
    credential=DefaultAzureCredential(),
    model="gpt-4o-realtime-preview",
    credential_scopes=["https://cognitiveservices.azure.com/.default"]
) as conn:
    ...
```

**API Key (快速验证)**:
```python
from azure.ai.voicelive.aio import connect
from azure.core.credentials import AzureKeyCredential
# ...
async with connect(
    endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
    model="gpt-4o-realtime-preview"
) as conn:
    ...
```

## 会话配置

```python
from azure.ai.voicelive.models import RequestSession, FunctionTool
# ...
await conn.session.update(session=RequestSession(
    instructions="You are a helpful voice assistant.",
    modalities=["text", "audio"],
    voice="alloy",
    input_audio_format="pcm16",
    output_audio_format="pcm16",
    turn_detection={
        "type": "server_vad",
        "threshold": 0.5,
        "prefix_padding_ms": 300,
        "silence_duration_ms": 500
    },
    tools=[
        FunctionTool(
            type="function",
            name="get_weather",
            description="Get current weather",
            parameters={
                "type": "object",
                "properties": {"location": {"type": "string"}},
                "required": ["location"]
            }
        )
    ]
))
```

## 案例展示

### 案例一： 完整语音对话循环

建立连接、配置会话、监听事件并处理音频输入输出与函数调用:
```python
import asyncio, os, json, base64
from azure.ai.voicelive.aio import connect
from azure.identity.aio import DefaultAzureCredential
# ...
def handle_function(name, arguments):
    if name == "get_weather":
        return {"temperature": 26, "condition": "sunny"}
    return {}
# ...
async def main():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
        credential_scopes=["https://cognitiveservices.azure.com/.default"]
    ) as conn:
        await conn.session.update(session={
            "instructions": "You are a helpful assistant.",
            "modalities": ["text", "audio"],
            "voice": "alloy"
        })
# ...
        async for event in conn:
            if event.type == "response.audio_transcript.done":
                print(f"Transcript: {event.transcript}")
            elif event.type == "response.audio.delta":
                audio_bytes = base64.b64decode(event.delta)
                # 将audio_bytes送入扬声器播放
            elif event.type == "response.function_call_arguments.done":
                result = handle_function(event.name, event.arguments)
                await conn.conversation.item.create(item={
                    "type": "function_call_output",
                    "call_id": event.call_id,
                    "output": json.dumps(result)
                })
                await conn.response.create()
            elif event.type == "response.done":
                break
# ...
asyncio.run(main())
```

### 案例二： 手动轮次模式 (无VAD)

关闭VAD后由业务侧控制用户话音结束时机,适用于按键说话或外部分片场景:
```python
await conn.session.update(session={"turn_detection": None})
# ...
# 注入音频块
audio_chunk = await read_audio_from_microphone()
b64_audio = base64.b64encode(audio_chunk).decode()
await conn.input_audio_buffer.append(audio=b64_audio)
# ...
# 显式结束用户轮次并触发响应
await conn.input_audio_buffer.commit()
await conn.response.create()
```

### 案例三： 用户打断处理

监听用户重新说话事件,取消当前未完成的响应并清空输出缓冲:
```python
async for event in conn:
    if event.type == "input_audio_buffer.speech_started":
        await conn.response.cancel()
        await conn.output_audio_buffer.clear()
    elif event.type == "input_audio_buffer.speech_stopped":
        print(f"Speech stopped at {event.audio_end_ms}ms")
```

## 事件参考

`async for event in conn` 可迭代以下事件:
- 会话事件: `session.created`、`session.updated`
- 音频输入: `input_audio_buffer.speech_started`、`input_audio_buffer.speech_stopped`
- 转写: `conversation.item.input_audio_transcription.delta`、`conversation.item.input_audio_transcription.completed`
- 响应: `response.created`、`response.audio.delta`、`response.audio_transcript.delta`、`response.audio_transcript.done`、`response.done`
- 函数调用: `response.function_call_arguments.done`
- 错误: `error` (包含 `event.error.code` 与 `event.error.message`)

## 异常处理

### WebSocket连接中断
现象: 抛出 `ConnectionClosed`,带 `code` 与 `reason`.
原因: 网络抖动、服务端超时、鉴权令牌过期.
处理: 捕获 `ConnectionClosed` 后重新 `connect()` 并恢复 `session.update`,长连接场景建议外层 `while True` 并指数退避.
### 鉴权失败 (401/403)
现象: 事件流中收到 `error`, `code` 为 `unauthorized` 或 `forbidden`.
原因: `AZURE_COGNITIVE_SERVICES_KEY` 错误、AAD主体未授予认知服务权限、`credential_scopes` 写错.
处理: 用 `az cognitiveservices account keys list` 复核密钥;AAD方式确认子主体已加入资源 `Cognitive Services User` 角色;`credential_scopes` 必须为 `https://cognitiveservices.azure.com/.default`.
### 音频格式不匹配
现象: 上行音频被服务端丢弃,日志出现 `invalid_audio_format`.
原因: `input_audio_format` 配置与实际采样率/编码不一致,例如设备是16kHz但配置为 `pcm16` (24kHz).
处理: 用 `pyaudio`/`sounddevice` 检查实际采样率,改为 `pcm16-16000hz`;G711电话流必须显式指定 `g711_ulaw` 或 `g711_alaw`.
### VAD端点漏判
现象: 用户话音未结束就被 `speech_stopped` 触发响应,或停顿后未触发响应.
原因: `server_vad.threshold` 过高/过低,`silence_duration_ms` 太短.
处理: 嘈杂环境调高 `threshold` 至 0.6-0.7;温和场景降至 0.3-0.4;`silence_duration_ms` 默认500ms,中文对话可调至700ms.
### 函数调用回填丢失
现象: 模型不再继续响应,事件流停滞在 `response.function_call_arguments.done`.
原因: 未调用 `conn.conversation.item.create` 注入 `function_call_output`,或 `call_id` 不匹配.
处理: 始终用事件提供的 `event.call_id` 作为回填 `call_id`;回填后必须显式 `await conn.response.create()` 触发下一轮响应.
### 音色不可用
现象: `session.update` 返回 `voice_not_found` 错误.
原因: 指定音色在当前区域/模型不可用,例如Azure原生音色未在资源上部署.
处理: OpenAI系列音色用字符串名 (`alloy`/`echo` 等);Azure原生音色需用 `AzureStandardVoice`/`AzureCustomVoice`/`AzurePersonalVoice` 模型对象,且确认资源已部署对应音色.
### 响应被取消后状态不一致
现象: 调用 `response.cancel()` 后再次 `response.create()` 报 `response_already_active`.
原因: 取消是异步操作,未等待完成就触发新响应.
处理: 在 `response.cancel()` 协程完成后再调用 `response.create()`;必要时先 `output_audio_buffer.clear()` 重置输出.
### 并发音频追加冲突
现象: `input_audio_buffer.append` 抛 `concurrent_append` 错误.
原因: 多个协程同时向同一连接写入音频块.
处理: 用 `asyncio.Lock` 串行化对 `input_audio_buffer` 的写入,或采用单生产者协程从音频队列消费.
## 常见问题

### Q1: DefaultAzureCredential 与 API Key 该选哪个?
生产环境优先 `DefaultAzureCredential`,可结合托管身份、AAD令牌、Key Vault轮换,避免密钥硬编码;本地快速验证或无AAD环境用 `AzureKeyCredential`,密钥通过环境变量注入而非源码.
### Q2: 如何降低端到端延迟?
启用 `server_vad` 让服务端自动判定话音起止,避免本地VAD往返;`prefix_padding_ms` 设为200-300ms防截断;`input_audio_format` 使用 `pcm16` 24kHz;播放端使用环形缓冲区而非整段缓存;模型选 `gpt-4o-realtime-preview` 而非标准版.
### Q3: 如何在对话中保留历史上下文?
通过 `conn.conversation.item.create` 显式注入 `type=message` 的 `system`/`user`/`assistant` 消息,`content` 数组中 `input_text`/`output_text`/`input_audio`/`output_audio` 类型混合存在;服务端会按注入顺序维护对话历史.
### Q4: 能否同时拿到音频流和文字转写?
可以。`modalities=["text","audio"]` 配置后,同一响应会同时派发 `response.audio.delta` 与 `response.audio_transcript.delta`,前者为base64 PCM,后者为增量文本,业务侧可分别消费.
### Q5: Azure原生音色和OpenAI音色有什么区别?
OpenAI音色 (`alloy`/`echo`/`shimmer` 等) 走实时模型内置TTS;Azure原生音色 (`AzureStandardVoice`/`AzureCustomVoice`/`AzurePersonalVoice`) 走Azure语音服务,支持自定义音色与神经语音克隆,但需要在Azure语音资源上单独部署.
### Q6: 通话中断后如何恢复对话?
`VoiceLiveConnection` 是无状态WebSocket,断线后必须重新 `connect()` 建立新会话;若要恢复语义上下文,需把历史 `conversation.item` 重新通过 `item.create` 注入新会话,服务端不会自动持久化.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持Azure OpenAI实时模型 (如 `gpt-4o-realtime-preview`),不兼容标准Chat Completion API
- WebSocket长连接依赖稳定网络,断线后对话上下文不会自动恢复
- Azure原生音色 (`AzureCustomVoice`/`AzurePersonalVoice`) 需在Azure语音资源上单独部署,不支持即时切换
- `transcription_session` 与 `session` 不能在同一连接上同时启用实时响应与纯转写模式
- 音频输出格式受模型限制,部分模型仅支持 `pcm16` 24kHz
- 函数调用结果必须为JSON字符串,且 `call_id` 来自服务端事件,业务侧不能自行生成
