---
name: uyghur-ai
description: "使用场景: 用户提到维吾尔语、维文、汉维翻译、维吾尔语问答写作、DOCX/PDF 翻译或维文图片 OCR；需要 UYGHUR_AI_SKILL_API_KEY。"
metadata:
    {
        "packageVersion": "1.7.0",
        "openclaw":
            {
                "emoji": "🌙",
                "homepage": "https://ai-skills.open-idea.net",
                "primaryEnv": "UYGHUR_AI_SKILL_API_KEY",
                "requires": { "env": ["UYGHUR_AI_SKILL_API_KEY"] },
            },
    }
---

# 维吾尔语 AI

## Skill 简介

维吾尔语 AI Skill 由阿里云百炼 Qwen3.8-Max 提供模型能力，用于中文与维吾尔语双向翻译、维吾尔语问答和内容创作、Word/PDF 翻译，以及图片 OCR 原文识别与翻译。PDF 支持文字版、扫描件和混合型文档。

## 平台入口与注册

1. 打开 [AI Skills 平台](https://ai-skills.open-idea.net/)，新用户可直接进入 [注册页面](https://ai-skills.open-idea.net/register)，已有账号进入 [登录页面](https://ai-skills.open-idea.net/login)。
2. 登录后进入 [产品管理](https://ai-skills.open-idea.net/dashboard/products) 开通本 Skill，再到 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys) 创建密钥。

## Skill 安装与配置

1. 在 [API 密钥管理](https://ai-skills.open-idea.net/dashboard/keys)中选择已开通的产品，创建并复制 API 密钥。
2. 在 OpenClaw 中安装本 Skill。
3. 将复制的密钥配置到本 Skill 的 API 密钥环境变量，然后重启 Gateway：

```sh
openclaw config set env.UYGHUR_AI_SKILL_API_KEY "你的平台APIKey"
openclaw gateway restart
```

## 参考资料

- [API 密钥配置](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/API-KEY.md)
- [接口路由](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/INTERFACE-ROUTING.md)
- [文本翻译](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/TRANSLATION.md)
- [对话补全](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/CHAT-COMPLETIONS.md)
- [文档翻译](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/DOCUMENT-TRANSLATION.md)
- [图片 OCR 翻译](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/IMAGE-OCR.md)
- [HTTP 请求示例](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/HTTP-REQUESTS.md)
- [行为、错误与重试规则](https://ai-skills.open-idea.net/skill-docs/uyghur-ai/BEHAVIOR-RULES.md)
