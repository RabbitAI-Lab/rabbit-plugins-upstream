---
slug: "azure-voicelive"
name: "azure-voicelive"
version: 1.0.1
displayName: "Azure语音交互专业版"
summary: "企业级实时语音AI工具，支持函数调用、自定义语音、电话音频、高级会话与中断处理。"
license: "Proprietary"
edition: "pro"
description: |-
  Azure语音交互专业版 —— 面向企业团队与专业开发者的高级实时语音AI工具。核心能力:
  - 函数调用（Function Tools），支持AI主动调用外部API
  - 自定义语音集成：Azure标准语音、自定义语音、个人语音
  - 电话音频格式支持：G。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - 语音AI
  - Azure
  - 企业工具
  - 函数调用
  - 电话客服
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Azure语音交互专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Azure语音交互专业版高级会话与中断处理 | 不支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |

## 核心能力

### 1. 函数调用（Function Tools）

```python
import json
from azure.ai.voicelive.models import FunctionTool
# ...
async def voice_assistant_with_tools():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
    ) as conn:
        # 配置带函数工具的会话
        await conn.session.update(session=RequestSession(
            instructions="你是智能客服助手，可以查询订单和天气信息。",
            modalities=["text", "audio"],
            voice="shimmer",
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
                    name="get_order_status",
                    description="查询订单状态",
                    parameters={
                        "type": "object",
                        "properties": {
                            "order_id": {"type": "string", "description": "订单号"}
                        },
                        "required": ["order_id"]
                    }
                ),
                FunctionTool(
                    type="function",
                    name="get_weather",
                    description="查询天气信息",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {"type": "string", "description": "城市名"}
                        },
                        "required": ["location"]
                    }
                )
            ]
        ))
# ...
        # 事件处理（含函数调用）
        async for event in conn:
            match event.type:
                case "response.function_call_arguments.done":
                    # AI请求调用函数
                    result = await handle_function(event.name, event.arguments)
                    await conn.conversation.item.create(item={
                        "type": "function_call_output",
                        "call_id": event.call_id,
                        "output": json.dumps(result)
                    })
                    await conn.response.create()  # 触发后续响应
# ...
                case "response.audio_transcript.delta":
                    print(event.delta, end="", flush=True)
# ...
                case "response.audio.delta":
                    audio = base64.b64decode(event.delta)
                    await play_audio(audio)
# ...
                case "response.done":
                    break
# ...
async def handle_function(name, arguments):
    """处理AI请求的函数调用"""
    args = json.loads(arguments)
    if name == "get_order_status":
        return {"order_id": args["order_id"], "status": "已发货", "eta": "明天到达"}
    elif name == "get_weather":
        return {"location": args["location"], "temp": "25℃", "condition": "晴"}
    return {"error": "未知函数"}
```- 验证返回数据的完整性和格式正确性
- 参考`中断处理与手动轮次`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`电话音频格式支持`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`函数调用（Function Tools）`的配置文档进行参数调优
### 2. 电话音频格式支持

```python
# 电话客服系统配置（G.711格式）
async def telephony_voice_bot():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
    ) as conn:
        await conn.session.update(session={
            "instructions": "你是电话客服，请简洁专业地回答。",
            "modalities": ["text", "audio"],
            "voice": "shimmer",
            "input_audio_format": "g711_ulaw",   # 电话音频格式
            "output_audio_format": "g711_ulaw",
            "turn_detection": {
                "type": "server_vad",
                "threshold": 0.5,
                "silence_duration_ms": 600
            }
        })
        # ... 事件处理逻辑
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `电话音频格式支持` 选项
- 处理流程: 接收输入 -> 执行电话音频格式支持 -> 返回结果
- 输入: 用户提供电话音频格式支持所需的参数和指令
- 输出: 返回电话音频格式支持的处理结果,包含执行状态码、结果数据和执行日志

### 3. 中断处理与手动轮次

```python
# 用户中断处理
async def interruptible_assistant():
    async with connect(...) as conn:
        await conn.session.update(session={
            "instructions": "你是语音助手。",
            "modalities": ["text", "audio"],
            "voice": "alloy",
            "turn_detection": {"type": "server_vad", "threshold": 0.5}
        })
# ...
        async for event in conn:
            if event.type == "input_audio_buffer.speech_started":
                # 用户开始说话 → 取消当前AI响应
                await conn.response.cancel()
                await conn.output_audio_buffer.clear()
                print("[用户打断，已停止当前回复]")
# ...
            elif event.type == "response.audio.delta":
                audio = base64.b64decode(event.delta)
                await play_audio(audio)
# ...
# 手动轮次模式（无VAD）
async def manual_turn_mode():
    async with connect(...) as conn:
        # 关闭自动VAD
        await conn.session.update(session={"turn_detection": None})
# ...
        # 手动发送音频并提交
        audio_chunk = await read_audio_from_microphone()
        b64_audio = base64.b64encode(audio_chunk).decode()
        await conn.input_audio_buffer.append(audio=b64_audio)
        await conn.input_audio_buffer.commit()  # 结束用户轮次
        await conn.response.create()            # 触发AI响应
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `中断处理与手动轮次` 选项
- 处理流程: 接收输入 -> 执行中断处理与手动轮次 -> 返回结果
- 输入: 用户提供中断处理与手动轮次所需的参数和指令
- 输出: 返回中断处理与手动轮次的处理结果,包含执行状态码、结果数据和执行日志

### 4. 自定义语音集成
```python
from azure.ai.voicelive.models import AzureStandardVoice, AzureCustomVoice
# ...
# 使用Azure标准语音
await conn.session.update(session={
    "voice": AzureStandardVoice(
        voice_name="zh-CN-XiaoxiaoNeural",
        voice_type="AzureStandardVoice"
    )
})
# ...
# 使用自定义语音（品牌专属语音）
await conn.session.update(session={
    "voice": AzureCustomVoice(
        voice_name="my-brand-voice",
        voice_type="AzureCustomVoice",
        custom_voice_endpoint="https://<endpoint>"
    )
})
```

**输入**: 用户提供自定义语音集成所需的指令和必要参数.
**处理**: 解析自定义语音集成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回自定义语音集成的处理结果,包含执行状态码、结果数据和执行日志。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `自定义语音集成` 选项

#
## 适用场景

### 场景一：企业智能客服系统

企业客服中心部署AI语音助手，支持查询订单、天气等功能调用.
```python
async def enterprise_customer_service():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
        credential_scopes=["https://cognitiveservices.azure.com/.default"]
    ) as conn:
        await conn.session.update(session=RequestSession(
            instructions="你是XX公司智能客服。可以查询订单状态、产品信息、退换货政策。保持专业友好的语气。",
            modalities=["text", "audio"],
            voice="shimmer",
            input_audio_format="pcm16",
            output_audio_format="pcm16",
            turn_detection={
                "type": "azure_semantic_vad",  # 语义VAD，更准确的端点检测
                "threshold": 0.5
            },
            tools=[
                FunctionTool(type="function", name="query_order",
                    description="查询订单状态",
                    parameters={"type": "object",
                        "properties": {"order_id": {"type": "string"}},
                        "required": ["order_id"]}),
                FunctionTool(type="function", name="query_product",
                    description="查询产品信息",
                    parameters={"type": "object",
                        "properties": {"product_name": {"type": "string"}},
                        "required": ["product_name"]}),
                FunctionTool(type="function", name="return_policy",
                    description="查询退换货政策",
                    parameters={"type": "object", "properties": {}})
            ]
        ))
# ...
        async for event in conn:
            if event.type == "response.function_call_arguments.done":
                result = await handle_service_function(event.name, event.arguments)
                await conn.conversation.item.create(item={
                    "type": "function_call_output",
                    "call_id": event.call_id,
                    "output": json.dumps(result)
                })
                await conn.response.create()
            elif event.type == "input_audio_buffer.speech_started":
                await conn.response.cancel()
                await conn.output_audio_buffer.clear()
            elif event.type == "response.done":
                pass  # 继续监听
```

### 场景二：电话客服AI语音机器人

电话客服系统接入AI语音，处理来电咨询.
```python
async def telephony_bot():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=AzureKeyCredential(os.environ["AZURE_COGNITIVE_SERVICES_KEY"]),
        model="gpt-4o-realtime-preview"
    ) as conn:
        # 电话音频格式配置
        await conn.session.update(session={
            "instructions": "你是电话客服机器人，回答简洁明了。",
            "modalities": ["text", "audio"],
            "voice": AzureStandardVoice(voice_name="zh-CN-YunxiNeural"),
            "input_audio_format": "g711_ulaw",  # 电话格式
            "output_audio_format": "g711_ulaw",
            "turn_detection": {
                "type": "server_vad",
                "threshold": 0.5,
                "silence_duration_ms": 700  # 电话场景适当延长静默时间
            }
        })
# ...
        # 对话历史管理
        await conn.conversation.item.create(item={
            "type": "message",
            "role": "system",
            "content": [{"type": "input_text", "text": "当前来电号码: 138详情见说明x1234"}]
        })
# ...
        # ... 事件处理
```

### 场景三：品牌定制语音体验

品牌应用使用专属定制语音，提供独特交互体验.
```python
async def branded_voice_experience():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
        credential_scopes=["https://cognitiveservices.azure.com/.default"]
    ) as conn:
        # 品牌定制语音
        await conn.session.update(session={
            "instructions": "你是XX品牌的专属语音助手，体现品牌温暖专业的调性。",
            "modalities": ["text", "audio"],
            "voice": AzureCustomVoice(
                voice_name="brand-exclusive-voice",
                custom_voice_endpoint="https://<custom-voice-endpoint>"
            ),
            "input_audio_format": "pcm16",
            "output_audio_format": "pcm16",
            "turn_detection": {"type": "azure_semantic_vad_multilingual"}
        })
        # ... 事件处理
```

## 使用流程

### 1. 环境准备

```bash
pip install azure-ai-voicelive aiohttp azure-identity
```

### 2. 托管身份认证配置

```bash
# 使用DefaultAzureCredential（推荐企业使用）
export AZURE_COGNITIVE_SERVICES_ENDPOINT="https://<region>.api.cognitive.microsoft.com"
# 通过Azure CLI登录
az login
```

### 3. 函数调用语音助手

```python
import asyncio, os, json, base64
from azure.ai.voicelive.aio import connect
from azure.ai.voicelive.models import RequestSession, FunctionTool
from azure.identity.aio import DefaultAzureCredential
# ...
async def main():
    async with connect(
        endpoint=os.environ["AZURE_COGNITIVE_SERVICES_ENDPOINT"],
        credential=DefaultAzureCredential(),
        model="gpt-4o-realtime-preview",
        credential_scopes=["https://cognitiveservices.azure.com/.default"]
    ) as conn:
        await conn.session.update(session=RequestSession(
            instructions="你是智能助手。",
            modalities=["text", "audio"],
            voice="alloy",
            tools=[FunctionTool(type="function", name="get_time",
                description="获取当前时间",
                parameters={"type": "object", "properties": {}})]
        ))
        async for event in conn:
            if event.type == "response.function_call_arguments.done":
                if event.name == "get_time":
                    await conn.conversation.item.create(item={
                        "type": "function_call_output",
                        "call_id": event.call_id,
                        "output": json.dumps({"time": "2026-01-18 10:00"})
                    })
                    await conn.response.create()
            elif event.type == "response.done":
                break
# ...
asyncio.run(main())
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | azure-voicelive处理的内容输入 |, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| azure-ai-voicelive | Python SDK | 必需 | `pip install azure-ai-voicelive` |
| aiohttp | Python库 | 必需 | `pip install aiohttp` |
| azure-identity | Python库 | 必需 | `pip install azure-identity` |
| Azure认知服务 | 云服务 | 必需 | Azure门户创建资源 |

### API Key 配置

- `AZURE_COGNITIVE_SERVICES_ENDPOINT`：Azure认知服务端点URL
- `AZURE_COGNITIVE_SERVICES_KEY`：API密钥（API Key认证）
- 支持DefaultAzureCredential托管身份认证（企业推荐）
- 与免费版使用相同的端点配置，完全兼容

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业实时语音交互任务。支持函数调用、自定义语音、电话音频格式等企业级功能，通过Python异步SDK调用Azure VoiceLive服务。与免费版完全兼容，可直接复用免费版的认证配置与基础会话流程.
**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 音频格式对比

| 格式 | 采样率 | 适用场景 |
|:------|------:|:------|
| `pcm16` | 24kHz | 默认，高质量 |
| `pcm16-8000hz` | 8kHz | 电话 |
| `pcm16-16000hz` | 16kHz | 语音助手 |
| `g711_ulaw` | 8kHz | 电话（美国） |
| `g711_alaw` | 8kHz | 电话（欧洲） |

### VAD选项对比

| VAD类型 | 说明 | 适用场景 |
|---:|:---|---:|
| `server_vad` | 基于阈值的服务器端检测 | 通用场景 |
| `azure_semantic_vad` | 语义级端点检测 | 高精度场景 |
| `azure_semantic_vad_multilingual` | 多语言语义检测 | 多语言应用 |

### 语音类型对比

| 类型 | 说明 | 适用场景 |
|:------:|--------|:-------|
| 内置语音 | alloy/echo/shimmer等 | 通用 |
| AzureStandardVoice | Azure神经语音 | 生产环境 |
| AzureCustomVoice | 自定义训练语音 | 品牌专属 |
| AzurePersonalVoice | 个人语音克隆 | 个性化 |

## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 常见问题

### Q1：函数调用不触发怎么办？

检查函数工具的description是否清晰，parameters定义是否正确。AI需要理解何时调用哪个函数.
### Q2：电话音频质量不佳怎么办？

确保使用正确的G.711格式（美国用ulaw，欧洲用alaw），适当调整silence_duration_ms.
## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 
- 和网络环境
