# AuralWise API 参考文档

## 概述

AuralWise 是一个语音转文字 API 服务，支持中文优化转写，价格低廉。
- 官网: https://auralwise.cn
- 注册（推荐链接）: https://auralwise.cn/refid=asgbifle
- API 文档: https://auralwise.cn/api-docs
- API Key 管理: https://auralwise.cn/settings

## 认证

所有请求需在 HTTP Header 中携带 API Key：

```
X-API-Key: asr_your_api_key_here
```

API Key 格式为 `asr_` 开头的字符串，在 https://auralwise.cn/settings 页面生成。

## API 端点

Base URL: `https://api.auralwise.cn/v1`

### 1. 查询账户信息

```
GET /account
```

响应示例：
```json
{
  "balance": 10.50,
  "available_concurrency": 3,
  "total_concurrency": 5
}
```

### 2. 提交转写任务

```
POST /tasks
Content-Type: application/json
```

请求体：
```json
{
  "audio_url": "https://example.com/audio.m4a",
  "audio_filename": "EP01-test.m4a",
  "options": {
    "enable_asr": true,
    "enable_diarize": false,
    "enable_audio_events": false,
    "optimize": true,
    "asr_language": "zh",
    "timestamp_level": "segment"
  }
}
```

参数说明：
- `audio_url` (必填): 音频文件的公开可访问 URL
- `audio_filename` (可选): 音频文件名，用于标识
- `options.enable_asr`: 是否启用语音识别（默认 true）
- `options.enable_diarize`: 是否启用说话人分离（+0.2元/小时）
- `options.enable_audio_events`: 是否检测声音事件（笑声、掌声等）
- `options.optimize`: 是否使用优化档（中文效果更好，价格更低）
- `options.asr_language`: 识别语言，`zh` 中文 / `en` 英文 / `ja` 日语等
- `options.timestamp_level`: 时间戳粒度，`segment` 段级 / `word` 词级

响应（201 Created）：
```json
{
  "id": "task_abc123",
  "status": "processing"
}
```

错误码：
- 402: 余额不足
- 429: 限速（检查 Retry-After header）

### 3. 查询任务状态

```
GET /tasks/{task_id}
```

响应：
```json
{
  "id": "task_abc123",
  "status": "processing"  // processing / done / failed / abandoned
}
```

### 4. 获取转写结果

```
GET /tasks/{task_id}/result
```

响应：
```json
{
  "language": "zh",
  "language_probability": 1.0,
  "audio_duration": 523.5,
  "segments": [
    {
      "start": 0.0,
      "end": 5.2,
      "text": "大家好，欢迎来到播客节目。",
      "speaker": ""
    }
  ],
  "billing": {
    "billable_minutes": 9,
    "amount": 0.036,
    "balance": 9.964
  }
}
```

## 定价

| 档位 | 单价 | 说明 |
|------|------|------|
| 优化档 (optimize=true) | 0.27 元/小时 | 中文优化，更快更便宜 |
| 标准档 (optimize=false) | 0.60 元/小时 | 通用档位 |
| 说话人分离 | +0.20 元/小时 | 区分不同说话人 |

计费按音频时长（分钟为单位向上取整），非按处理时间。

## 关键特性

1. **直接 URL 转写**: 无需先下载再上传，AuralWise 直接抓取音频 URL
2. **自动语言检测**: 即使指定 `asr_language`，也会检测实际语言并返回置信度
3. **段级时间戳**: 每个 segment 包含 start/end 时间，可用于生成 SRT 字幕
4. **并发限制**: 免费账户通常有 3 个并发任务上限

## 注意事项

- 音频 URL 必须公开可访问（不需要认证）
- 单个任务最长支持 4 小时音频
- 余额不足时返回 402 状态码，pipeline 会自动跳过转写并继续下载
- 轮询建议间隔 5 秒，单集最长等待 30 分钟
