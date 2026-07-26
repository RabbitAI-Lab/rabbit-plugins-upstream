---
slug: "azure-ai-voicelive-py-free"
name: "azure-ai-voicelive-py-free"
version: "1.0.0"
displayName: "Azure实时语音AI免费版"
summary: "Azure VoiceLive SDK基础实时语音对话能力,支持API Key认证、流式音频与文字转写。"
license: "MIT"
description: |-
  Azure VoiceLive SDK基础版技能,提供WebSocket双向连接、API Key认证、
  pcm16音频流式输入输出与文字转写能力。适用于快速验证语音对话效果、
  构建简单语音助手原型。仅支持OpenAI系列音色与服务端VAD,不包含
  函数调用、Azure原生音色、多VAD模式等高级特性.
tags:
  - 通用办公
  - voice
  - azure
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Azure VoiceLive 实时语音AI (免费版)

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure实时语音AI免费版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
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

- 通过 `azure.ai.voicelive.aio.connect` 建立与Azure认知服务的WebSocket双向流式连接,使用 `gpt-4o-realtime-preview` 实时模型进行语音对话
- 使用 `AzureKeyCredential` API密钥认证,通过 `AZURE_COGNITIVE_SERVICES_ENDPOINT` 与 `AZURE_COGNITIVE_SERVICES_KEY` 环境变量配置
- 支持 `session.update` 配置 `instructions`、`modalities`、`voice` 与 `input_audio_format`/`output_audio_format`
- 内置 `alloy`、`echo`、`shimmer` 三种基础OpenAI音色,默认音频格式 `pcm16` (24kHz)
- 监听 `response.audio.delta` 接收base64 PCM音频,`response.audio_transcript.done` 接收完整文字转写
- 支持服务端VAD (`server_vad`) 自动检测话音起止,默认 `threshold` 0.5、`silence_duration_ms` 500ms
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`azure-ai-voicelive-py-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 适用场景

- **语音助手原型**: 快速搭建可对话的语音助手Demo,验证Azure实时模型效果
- **文字转写验证**: 通过 `modalities=["text","audio"]` 同时获取音频与转写文本,用于校验识别准确率

## 安装与环境

```bash
pip install azure-ai-voicelive aiohttp
```

必要环境变量:
```bash
AZURE_COGNITIVE_SERVICES_ENDPOINT=https://<region>.api.cognitive.microsoft.com
AZURE_COGNITIVE_SERVICES_KEY=<api-key>
```

## 基础用法

```python
import asyncio, os
from azure.ai.voicelive.aio import connect
from azure.core.credentials import AzureKeyCredential
# ...
async def main():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
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
            elif event.type == "response.done":
                break
# ...
asyncio.run(main())
```

## 案例展示

### 案例一： 接收音频流并解码播放

监听 `response.audio.delta` 事件,将base64音频块解码为PCM字节送入扬声器:
```python
import base64
# ...
async for event in conn:
    if event.type == "response.audio.delta":
        audio_bytes = base64.b64decode(event.delta)
        # 将audio_bytes写入音频播放设备
    elif event.type == "response.audio.done":
        print("Audio playback complete")
    elif event.type == "response.done":
        break
```

### 案例二： 发送麦克风音频

读取麦克风PCM块,base64编码后通过 `input_audio_buffer.append` 上行:
```python
import base64
# ...
audio_chunk = await read_audio_from_microphone()
b64_audio = base64.b64encode(audio_chunk).decode()
await conn.input_audio_buffer.append(audio=b64_audio)
```

## 异常处理

### WebSocket连接中断
现象: 抛出 `ConnectionClosed` 异常,带 `code` 与 `reason`.
原因: 网络抖动、服务端超时、长时间无音频收发.
处理: 捕获异常后重新调用 `connect()` 建立连接并重新 `session.update`,简单场景可外层 `while True` 检查网络连接和配置后重试3次.
### 鉴权失败 (401)
现象: 事件流收到 `error` 事件,`code` 为 `unauthorized`.
原因: `AZURE_COGNITIVE_SERVICES_KEY` 错误或已轮换、endpoint区域与资源不匹配.
处理: 在Azure门户复核密钥,确认endpoint域名中的region与资源部署区域一致;密钥通过环境变量注入,避免硬编码.
### 音色不可用
现象: `session.update` 返回 `voice_not_found`.
原因: 免费版仅支持 `alloy`/`echo`/`shimmer` 三种基础音色,其他音色需付费版.
处理: 切换到三种基础音色之一;若需 `sage`/`coral`/`ash`/`ballad`/`verse` 或Azure原生音色,请升级付费版.
### 事件流无响应
现象: 调用 `response.create()` 后长时间未收到任何事件.
原因: 会话未配置 `modalities`,或 `instructions` 为空导致模型无输出.
处理: 确认 `session.update` 已设置 `modalities=["text","audio"]` 与非空 `instructions`;检查 `input_audio_buffer.commit()` 是否在手动模式下被调用.
### 音频格式不匹配
现象: 上行音频被服务端丢弃,转写结果为空.
原因: 实际采样率与 `input_audio_format` 配置不一致.
处理: 免费版默认 `pcm16` 24kHz,麦克风采集需匹配该采样率;若设备为16kHz需付费版支持 `pcm16-16000hz`.
## 常见问题

### Q1: 免费版支持哪些音色?
免费版仅支持 `alloy`、`echo`、`shimmer` 三种基础OpenAI音色。`sage`、`coral`、`ash`、`ballad`、`verse` 与Azure原生音色 (`AzureStandardVoice`/`AzureCustomVoice`/`AzurePersonalVoice`) 需升级付费版.
### Q2: 免费版能用DefaultAzureCredential吗?
免费版仅支持 `AzureKeyCredential` API密钥认证。`DefaultAzureCredential`(托管身份/AAD令牌/Key Vault轮换)属付费版能力,适合生产环境.
### Q3: 如何同时拿到音频和文字?
配置 `modalities=["text","audio"]` 后,同一响应会同时派发 `response.audio.delta`(base64 PCM)与 `response.audio_transcript.delta`(增量文本),`response.audio_transcript.done` 给出完整转写.
### Q4: 免费版支持函数调用吗?
不支持。`FunctionTool` 工具集成、`response.function_call_arguments.done` 事件处理与 `conversation.item.create` 回填流程属付费版能力.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持 `alloy`/`echo`/`shimmer` 三种基础音色,不包含5种扩展音色与Azure原生音色
- 仅支持 `AzureKeyCredential` 认证,不包含 `DefaultAzureCredential` 托管身份
- 仅支持 `server_vad` 端点检测,不包含 `azure_semantic_vad` 系列语义VAD
- 不支持 `FunctionTool` 函数调用与多轮工具链
- 不支持手动轮次模式 (`turn_detection: None`) 与用户打断处理
- 默认音频格式 `pcm16` 24kHz,不包含8kHz/16kHz/G711电话格式

## 升级提示

当前为免费版,仅包含基础语音对话能力。升级付费版可获得:
- 完整8种OpenAI音色 + Azure原生音色 (`AzureCustomVoice`/`AzurePersonalVoice`)
- `DefaultAzureCredential` 托管身份认证,适配生产环境
- `FunctionTool` 函数调用与多轮工具链
- `azure_semantic_vad` 语义VAD与手动轮次模式
- `pcm16-8000hz`/`pcm16-16000hz`/`g711_ulaw`/`g711_alaw` 电话音频格式
- 用户打断处理与 `transcription_session` 纯转写模式

付费版slug: `azure-ai-voicelive-py`

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Azure实时语音AI免费版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "azure-ai-voicelive-py"
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
