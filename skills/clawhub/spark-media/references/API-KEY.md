# API Key 配置

## 获取 API Key

1. 访问 [media.open-idea.net](https://media.open-idea.net)
2. 注册并登录账号
3. 进入「API Key」页面创建新的 Key
4. 复制 Key 并配置到 OpenClaw、图片 API 或视频 API 客户端

## 配置环境变量

```bash
SPARK_MEDIA_API_KEY=你的APIKey
```

## 同一个 Key 可用于

- OpenClaw `spark-media` Skill
- `POST /api/v1/image` 图片生成
- `POST /api/v1/image/edit` 图生图
- `POST /api/v1/video` 视频任务创建
- `POST /api/v1/video/image` 图生视频任务创建
- `GET /api/v1/video/{taskId}` 视频任务查询

## 验证 Key

### 验证图片接口

```bash
curl -X POST https://media.open-idea.net/api/v1/image \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "一只在草地上打滚的柯基",
    "width": 2048,
    "height": 2048
  }'
```

### 验证视频接口

```bash
curl -X POST https://media.open-idea.net/api/v1/video \
  -H "Authorization: Bearer <YOUR_API_KEY>" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "海边日落，镜头缓慢推进，温暖电影感",
    "duration": 5,
    "resolution": "720p",
    "ratio": "16:9"
  }'
```

返回图片结果、视频任务信息或计费 / 权限错误，即表示 Key 已生效。

## Key 管理

- 每个用户可创建多个 API Key
- 可在后台撤销不再使用的 Key
- 新注册用户赠送免费额度
- 图片与视频共用同一账号余额和同一套 Key
