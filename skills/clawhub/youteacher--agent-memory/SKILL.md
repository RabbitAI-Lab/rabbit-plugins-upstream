---
name: agent-memory
description: "使用场景: 用户要求代理记忆、长期偏好、纠错经验、范围化检索、记忆整理、归档或删除，并希望通过 AI Skills 平台 API 执行时。"
metadata:
    {
        "packageVersion": "1.4.1",
        "openclaw":
            {
                "requires": { "env": ["AGENT_MEMORY_API_KEY"] },
                "primaryEnv": "AGENT_MEMORY_API_KEY",
            },
    }
---

# Agent Memory

## Skill 简介

Agent 记忆 Skill 用于保存和检索用户偏好、错误纠正、项目约定及可复用经验，也支持对记忆进行整理、归档和删除，让 Agent 能持续复用经过确认的上下文。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.AGENT_MEMORY_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- 鉴权与环境变量：[API-KEY.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/API-KEY.md)
- HTTP、幂等与轮询：[HTTP-REQUESTS.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/HTTP-REQUESTS.md)
- 全部字段与结果：[OPERATIONS.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/OPERATIONS.md)
- 错误、安全与交付规则：[BEHAVIOR-RULES.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/BEHAVIOR-RULES.md)
