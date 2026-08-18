---
name: ai-subtitle-remover
description: 使用 550W 处理视频去字幕、静音后去字幕、短视频去水印和图片去水印，并查询任务或积分。用户发送视频、图片、媒体直链或短视频分享链接并要求去字幕、去声音、去水印、查询进度或余额时使用。
metadata: { "openclaw": { "primaryEnv": "SUBTITLE_REMOVER_API_KEY" } }
---

# 550W 视频与图片处理

将用户的自然语言意图路由到确定性 Action。不要要求用户填写接口字段、宽高、时长或擦除区域。

## 首次配置

缺少凭证时，要求用户提供 550W 用户 ID 和 API-KEY，然后调用：

```json
{ "action": "configureCredentials", "params": { "userNo": "用户ID", "apiKey": "API-KEY" } }
```

也支持环境变量 `SUBTITLE_REMOVER_USER_NO`、`SUBTITLE_REMOVER_API_KEY`。获取地址：<https://qzm.550wai.cn>。不要在后续回复、日志或错误信息中复述完整 API-KEY。

## 执行方式

优先使用宿主平台注册的 Action。宿主未自动注册 Action 时，把单个 JSON 请求写入标准输入并运行：

```bash
node {baseDir}/dist/550w-skill.cjs
```

处理本地文件时可以用 `params.filePath` 传绝对路径；不要把文件内容编码进对话。每次只发送一个请求，读取标准输出的单个 JSON 响应。

## 路由规则

- 用户发送视频文件或可直接访问的视频文件 URL，并要求去字幕：调用 `workflow`。
- 用户同时要求去掉声音：在 `workflow` 中传 `removeAudio: true`；否则不传，默认保留声音。
- 用户发送短视频平台分享链接并要求无水印视频：调用 `removeVideoWatermark`，不要下载视频。
- 用户发送图片并要求擦除水印或文字：调用 `removeImageWatermark`。
- 用户询问去字幕进度：调用 `taskDetail`；询问历史任务：调用 `taskList`。
- 用户询问图片任务进度：调用 `imageWatermarkTaskDetail`。
- 用户询问余额：调用 `queryCredits`。
- 输入类型或处理意图不明确时，只询问一个必要问题，不猜测付费操作。

## 视频去字幕

本地文件：

```json
{ "action": "workflow", "params": { "file": "<视频文件>" } }
```

远程视频直链：

```json
{ "action": "workflow", "params": { "videoUrl": "https://example.com/video.mp4" } }
```

固定使用全屏擦除。不要询问、生成或传递 `x1`、`y1`、`x2`、`y2`；Skill 会在代码层强制使用全零坐标。

本地文件由上传接口返回真实元信息。远程直链缺少元信息时使用本机 `ffprobe` 预检，可通过 `FFPROBE_PATH` 指定路径。预检失败时停止，不伪造参数、不继续提交。

工作流会轮询最长 10 分钟。成功时返回 `resultUrl`；失败时返回原因；超时或连续查询失败时返回 `taskId`，不要重复提交。

## 视频去水印

```json
{ "action": "removeVideoWatermark", "params": { "videoUrl": "https://example.com/share/video" } }
```

成功时返回 `data.video`，并按实际响应展示封面或文案。不要下载、转存或再次处理返回媒体。

## 图片去水印

默认同步处理：

```json
{ "action": "removeImageWatermark", "params": { "file": "<图片文件>", "sync": true } }
```

多张图片必须逐张串行调用，不能并发扩大处理池。异步返回 `processing` 时保存 `task.taskId`，再调用：

```json
{ "action": "imageWatermarkTaskDetail", "params": { "taskId": "TASK_ID" } }
```

仅在 `task.status=success` 时提供 `task.resultUrl`；失败展示 `task.failReason`；过期则提示重新处理。

## 付费与重试约束

- 去字幕按视频时长和分辨率计费；失败任务自动退还已扣积分。
- 视频去水印成功一次扣 1 积分，失败不扣。
- 图片去水印成功一张扣 10 积分，失败不扣。
- 批量操作前先告知计费单位；除非用户已明确要求批量处理，否则不要自行扩展输入范围。
- 网络超时不能证明提交失败。发生不确定结果时优先查询已有任务，绝不无条件重试付费提交。
- 相同输入重复提交可能独立计费；不得通过重复提交“催促”任务。

## 响应要求

- 成功：说明完成的能力并提供结果链接；存在任务编号时一并返回。
- 处理中：说明当前状态和任务编号。
- 失败：展示可操作的失败原因，不泄露内部堆栈、凭证或实现信息。
- 任何结果都必须回复用户，不得返回 `NO_REPLY`。

需要字段限制、状态和错误码时读取 [API 契约](references/api-contract.md)。
