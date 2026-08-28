---
name: business-documents
description: "使用场景: 用户要求创建、读取、修改或导出报价单、收款收据、送货单等业务单据，并希望通过 AI Skills 平台 API 获得结构化结果和 PDF 时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.1.1",
        "openclaw":
            {
                "emoji": "🧾",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "BUSINESS_DOCUMENTS_API_KEY",
                "requires":
                    { "env": ["BUSINESS_DOCUMENTS_API_KEY"], "bins": ["curl"] },
                "envVars":
                    [
                        {
                            "name": "BUSINESS_DOCUMENTS_API_KEY",
                            "required": true,
                            "description": "AI Skills 平台业务单据 API Key。",
                        },
                        {
                            "name": "AI_SKILLS_API_URL",
                            "required": false,
                            "description": "可选的自托管 API 根地址；未设置时使用官方平台。",
                        },
                    ],
            },
    }
---

# Business Documents

## Skill 简介

业务单据 Skill 用于根据用户提供的交易事实创建、读取、修改和导出报价单、收款收据与送货单，并生成结构化结果和私有 PDF。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 API Key 管理中选择已开通的“业务单据”，创建并复制 API Key。
2. 在 OpenClaw 中安装 `business-documents` Skill。
3. 将 Key 配置到本 Skill 的环境变量，然后重启 Gateway：

```sh
openclaw config set env.BUSINESS_DOCUMENTS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

配置完成后，用户可以直接描述需要的单据和交易事实，例如：

- “为客户生成一份报价单，编号 QT-2026-001，包含两项服务，税率 6%。”
- “读取刚才的报价单，把第二项数量改为 3，并重新导出 PDF。”
- “根据这次收款信息生成收款收据。”

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/business-documents/API-KEY.md)
- [Operations 契约](https://ai-skills.open-idea.net/skill-docs/business-documents/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/business-documents/HTTP-REQUESTS.md)
- [行为与错误规则](https://ai-skills.open-idea.net/skill-docs/business-documents/BEHAVIOR-RULES.md)
