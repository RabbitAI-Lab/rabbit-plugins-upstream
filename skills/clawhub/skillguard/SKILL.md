---
name: skillguard
description: "使用场景: 用户要审计第三方 Agent Skill、检查 SKILL.md、安装前安全扫描，或评估提示注入、敏感数据、危险命令与供应链风险；需要 SKILLGUARD_API_KEY。"
metadata:
    {
        "packageVersion": "1.4.1",
        "openclaw":
            {
                "emoji": "🛡️",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "SKILLGUARD_API_KEY",
                "requires": { "env": ["SKILLGUARD_API_KEY"] },
            },
    }
---

# SkillGuard

## Skill 简介

SkillGuard 用于在安装第三方 Agent Skill 前审计其 SKILL.md、脚本和参考文件，识别提示词注入、敏感数据访问、危险命令及供应链风险，并提供可解释的风险结论。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## API Key 获取与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.SKILLGUARD_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/skillguard/API-KEY.md)
- [审计工作流](https://ai-skills.open-idea.net/skill-docs/skillguard/AUDIT-WORKFLOW.md)
- [HTTP 请求与响应](https://ai-skills.open-idea.net/skill-docs/skillguard/HTTP-REQUESTS.md)
- [行为、错误与决策规则](https://ai-skills.open-idea.net/skill-docs/skillguard/BEHAVIOR-RULES.md)
