---
name: spark-media
description: "使用场景: 用户明确希望通过 AI Skills 平台 API 生成或编辑图片、生成视频或查询媒体任务时。"
license: MIT-0
metadata:
    {
        "packageVersion": "2.7.0",
        "openclaw": {
            "emoji": "✨",
            "homepage": "https://ai-skills.open-idea.net",
            "primaryEnv": "SPARK_MEDIA_API_KEY",
            "envVars": [
                {
                    "name": "AI_SKILLS_API_KEY",
                    "required": false,
                    "description": "通用平台 Key；与产品专用变量任选其一。"
                },
                {
                    "name": "SPARK_MEDIA_API_KEY",
                    "required": false,
                    "description": "兼容产品专用 Key；设置时优先使用。"
                }
            ]
        }
    }
---

# Spark 媒体

## Skill 简介

Spark Media 用于根据文字生成图片和视频、基于参考图进行图片或视频创作，并查询媒体任务进度与结果，适合广告图、商品图、海报和短视频素材制作。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

当前控制台直接创建通用 Key，无需选择产品；每个账号最多保留一把未撤销的通用 Key，已有时直接复制复用，更换时先撤销旧 Key。下列产品选择说明适用于旧版控制台。

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.AI_SKILLS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

推荐创建账号通用 Key，以上全局变量只需配置一次即可供各 Skill 使用；仍需在产品管理中开通目标产品。原有产品专用 Key 仅能调用对应产品。

兼容旧配置：如需隔离本产品，可改用 `openclaw config set env.SPARK_MEDIA_API_KEY "你的平台APIKey"`，然后重启 Gateway。调用时优先读取 `SPARK_MEDIA_API_KEY`，为空时读取 `AI_SKILLS_API_KEY`；两者均缺失时停止调用并引导创建密钥。不要输出、记录或要求用户在对话中粘贴完整密钥。


## 完成标准

- 在用户已授权范围内完成请求；收到异步任务时持续轮询任务状态，按 HTTP-REQUESTS.md 的终态与等待上限停止。未规定上限时，开始轮询前设定有限等待预算；超时保留任务 ID、最后状态与查询方式，不宣称成功或失败、不重复提交。
- 429/503 等可恢复错误按参考规则有限退避；同一逻辑请求复用原 `Idempotency-Key` 和相同输入。结果不确定或规则要求人工核对时停止自动重试；已授权范围内的安全续查无需重复确认。
- 多文件或多步骤任务完成后逐项交付结果；部分失败、仍在处理或等待人工核对的项目分别说明，并给出下一步。

## 参考资料

按当前任务读取对应资料；无需预读全部文档。

- 首次配置或排查鉴权时：[API 密钥配置](https://ai-skills.open-idea.net/skill-docs/spark-media/API-KEY.md)
- 生成或编辑图片时：[图片生成与编辑](https://ai-skills.open-idea.net/skill-docs/spark-media/IMAGE-GENERATION.md)
- 生成视频或查询视频任务时：[视频生成与轮询](https://ai-skills.open-idea.net/skill-docs/spark-media/VIDEO-GENERATION.md)
- 调用 API 前，确认请求、响应与重试规则：[HTTP 请求示例](https://ai-skills.open-idea.net/skill-docs/spark-media/HTTP-REQUESTS.md)
- 执行前，确认本次授权、安全与结果解释边界：[行为、错误与重试规则](https://ai-skills.open-idea.net/skill-docs/spark-media/BEHAVIOR-RULES.md)
