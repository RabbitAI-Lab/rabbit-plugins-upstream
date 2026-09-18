---
name: investment-research
description: "使用场景: 用户需要检索公司公告或 XBRL 事实，并基于平台内真实来源任务生成带引用、无投资指令的风险分析或投资研究报告。"
license: MIT-0
metadata:
    {
        "packageVersion": "1.5.2",
        "openclaw":
            {
                "emoji": "📊",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "INVESTMENT_RESEARCH_API_KEY",
                "requires": { "env": ["INVESTMENT_RESEARCH_API_KEY"] },
            },
    }
---

# 投资研究

## Skill 简介

投资研究 Skill 用于检索公司公告和公开披露事实，提取可核验信息，并生成带来源、时间和风险说明的研究报告；它不提供投资指令。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.INVESTMENT_RESEARCH_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 完成标准

- 异步操作提交后持续轮询任务状态，直到成功或失败的终态再汇报；不要在 pending/processing 中途停下征求许可。
- 用户已确认的处理范围内，遇 429/503 按参考文档以原幂等键退避重试（不产生额外扣费），恢复后继续，无需再次确认。
- 一次请求涉及多个文件或多个步骤时，全部处理完再汇报；部分失败要逐项说明哪些成功、哪些失败及原因。

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/investment-research/API-KEY.md)
- [操作契约](https://ai-skills.open-idea.net/skill-docs/investment-research/OPERATIONS.md)
- [HTTP 请求与任务轮询](https://ai-skills.open-idea.net/skill-docs/investment-research/HTTP-REQUESTS.md)
- [来源、证据与投资安全规则](https://ai-skills.open-idea.net/skill-docs/investment-research/BEHAVIOR-RULES.md)
