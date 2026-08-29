---
name: investment-research
description: "使用场景: 用户需要检索公司公告或 XBRL 事实，并基于平台内真实来源任务生成带引用、无投资指令的风险分析或投资研究报告；需要 INVESTMENT_RESEARCH_API_KEY。"
metadata:
    {
        "packageVersion": "1.4.1",
        "openclaw":
            {
                "emoji": "📊",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "INVESTMENT_RESEARCH_API_KEY",
                "requires": { "env": ["INVESTMENT_RESEARCH_API_KEY"] },
            },
    }
---

# Investment Research

## Skill 简介

投资研究 Skill 用于检索公司公告和公开披露事实，提取可核验信息，并生成带来源、时间和风险说明的研究报告；它不提供投资指令。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.INVESTMENT_RESEARCH_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/investment-research/API-KEY.md)
- [Operations 契约](https://ai-skills.open-idea.net/skill-docs/investment-research/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/investment-research/HTTP-REQUESTS.md)
- [来源、证据与投资安全规则](https://ai-skills.open-idea.net/skill-docs/investment-research/BEHAVIOR-RULES.md)
