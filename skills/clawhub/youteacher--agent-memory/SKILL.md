---
name: agent-memory
description: "使用场景: 用户要求代理记忆、长期偏好、纠错经验、范围化检索、记忆整理、归档或删除，并希望通过 AI Skills 平台 API 执行时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.5.2",
        "openclaw":
            {
                "emoji": "🧠",
                "homepage": "https://ai-skills.open-idea.net",
                "requires": { "env": ["AGENT_MEMORY_API_KEY"] },
                "primaryEnv": "AGENT_MEMORY_API_KEY",
            },
    }
---

# Agent 记忆

## Skill 简介

Agent 记忆 Skill 用于保存和检索用户偏好、错误纠正、项目约定及可复用经验，也支持对记忆进行整理、归档和删除，让 Agent 能持续复用经过确认的上下文。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.AGENT_MEMORY_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 完成标准

- 异步操作提交后持续轮询任务状态，直到成功或失败的终态再汇报；不要在 pending/processing 中途停下征求许可。
- 用户已确认的处理范围内，遇 429/503 按参考文档以原幂等键退避重试（不产生额外扣费），恢复后继续，无需再次确认。
- 一次请求涉及多个文件或多个步骤时，全部处理完再汇报；部分失败要逐项说明哪些成功、哪些失败及原因。

## 参考资料

- 鉴权与环境变量：[API-KEY.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/API-KEY.md)
- HTTP、幂等与轮询：[HTTP-REQUESTS.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/HTTP-REQUESTS.md)
- 全部字段与结果：[OPERATIONS.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/OPERATIONS.md)
- 错误、安全与交付规则：[BEHAVIOR-RULES.md](https://ai-skills.open-idea.net/skill-docs/agent-memory/BEHAVIOR-RULES.md)
