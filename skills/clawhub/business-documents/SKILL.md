---
name: business-documents
description: "使用场景: 用户要求创建、读取、修改或导出报价单、收款收据、送货单等业务单据，并希望通过 AI Skills 平台 API 获得结构化结果和 PDF 时。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.2.1",
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
                            "description": "AI Skills 平台业务单据 API 密钥。",
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

# 业务单据

## Skill 简介

业务单据 Skill 用于根据用户提供的交易事实创建、读取、修改和导出报价单、收款收据与送货单，并生成结构化结果和私有 PDF。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.BUSINESS_DOCUMENTS_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## Skill 使用

配置完成后，用户可以直接描述需要的单据和交易事实，例如：

- “为客户生成一份报价单，编号 QT-2026-001，包含两项服务，税率 6%。”
- “读取刚才的报价单，把第二项数量改为 3，并重新导出 PDF。”
- “根据这次收款信息生成收款收据。”

## 完成标准

- 异步操作提交后持续轮询任务状态，直到成功或失败的终态再汇报；不要在 pending/processing 中途停下征求许可。
- 用户已确认的处理范围内，遇 429/503 按参考文档以原幂等键退避重试（不产生额外扣费），恢复后继续，无需再次确认。
- 一次请求涉及多个文件或多个步骤时，全部处理完再汇报；部分失败要逐项说明哪些成功、哪些失败及原因。

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/business-documents/API-KEY.md)
- [操作契约](https://ai-skills.open-idea.net/skill-docs/business-documents/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/business-documents/HTTP-REQUESTS.md)
- [行为与错误规则](https://ai-skills.open-idea.net/skill-docs/business-documents/BEHAVIOR-RULES.md)
