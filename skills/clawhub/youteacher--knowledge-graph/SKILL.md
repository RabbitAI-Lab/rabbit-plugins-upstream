---
name: knowledge-graph
description: "使用场景: 用户要求构建知识图谱、写入实体或关系、从单个种子实体查询子图、附加 HTTPS 来源链接或生成带来源摘要，并希望通过 AI Skills 平台 API 执行时。"
metadata:
    {
        "packageVersion": "1.4.1",
        "openclaw":
            {
                "requires": { "env": ["KNOWLEDGE_GRAPH_API_KEY"] },
                "primaryEnv": "KNOWLEDGE_GRAPH_API_KEY",
            },
    }
---

# Knowledge Graph

## Skill 简介

知识图谱 Skill 用于保存带来源的实体与关系，从种子实体查询有限深度的关联子图，并生成可追溯的结构化知识摘要，为 Agent 提供可查询上下文。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.KNOWLEDGE_GRAPH_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- 鉴权与环境变量：[API-KEY.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/API-KEY.md)
- HTTP、幂等与轮询：[HTTP-REQUESTS.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/HTTP-REQUESTS.md)
- 字段、枚举与结果：[OPERATIONS.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/OPERATIONS.md)
- 安全、来源与错误：[BEHAVIOR-RULES.md](https://ai-skills.open-idea.net/skill-docs/knowledge-graph/BEHAVIOR-RULES.md)
