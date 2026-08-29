---
name: commerce-radar
description: "使用场景: 用户需要商品搜索与价格证据、查看商品详情、分析公开店铺，或基于关键词生成电商竞争报告；需要 COMMERCE_RADAR_API_KEY。"
metadata:
    {
        "packageVersion": "1.2.1",
        "openclaw":
            {
                "emoji": "📡",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "COMMERCE_RADAR_API_KEY",
                "requires": { "env": ["COMMERCE_RADAR_API_KEY"] },
            },
    }
---

# Commerce Radar

## Skill 简介

电商情报雷达 Skill 用于检索商品和价格、查看商品详情、分析公开店铺，并生成带来源证据的电商竞争报告，辅助选品、定价和竞店研究。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.COMMERCE_RADAR_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/commerce-radar/API-KEY.md)
- [Operations 契约](https://ai-skills.open-idea.net/skill-docs/commerce-radar/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/commerce-radar/HTTP-REQUESTS.md)
- [行为与错误规则](https://ai-skills.open-idea.net/skill-docs/commerce-radar/BEHAVIOR-RULES.md)
