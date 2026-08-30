---
name: tibetan-ai
description: "使用场景: 用户提到藏语、藏文、汉藏翻译、中文翻译成藏语、藏语翻译成中文、藏语问答写作或 DOCX/PDF 文字层翻译；需要 TIBETAN_AI_SKILL_API_KEY。"
metadata:
    {
        "packageVersion": "1.4.1",
        "openclaw":
            {
                "emoji": "☸️",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "TIBETAN_AI_SKILL_API_KEY",
                "requires": { "env": ["TIBETAN_AI_SKILL_API_KEY"] },
            },
    }
---

# Tibetan AI

## Skill 简介

藏语 AI Skill 用于中文与藏语双向翻译、藏语问答和内容创作，以及 Word 与 PDF 文字层翻译，适合日常文本、文档处理和藏语沟通场景。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API Key 管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API Key。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.TIBETAN_AI_SKILL_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API Key 配置](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/API-KEY.md)
- [接口路由](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/INTERFACE-ROUTING.md)
- [文本翻译](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/TRANSLATION.md)
- [对话补全](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/CHAT-COMPLETIONS.md)
- [文档翻译](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/DOCUMENT-TRANSLATION.md)
- [HTTP 请求示例](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/HTTP-REQUESTS.md)
- [行为、错误与重试规则](https://ai-skills.open-idea.net/skill-docs/tibetan-ai/BEHAVIOR-RULES.md)
