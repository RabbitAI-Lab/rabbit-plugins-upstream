---
name: knowledge-graph
description: "使用场景: 用户要求通过平台构建知识图谱、查询实体关系或生成带来源摘要时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.7.0",
        "openclaw": {
            "emoji": "🕸️",
            "homepage": "https://ai-skills.open-idea.net",
            "primaryEnv": "KNOWLEDGE_GRAPH_API_KEY",
            "envVars": [
                {
                    "name": "AI_SKILLS_API_KEY",
                    "required": false,
                    "description": "通用平台 Key；与产品专用变量任选其一。"
                },
                {
                    "name": "KNOWLEDGE_GRAPH_API_KEY",
                    "required": false,
                    "description": "兼容产品专用 Key；设置时优先使用。"
                }
            ]
        }
    }
---

# 知识图谱

## Skill 简介

知识图谱 Skill 用于保存带来源的实体与关系，从种子实体查询有限深度的关联子图，并生成可追溯的结构化知识摘要，为 Agent 提供可查询上下文。

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

兼容旧配置：如需隔离本产品，可改用 `openclaw config set env.KNOWLEDGE_GRAPH_API_KEY "你的平台APIKey"`，然后重启 Gateway。调用时优先读取 `KNOWLEDGE_GRAPH_API_KEY`，为空时读取 `AI_SKILLS_API_KEY`；两者均缺失时停止调用并引导创建密钥。不要输出、记录或要求用户在对话中粘贴完整密钥。


## 完成标准

- 在用户已授权范围内完成请求；收到异步任务时持续轮询任务状态，按 HTTP-REQUESTS.md 的终态与等待上限停止。未规定上限时，开始轮询前设定有限等待预算；超时保留任务 ID、最后状态与查询方式，不宣称成功或失败、不重复提交。
- 429/503 等可恢复错误按参考规则有限退避；同一逻辑请求复用原 `Idempotency-Key` 和相同输入。结果不确定或规则要求人工核对时停止自动重试；已授权范围内的安全续查无需重复确认。
- 多文件或多步骤任务完成后逐项交付结果；部分失败、仍在处理或等待人工核对的项目分别说明，并给出下一步。

## 参考资料

按当前任务读取对应资料；无需预读全部文档。

- 首次配置或排查鉴权时：鉴权与环境变量：[API-KEY.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/API-KEY.md)
- 调用 API 前，确认请求、响应与重试规则：HTTP、幂等与轮询：[HTTP-REQUESTS.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/HTTP-REQUESTS.md)
- 选择当前操作后，查其字段与结果：字段、枚举与结果：[OPERATIONS.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/OPERATIONS.md)
- 执行前，确认本次授权、安全与结果解释边界：安全、来源与错误：[BEHAVIOR-RULES.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/BEHAVIOR-RULES.md)
