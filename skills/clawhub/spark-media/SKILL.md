---
name: spark-media
description: "使用场景: 用户要求生成图片、编辑参考图、文生视频、图生视频、制作短视频或查询媒体任务；需要 SPARK_MEDIA_API_KEY。"
metadata:
    {
        "packageVersion": "2.2.0",
        "openclaw":
            {
                "emoji": "✨",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "SPARK_MEDIA_API_KEY",
                "requires": { "env": ["SPARK_MEDIA_API_KEY"] },
            },
    }
---

# Spark Media

## Skill 简介

Spark Media 用于根据文字生成图片和视频、基于参考图进行图片或视频创作，并查询媒体任务进度与结果，适合广告图、商品图、海报和短视频素材制作。

## API Key 获取与配置

1. 注册并登录 AI Skills 平台，在「产品管理」中开通 Spark Media。
2. 进入「API Key」，选择该产品，创建并复制 API Key。
3. 在 OpenClaw 中安装本 Skill。
4. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.SPARK_MEDIA_API_KEY "你的平台APIKey"
openclaw gateway restart
```

不要把完整 Key 发到对话中或写入代码、日志和生成文件。

统一处理文生图、图生图、文生视频和图生视频。默认 API 根地址为
`https://ai-skills.open-idea.net/api/v1`。

## 工作流程

1. 检查 [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/API-KEY.md)，不要输出完整 Key。
2. 图片任务读取 [图片生成与编辑](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/IMAGE-GENERATION.md)。
3. 视频任务读取 [视频生成与轮询](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/VIDEO-GENERATION.md)。
4. 四个创建接口均必须携带唯一 `Idempotency-Key`。
5. 用户未指定但会显著影响结果的尺寸、画幅或时长应先确认；其余参数可采用安全默认值。

## 交付规则

- 保存并返回本次响应已有的媒体结果，不为“保存”“移动”“下载”再次生成。
- 不在对话中展开完整 base64 data URL。
- 视频创建返回 HTTP 202 和 `task_id` 后持续轮询，直到成功、失败或明确超时。
- 需要展示计费时读取 `X-AI-Skills-Billing-Currency`、
  `X-AI-Skills-Billing-Charged`、`X-AI-Skills-Billing-Balance`。

## 参考资料

- [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/API-KEY.md)
- [图片生成与编辑](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/IMAGE-GENERATION.md)
- [视频生成与轮询](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/VIDEO-GENERATION.md)
- [HTTP 请求示例](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/HTTP-REQUESTS.md)
- [行为、错误与重试规则](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/spark-media/references/BEHAVIOR-RULES.md)
