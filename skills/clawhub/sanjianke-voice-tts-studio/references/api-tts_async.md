# 语音TTS · 文字转语音（异步）

> a7w 插件 `voice_tts` 的接口 `tts_async` · 官方文档

---

## 文字转语音（异步）

### 接口地址
`POST /api/v1/apps/voice_tts/tts_async`

### 功能说明
将文本内容异步合成为语音音频文件。适合长文本，提交后立即返回 `task_id`，通过回调或轮询获取结果。

### 调用模式
**异步接口** - 提交后返回 task_id。
- 传 `callback_url`：任务完成后自动回调
- 不传 `callback_url`：通过 `GET /api/v1/tasks/{task_id}` 轮询

### 提交响应示例
```json
{
  "code": 1,
  "msg": "success",
  "data": {
    "task_id": "tsk_xxxxxxxxxxxx",
    "status": "pending",
    "app": "voice_tts",
    "api": "tts_async"
  }
}
```