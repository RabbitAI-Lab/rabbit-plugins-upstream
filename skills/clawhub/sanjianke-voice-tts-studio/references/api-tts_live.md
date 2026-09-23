# 语音TTS · 文字转语音（Live·异步）

> a7w 插件 `voice_tts` 的接口 `tts_live` · 官方文档

---

## 文字转语音（WebSocket Live · 异步）

### 接口地址
`POST /api/v1/apps/voice_tts/tts_live`

### 功能说明
使用 Fish Audio **WebSocket `wss://…/v1/tts/live`** 流式合成，适合长文本；**提交后立即返回 `task_id`**，实际合成在后台 **独立 Worker** 中执行，避免 HTTP 网关超时。

### 轮询
`GET /api/v1/tasks/{task_id}` 直至 `status` 为 `completed`，结果中 `result.audio_url` 为音频地址。

### 回调
可选 `callback_url`，与 `tts_async` 行为一致。

### Worker 部署
服务器需执行：
`php think fish_tts:worker`（常驻）或 `php think fish_tts:worker --once`（crontab 每分钟）。

### 依赖
Composer 已包含 `rybakit/msgpack`、`textalk/websocket`；服务端需能访问 `wss://api.fish.audio`。