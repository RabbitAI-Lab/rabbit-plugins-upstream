---
name: spark-media
description: "使用场景: 用户要求生成图片、编辑参考图、文生视频、图生视频、制作短视频或查询媒体任务；需要 SPARK_MEDIA_API_KEY。"
metadata:
    {
        "packageVersion": "2.4.1",
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

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.SPARK_MEDIA_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/spark-media/API-KEY.md)
- [图片生成与编辑](https://ai-skills.open-idea.net/skill-docs/spark-media/IMAGE-GENERATION.md)
- [视频生成与轮询](https://ai-skills.open-idea.net/skill-docs/spark-media/VIDEO-GENERATION.md)
- [HTTP 请求示例](https://ai-skills.open-idea.net/skill-docs/spark-media/HTTP-REQUESTS.md)
- [行为、错误与重试规则](https://ai-skills.open-idea.net/skill-docs/spark-media/BEHAVIOR-RULES.md)
