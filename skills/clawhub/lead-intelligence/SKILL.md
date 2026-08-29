---
name: lead-intelligence
description: "使用场景: 用户需要按合规过滤器搜索企业或联系人、基于用户提交的可观察信号执行线索评分，或生成本地线索报告；需要 LEAD_INTELLIGENCE_API_KEY。"
metadata:
    {
        "packageVersion": "1.2.1",
        "openclaw":
            {
                "emoji": "🎯",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "LEAD_INTELLIGENCE_API_KEY",
                "requires": { "env": ["LEAD_INTELLIGENCE_API_KEY"] },
            },
    }
---

# Lead Intelligence

## Skill 简介

销售线索情报 Skill 用于按合规条件搜索企业或联系人，结合公开且可观察的信号进行线索评分，并生成带依据的本地线索研究报告。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.LEAD_INTELLIGENCE_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/API-KEY.md)
- [Operations 契约](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/OPERATIONS.md)
- [HTTP 请求与任务查询](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/HTTP-REQUESTS.md)
- [隐私、评分与错误规则](https://ai-skills.open-idea.net/skill-docs/lead-intelligence/BEHAVIOR-RULES.md)
