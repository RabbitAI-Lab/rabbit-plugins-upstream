---
name: tibetan-ai
description: "使用场景: 用户提到藏语、藏文、汉藏翻译、中文翻译成藏语、藏语翻译成中文、藏语问答写作或 DOCX/PDF 文字层翻译；需要 TIBETAN_AI_SKILL_API_KEY。"
metadata:
    {
        "packageVersion": "1.2.0",
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

## Skill 安装与配置

1. 注册并登录 AI Skills 平台，在「产品管理」中开通藏语 AI。
2. 进入「API Key」，选择该产品，创建并复制 API Key。
3. 在 OpenClaw 中安装本 Skill。
4. 将复制的 Key 配置到本 Skill 的 API Key 环境变量，然后重启 Gateway：

```sh
openclaw config set env.TIBETAN_AI_SKILL_API_KEY "你的平台APIKey"
openclaw gateway restart
```

不要把完整 Key 发到对话中或写入代码、日志和文件名。

通过 AI Skills 平台调用藏语能力。默认 API 根地址为
`https://ai-skills.open-idea.net/api/v1`。

## 开始之前

1. 按 [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/API-KEY.md)检查专属 Key，禁止回显完整 Key。
2. 根据 [接口路由](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/INTERFACE-ROUTING.md)选择翻译、对话或文档接口。
3. 涉及文件或可能包含隐私的长文本时，先说明会上传到 AI Skills 平台并取得用户同意。
4. 所有计费写请求都携带稳定且唯一的 `Idempotency-Key`。

## 结果交付

- 普通翻译读取 `data.tgtText`。
- 对话读取 `choices[0].message.content`。
- 文档接口返回提取文本的翻译结果；本技能不改写原文件版式。
- 向用户展示业务结果，不展示完整原始响应、Key 或无必要的计费细节。
- 如需说明费用，读取 `X-AI-Skills-Billing-Currency`、
  `X-AI-Skills-Billing-Charged` 和 `X-AI-Skills-Billing-Balance`。

## 参考资料

- [API Key 配置](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/API-KEY.md)
- [接口路由](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/INTERFACE-ROUTING.md)
- [文本翻译](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/TRANSLATION.md)
- [对话补全](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/CHAT-COMPLETIONS.md)
- [文档翻译](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/DOCUMENT-TRANSLATION.md)
- [HTTP 请求示例](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/HTTP-REQUESTS.md)
- [行为、错误与重试规则](https://github.com/YouTeacher/ai-skills-platform/blob/main/openclaw/tibetan-ai/references/BEHAVIOR-RULES.md)
