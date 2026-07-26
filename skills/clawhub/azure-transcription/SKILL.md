---
slug: "azure-transcription"
name: "azure-transcription"
version: 1.0.1
displayName: "Azure语音转写专业版"
summary: "企业级语音转写工具，支持实时流式转写、说话人分离、批量处理与自定义模型。"
license: "Proprietary"
edition: "pro"
description: |-
  Azure语音转写专业版 —— 面向企业团队与专业用户的高级语音转写工具。核心能力:
  - 实时流式语音转写，支持麦克风输入与流式音频
  - 说话人分离（Diarization），自动识别不同说话人
  - 批量转写队列管理，支持大规模音频文件处理
  - 自定义语音模型集成，提升专业领域识别准确率
  - 多语言混合转写...
tags:
  - 语音识别
  - Azure
  - 企业工具
  - 实时转写
  - 说话人分离
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"

---
# Azure语音转写专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Azure语音转写专业版批量处理 | 不支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |

## 核心能力

### 1. 实时流式转写

```python
import os
from azure.ai.transcription import TranscriptionClient
# ...
client = TranscriptionClient(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    credential=os.environ["TRANSCRIPTION_KEY"]
)
# ...
# 实时流式转写
stream = client.begin_stream_transcription(locale="zh-CN")
# ...
# 发送音频文件进行实时转写
stream.send_audio_file("realtime_audio.wav")
# ...
# 接收实时转写结果
for event in stream:
    if event.is_partial:
        print(f"[实时] {event.text}", end="\r")
    else:
        print(f"[完成] {event.text}")
```- 验证返回数据的完整性和格式正确性
- 参考`批量转写队列管理`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`实时流式转写`的配置文档进行参数调优
### 2. 说话人分离（Diarization）
```python
# 启用说话人分离的批量转写
job = client.begin_transcription(
    name="meeting-with-diarization",
    locale="zh-CN",
    content_urls=["https://<storage>/meeting.wav"],
    diarization_enabled=True,
    diarization_config={
        "max_speakers": 5,
        "enabled": True
    }
)
# ...
result = job.result()
# ...
# 输出带说话人标识的转写结果
for segment in result.segments:
    speaker = segment.speaker  # 说话人标识: Speaker1, Speaker2, ...
    print(f"[{speaker}] [{segment.start_time:.1f}s-{segment.end_time:.1f}s] {segment.text}")
```

**输入**: 用户提供说话人分离（Diarization）所需的指令和必要参数.
**处理**: 解析说话人分离（Diarization）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `说话人分离（diarization）` 选项

### 3. 批量转写队列管理

```python
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from azure.ai.transcription import TranscriptionClient
# ...
class BatchTranscriptionManager:
    def __init__(self, endpoint, key, max_workers=5):
        self.client = TranscriptionClient(endpoint=endpoint, credential=key)
        self.max_workers = max_workers
        self.results = []
        self.failed = []
# ...
    def submit_transcription(self, audio_url, name, locale="zh-CN", 
                              diarization=True, callback=None):
        """提交单个转写任务"""
        try:
            job = self.client.begin_transcription(
                name=name,
                locale=locale,
                content_urls=[audio_url],
                diarization_enabled=diarization
            )
            result = job.result()
# ...
            output = {
                'name': name,
                'status': result.status,
                'transcript': result.transcript,
                'segments': result.segments if hasattr(result, 'segments') else []
            }
            self.results.append(output)
# ...
            if callback:
                callback(output)
            return output
        except Exception as e:
            self.failed.append({'name': name, 'error': str(e)})
            return None
# ...
    def batch_transcribe(self, audio_files, locale="zh-CN", diarization=True):
        """批量转写"""
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = []
            for audio in audio_files:
                future = executor.submit(
                    self.submit_transcription,
                    audio['url'], audio['name'], locale, diarization
                )
                futures.append(future)
# ...
            for future in as_completed(futures):
                future.result()
# ...
        return {'success': self.results, 'failed': self.failed}
# ...
    def export_results(self, format='srt', output_dir='./transcripts'):
        """导出转写结果"""
        os.makedirs(output_dir, exist_ok=True)
        for result in self.results:
            if format == 'srt':
                self._export_srt(result, output_dir)
            elif format == 'vtt':
                self._export_vtt(result, output_dir)
            elif format == 'json':
                self._export_json(result, output_dir)
# ...
    def _export_srt(self, result, output_dir):
        path = os.path.join(output_dir, f"{result['name']}.srt")
        with open(path, 'w', encoding='utf-8') as f:
            for i, seg in enumerate(result['segments'], 1):
                start = self._format_time(seg.start_time)
                end = self._format_time(seg.end_time)
                speaker = f"[{seg.speaker}] " if hasattr(seg, 'speaker') else ""
                f.write(f"{i}\n{start} --> {end}\n{speaker}{seg.text}\n\n")
# ...
    def _format_time(self, seconds):
        h = int(seconds // 3600)
        m = int((seconds % 3600) // 60)
        s = int(seconds % 60)
        ms = int((seconds % 1) * 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量转写队列管理` 选项

#
## 适用场景

### 场景一：企业会议实时字幕

企业会议系统实时生成字幕与会议纪要.
```python
# 会议实时字幕系统
meeting_manager = BatchTranscriptionManager(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    key=os.environ["TRANSCRIPTION_KEY"]
)
# ...
# 实时流式转写会议音频
stream = client.begin_stream_transcription(locale="zh-CN")
# ...
print("=== 会议实时字幕 ===")
for event in stream:
    if not event.is_partial:
        timestamp = event.timestamp
        print(f"[{timestamp}] {event.text}")
# ...
# 会后批量处理录音（带说话人分离）
meeting_manager.submit_transcription(
    audio_url="https://<storage>/meetings/full_meeting.wav",
    name="quarterly-review-20260118",
    locale="zh-CN",
    diarization=True
)
```

### 场景二：客服通话批量转写

客服中心批量转写通话录音，用于质检与分析.
```python
# 批量转写客服通话
manager = BatchTranscriptionManager(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    key=os.environ["TRANSCRIPTION_KEY"],
    max_workers=5
)
# ...
# 定义批量任务
call_recordings = [
    {"url": "https://<storage>/calls/call_001.wav", "name": "call_001"},
    {"url": "https://<storage>/calls/call_002.wav", "name": "call_002"},
    {"url": "https://<storage>/calls/call_003.wav", "name": "call_003"},
    {"url": "https://<storage>/calls/call_004.wav", "name": "call_004"},
    {"url": "https://<storage>/calls/call_005.wav", "name": "call_005"},
]
# ...
# 批量转写（启用说话人分离）
results = manager.batch_transcribe(call_recordings, locale="zh-CN", diarization=True)
# ...
# 导出为SRT格式
manager.export_results(format='srt', output_dir='./call_transcripts')
# ...
print(f"成功: {len(results['success'])}, 失败: {len(results['failed'])}")
```

### 场景三：多语言视频字幕批量生成

视频平台批量生成多语言字幕.
```python
# 多语言字幕生成
video_manager = BatchTranscriptionManager(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    key=os.environ["TRANSCRIPTION_KEY"],
    max_workers=3
)
# ...
# 中文视频生成中文字幕
chinese_videos = [
    {"url": "https://<storage>/videos/video_cn_01.wav", "name": "video_cn_01"},
    {"url": "https://<storage>/videos/video_cn_02.wav", "name": "video_cn_02"},
]
video_manager.batch_transcribe(chinese_videos, locale="zh-CN", diarization=False)
video_manager.export_results(format='vtt', output_dir='./subtitles/zh-CN')
# ...
# 英文视频生成英文字幕
english_videos = [
    {"url": "https://<storage>/videos/video_en_01.wav", "name": "video_en_01"},
    {"url": "https://<storage>/videos/video_en_02.wav", "name": "video_en_02"},
]
video_manager.batch_transcribe(english_videos, locale="en-US", diarization=False)
video_manager.export_results(format='vtt', output_dir='./subtitles/en-US')
```

## 使用流程

### 1. 环境准备

```bash
# 依赖说明
pip install azure-ai-transcription
# ...
# 配置环境变量
export TRANSCRIPTION_ENDPOINT="https://<resource>.cognitiveservices.azure.com"
export TRANSCRIPTION_KEY="API_KEY"
```

### 2. 实时转写

```python
import os
from azure.ai.transcription import TranscriptionClient
# ...
# 启动实时转写
stream = client.begin_stream_transcription(locale="zh-CN")
stream.send_audio_file("audio.wav")
# ...
for event in stream:
    print(event.text)
```

### 3. 批量转写

```python
manager = BatchTranscriptionManager(
    endpoint=os.environ["TRANSCRIPTION_ENDPOINT"],
    key=os.environ["TRANSCRIPTION_KEY"]
)
# ...
results = manager.batch_transcribe(
    audio_files=[{"url": "https://<storage>/audio.wav", "name": "test"}],
    locale="zh-CN",
    diarization=True
)
# ...
manager.export_results(format='srt')
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| content | string | 否 | azure-transcription处理的内容输入 |,  |
| content | string | 否 | azure-transcription处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "transcription 相关配置参数",
    result: "transcription 相关配置参数",
    result: "transcription 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

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

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| azure-ai-transcription | Python SDK | 必需 | `pip install azure-ai-transcription` |
| Azure认知服务 | 云服务 | 必需 | Azure门户创建资源 |
| concurrent.futures | Python标准库 | 必需 | Python自带 |

### API Key 配置

- `TRANSCRIPTION_ENDPOINT`：Azure认知服务端点URL
- `TRANSCRIPTION_KEY`：Azure认知服务订阅密钥
- 与免费版使用相同的认证配置，完全兼容

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业语音转写任务。支持实时流式转写、说话人分离、批量队列等企业级功能，通过Python SDK调用Azure AI服务。与免费版完全兼容，可直接复用免费版的认证配置与基础转写流程.
**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

### 转写参数配置

| 参数 | 说明 | 免费版 | 专业版 |
|:------|------:|:------|:------|
| `locale` | 语言代码 | 支持 | 支持 |
| `diarization_enabled` | 说话人分离 | 不支持 | 支持 |
| `max_speakers` | 最大说话人数 | 不支持 | 可配置 |
| `custom_model` | 自定义模型 | 不支持 | 支持 |
| `profanity_filter` | 敏感词过滤 | 不支持 | 支持 |
| `punctuation` | 标点恢复 | 不支持 | 支持 |

### 输出格式对比

| 格式 | 用途 | 特点 |
|---:|:---|---:|
| 纯文本 | 文档归档 | 最简格式 |
| SRT | 视频字幕 | 带序号与时间戳 |
| VTT | Web视频字幕 | HTML5标准 |
| JSON | 程序处理 | 含完整元数据 |

## 常见问题

### Q1：实时转写有延迟怎么办？

实时转写延迟受网络条件影响。建议使用稳定的网络连接，并适当增大音频缓冲区.
### Q2：说话人分离准确率如何提升？

确保音频质量良好，说话人间隔清晰。设置合理的max_speakers参数，避免过多或过少.
### Q3：批量转写如何处理失败任务？

专业版BatchTranscriptionManager自动记录失败任务，可通过retry_failed方法重试.
### Q4：自定义语音模型如何接入？

在Azure门户训练自定义模型后，在转写配置中指定custom_model参数即可.
### Q5：与免费版的API配置是否兼容？

完全兼容。专业版与免费版使用相同的TRANSCRIPTION_ENDPOINT和TRANSCRIPTION_KEY配置.
## 错误处理

| 错误场景2 | 原因 | 处理方式 |
|:-------:|---------|:--------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 依赖云服务，需要网络连接
