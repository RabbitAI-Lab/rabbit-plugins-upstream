# 语音TTS · 文字转语音

> a7w 插件 `voice_tts` 的接口 `tts` · 官方文档

---

## 文字转语音（同步）

### 接口地址
`POST /api/v1/apps/voice_tts/tts`

### 功能说明
将文本内容同步合成为语音音频文件。请求后直接返回结果，适合短文本（建议 500 字符内）。长文本请使用异步接口 `tts_async`。

### 调用模式
**同步接口** - 请求后直接返回合成结果（含音频URL），无需轮询。

### 请求参数
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| text | string | 是 | 待合成文本，建议不超过500字符 |
| reference_id | string | 否 | 音色模型ID（克隆音色返回的 model_id） |
| model | string | 否 | 合成引擎：speech-1.5 / speech-1.5-turbo |
| format | string | 否 | 输出格式：mp3(默认)/wav/ogg/opus/pcm |
| sample_rate | integer | 否 | 采样率：8000/16000/22050/44100(默认) |
| chunk_length | integer | 否 | 分块长度，默认200 |
| normalize | boolean | 否 | 文本规范化，默认true |
| mp3_bitrate | integer | 否 | MP3比特率，默认128 |
| temperature | number | 否 | 生成温度 0~1，默认0.7 |
| top_p | number | 否 | Top-P采样 0~1，默认0.8 |

### 响应示例
```json
{
  "code": 1,
  "msg": "success",
  "data": {
    "audio_url": "https://your-domain.com/uploads/ai_app/202604/tts_xxxxxxxx.mp3",
    "format": "mp3"
  }
}
```

### 注意事项
- 同步接口适合短文本（500字符内），长文本请使用 `tts_async` 异步接口
- 未指定 reference_id 时使用系统默认音色
- 未指定 model 时使用平台配置的默认模型