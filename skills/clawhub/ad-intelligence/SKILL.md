---
name: ad-intelligence
description: "使用场景: 用户需要搜索公开广告素材、按名称分析广告主，或基于域名生成广告投放趋势报告；需要 AD_INTELLIGENCE_API_KEY。"
metadata:
    {
        "packageVersion": "1.2.1",
        "openclaw":
            {
                "emoji": "📣",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "AD_INTELLIGENCE_API_KEY",
                "requires": { "env": ["AD_INTELLIGENCE_API_KEY"] },
            },
    }
---

# Ad Intelligence

## Skill 简介

广告情报 Skill 用于搜索公开广告素材、分析广告主投放情况，并根据域名汇总广告创意与渠道趋势，帮助你进行竞品投放复盘和创意研究。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.AD_INTELLIGENCE_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/API-KEY.md)
- [Operations 契约](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/OPERATIONS.md)
- [HTTP 请求与任务查询](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/HTTP-REQUESTS.md)
- [行为、证据与错误规则](https://ai-skills.open-idea.net/skill-docs/ad-intelligence/BEHAVIOR-RULES.md)
