# 语音TTS · 克隆音色

> a7w 插件 `voice_tts` 的接口 `clone_voice` · 官方文档

---

## 克隆音色

### 接口地址
`POST /api/v1/apps/voice_tts/clone_voice`

### 功能说明
上传一段参考音频（或提供音频URL），系统将自动训练生成专属语音音色模型。创建成功后返回 model_id，可用于后续文字转语音调用。

### 请求方式
- **方式一**（推荐）：JSON Body 传入 `audio_url` 音频链接
- **方式二**：multipart/form-data 上传 `voices` 文件字段

### 请求参数
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| audio_url | string | 否 | 参考音频URL（与文件上传二选一），支持mp3/wav/ogg |
| title | string | 是 | 音色名称 |
| description | string | 否 | 音色描述 |
| enhance_audio_quality | boolean | 否 | 是否增强音频质量 |

### 响应示例
```json
{
  "code": 1,
  "msg": "success",
  "data": {
    "id": "model_xxxxxxxxxxxx",
    "model_id": "model_xxxxxxxxxxxx",
    "title": "我的音色",
    "type": "tts"
  }
}
```

### 注意事项
- 参考音频建议 10秒 ~ 5分钟，过短影响效果
- 音频格式支持 mp3、wav、ogg
- 创建完成后使用返回的 model_id 作为 reference_id 进行语音合成