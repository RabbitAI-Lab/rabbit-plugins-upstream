---
name: uyghur-ai
description: Use when 用户提到维吾尔语、维文、汉维翻译、中文翻译成维吾尔语、维吾尔语翻译成中文、维吾尔语问答写作或 DOCX/PDF 文字层翻译；需要 UYGHUR_AI_SKILL_API_KEY。
metadata: {"packageVersion":"1.0.0","openclaw":{"emoji":"🌙","homepage":"https://ai-skills.open-idea.net","primaryEnv":"UYGHUR_AI_SKILL_API_KEY","requires":{"env":["UYGHUR_AI_SKILL_API_KEY"]}}}
---

# Uyghur AI

通过 AI Skills 平台调用维吾尔语能力。默认 API 根地址为
`https://ai-skills.open-idea.net/api/v1`，可用 `AI_SKILLS_API_URL` 覆盖站点根地址。

## 开始之前

1. 按 [API Key 配置](references/API-KEY.md)检查专属 Key，禁止回显完整 Key。
2. 根据 [接口路由](references/INTERFACE-ROUTING.md)选择翻译、对话或文档接口。
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

- [API Key 配置](references/API-KEY.md)
- [接口路由](references/INTERFACE-ROUTING.md)
- [文本翻译](references/TRANSLATION.md)
- [对话补全](references/CHAT-COMPLETIONS.md)
- [文档翻译](references/DOCUMENT-TRANSLATION.md)
- [HTTP 请求示例](references/HTTP-REQUESTS.md)
- [行为、错误与重试规则](references/BEHAVIOR-RULES.md)
