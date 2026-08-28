---
name: seo-auditor
description: "使用场景: 用户需要研究关键词指标、审计公开网页、比较本站与竞品的关键词差距，或把带来源的发现和指标汇总为 SEO 审计报告；需要 SEO_AUDITOR_API_KEY。"
metadata:
    {
        "packageVersion": "1.2.1",
        "openclaw":
            {
                "emoji": "🔎",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "SEO_AUDITOR_API_KEY",
                "requires": { "env": ["SEO_AUDITOR_API_KEY"] },
            },
    }
---

# SEO Auditor

## Skill 简介

SEO 审计 Skill 用于研究关键词指标、审计公开网页、比较网站与竞品的关键词差距，并输出带来源的 SEO 问题清单和优化建议。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.SEO_AUDITOR_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/seo-auditor/API-KEY.md)
- [Operations 契约](https://ai-skills.open-idea.net/skill-docs/seo-auditor/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/seo-auditor/HTTP-REQUESTS.md)
- [证据、安全与错误规则](https://ai-skills.open-idea.net/skill-docs/seo-auditor/BEHAVIOR-RULES.md)
