# 550W Skill API 契约

仅在需要校验输入、解释计费或处理错误时读取本文件。

## Action 与接口

| Action | 接口 | 输入摘要 |
|---|---|---|
| `uploadVideo` | `/open/uploadVideo` | MP4/MOV 文件 |
| `submitTask` | `/open/submitTask` | 视频 URL、真实宽高和时长；Skill 固定全屏坐标 |
| `taskDetail` | `/open/taskDetail` | `taskId` |
| `taskList` | `/open/taskList` | `page`、`size` |
| `queryCredits` | `/open/queryCredits` | 无业务参数 |
| `removeVideoWatermark` | `/open/removeVideoWatermark` | 短视频分享链接 `videoUrl` |
| `removeImageWatermark` | `/open/removeImageWatermark` | 图片文件；`sync` 默认 `true` |
| `imageWatermarkTaskDetail` | `/open/imageWatermarkTaskDetail` | `taskId` |

所有远程请求使用 `userNo` 与 `apiKey` 鉴权。

## 输入限制

- 视频：MP4、MOV；最大 1GB；时长 1–600 秒；最大边不超过 1920，最小边不超过 1080。
- 图片：JPG、PNG、BMP、WebP、AVIF、TIFF、SVG；最大 50MB。
- URL：必须使用 HTTP 或 HTTPS，最长 2048 字符。
- `removeAudio`：boolean，默认 `false`。开启时先通过格式检测，再移除音轨；不重新编码视频流。
- 图片 `sync=false` 时返回异步任务，后续按任务编号查询。

## 状态

- 去字幕：`waiting`、`processing`、`success`、`failed`。
- 图片去水印：`processing`、`success`、`failed`、`expired`。

## 计费

- 去字幕：不高于 720P 时 `ceil(duration × 1.3)`；高于 720P 时 `ceil(duration × 1.6)`。
- 视频去水印：成功一次 1 积分。
- 图片去水印：成功一张 10 积分。
- 各能力共用账户积分余额，以接口响应为准。

## 错误码

- `200`：成功。
- `-100`：鉴权或额度不足，以 `message` 为准。
- `-200`：参数或文件不合法。
- `-300`：业务拒绝、任务不存在或服务繁忙。
- `-400`：账号受限，停止提交。
- `-500`：服务异常；不确定是否已提交时先查询，不能直接重试。
- `-600`：视频格式不支持，提示用户重新导出兼容格式。
