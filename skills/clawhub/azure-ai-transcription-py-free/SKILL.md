---
slug: "azure-ai-transcription-py-free"
name: "azure-ai-transcription-py-free"
version: "1.0.0"
displayName: "Azure语音转文字基础版"
summary: "Azure AI Transcription 基础功能,支持批量语音转文字与语言指定"
license: "MIT"
description: |-
  Azure AI Transcription 的 Python 客户端库基础功能。支持对存储在 Blob 中的音频
  提交批量转写作业,通过 locale 指定识别语言。使用订阅密钥认证,通过
  TRANSCRIPTION_ENDPOINT 与 TRANSCRIPTION_KEY 环境变量配置资源。本基础版不含
  实时流式转写、说话人分离、时间戳字幕生成等高级能力.
tags:
  - 系统运维
  - Speech
tools:
  - read
  - exec
homepage: "https://skillhub.cn"

---
# Azure Ai Transcription Py Free

Azure AI Transcription(speech-to-text)Python 客户端库基础功能,支持批量转写.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Azure语音转文字基础版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 安装

```bash
pip install azure-ai-transcription
```

## 环境变量

```bash
TRANSCRIPTION_ENDPOINT=https://<resource>.cognitiveservices.azure.com
TRANSCRIPTION_KEY=API_KEY
```

`TRANSCRIPTION_ENDPOINT` 为 Azure AI 资源终结点,`TRANSCRIPTION_KEY` 为该资源的订阅密钥(primary 或 secondary 均可)。两个变量建议放入 `.env` 或系统环境变量,不要硬编码进源码;密钥泄漏后须在门户轮换并更新变量.
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

- 批量转写:对存储在 Blob 中的音频文件提交转写作业,异步等待完成
- 语言指定:通过 `locale` 指定识别语言(如 `en-US`、`zh-CN`),提升识别准确率
- 订阅密钥认证:通过环境变量配置资源,实例化时传入密钥
- 作业结果查询:`job.result()` 阻塞等待作业完成并返回结果
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`azure-ai-transcription-py-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 批量转写

```python
job = client.begin_transcription(
    name="meeting-transcription",
    locale="en-US",
    content_urls=["https://<storage>/audio.wav"]
)
result = job.result()
print(result.status)
```

`begin_transcription` 提交一个批量转写作业并立即返回作业句柄;`job.result()` 阻塞等待作业完成并返回结果。`content_urls` 指向可公开访问或带 SAS 的音频 URL.
## 结果处理

`result.status` 反映作业状态:`Succeeded` 表示成功可取回文稿,`Failed` 表示失败需检查 `content_urls` 可达性与 `locale` 合法性。结果按识别片段组织,每个片段含文本与时间戳。导出纯文稿时按片段顺序拼接文本即可;导出字幕时把每个片段起止时间戳格式化为时间码(形如 `00:00:01,000 至 00:00:03,000`)与文本拼接成字幕条目。批量作业通过轮询 `job.result()` 等待完成,无须显式关闭会话.
## 实践要点

1. 长文件用批量转写,服务端异步处理不受客户端连接时长限制
2. 指定 `locale` 提升识别准确率,避免语言误判
3. `content_urls` 须为可公开访问或带 SAS 的 HTTPS URL
4. 转写完成后取回结果,异常路径注意释放连接
5. 作业名 `name` 建议含日期或业务标识,便于在门户中检索与归档
6. 多段音频分多次提交作业,单作业 `content_urls` 控制在合理数量便于结果聚合

## 依赖

- Python 3.8 及以上,`azure-ai-transcription` 包(通过 pip 安装)
- 已部署的 Azure AI 资源,获得 endpoint 与 key
- 批量转写的音频须可通过 HTTPS 公开访问或附 SAS 令牌,纯本地文件须先上传

## 适用场景

### 会议录音批量转写
将会议录音上传至 Blob 存储并生成 SAS URL,提交批量转写作业并指定 `locale`,异步等待完成后取回完整会议文稿。适合长会议、离线归档、会议纪要生成.
### 指定语言提升准确率
对中英文等不同语言音频指定对应 `locale`(如 `zh-CN`、`en-US`),避免语言误判,提升专有名词与口音的识别准确率.
## 案例

### 批量转写会议录音
用户有一段会议录音 `meeting.wav` 已上传至 Blob 并得到 SAS URL。先配置环境变量 `TRANSCRIPTION_ENDPOINT` 与 `TRANSCRIPTION_KEY`,实例化 `TranscriptionClient`。调用 `begin_transcription(name="meeting-20260406", locale="zh-CN", content_urls=["https://<storage>/meeting.wav?<sas>"])`。`job.result()` 阻塞等待,完成后从 `result` 取回完整文稿并导出为会议纪要.
### 指定语言转写英文音频
用户有一段英文播客 `podcast.wav`,不指定语言时识别准确率低。批量提交 `begin_transcription(locale="en-US", content_urls=[...])`,指定 `en-US` 后专有名词识别准确率明显提升,取回结果后导出文本.
## 异常处理

### TRANSCRIPTION_ENDPOINT 未设置
实例化 `TranscriptionClient` 时 `os.environ["TRANSCRIPTION_ENDPOINT"]` 抛 `KeyError`。检查环境变量是否已导出(常见为 `https://<resource>.cognitiveservices.azure.com`),在 shell 或 `.env` 中配置后检查网络连接和配置后重试。不要把 endpoint 硬编码进源码.
### TRANSCRIPTION_KEY 无效(401/403)
调用转写接口返回 401 或 403。核对 `TRANSCRIPTION_KEY` 是否为该资源的有效订阅密钥,确认 endpoint 与 key 属于同一资源同一区域。密钥轮换后旧 key 会失效,需更新环境变量.
### DefaultAzureCredential 不被支持
尝试用 `DefaultAzureCredential` 认证时报错。此客户端仅支持订阅密钥认证,改用 `credential=os.environ["TRANSCRIPTION_KEY"]` 传入订阅密钥.
### content_urls 不可访问
批量转写作业提交后长时间不返回或返回失败。确认 `content_urls` 指向的 URL 可被服务端公开访问或附带了未过期的 SAS 令牌;Blob 容器若为私有须生成只读 SAS;URL 协议须为 HTTPS.
### locale 不被支持
指定 `locale` 后识别准确率低或报错语言不支持。核对 locale 是否在 Azure AI Speech 支持的语言列表内(如 `en-US`、`zh-CN`、`ja-JP`).
## 常见问题

### Q1:如何认证?
此客户端仅支持订阅密钥认证,通过 `TRANSCRIPTION_ENDPOINT` 与 `TRANSCRIPTION_KEY` 环境变量配置资源,实例化时传入 `credential=os.environ["TRANSCRIPTION_KEY"]`。不支持 `DefaultAzureCredential`.
### Q2:locale 怎么填?
填 BCP-47 语言标签,如 `en-US`、`zh-CN`、`ja-JP`。指定与音频一致的语言可显著提升识别准确率,避免语言误判.
### Q3:长文件怎么处理?
长文件优先用批量转写并存储在 Blob 中,服务端异步处理不受客户端连接时长限制;`job.result()` 阻塞等待完成.
### Q4:content_urls 有什么要求?
须为可被服务端公开访问或带 SAS 令牌的 HTTPS URL;Blob 容器若为私有须生成只读 SAS;URL 协议须为 HTTPS.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接和配置后重试；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖云服务,需要网络连接,断网时无法转写
- 仅支持订阅密钥认证,不支持 DefaultAzureCredential、托管标识等
- 批量转写要求音频可通过公开 URL 或 SAS 访问,纯本地文件须先上传
- 本基础版不含实时流式转写、说话人分离、时间戳字幕生成等高级能力
- 识别准确率受音频质量、背景噪声、口音与 locale 匹配度影响

## 升级提示

本基础版仅覆盖批量转写与语言指定。如需实时流式转写(`begin_stream_transcription` 与 `send_audio_file`)、说话人分离(`diarization_enabled`)、时间戳捕获与字幕生成、流式背压处理与会话管理实践要点,请升级至付费版 `azure-ai-transcription-py`.
## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "Azure语音转文字基础版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "azure-ai-transcription-py"
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
