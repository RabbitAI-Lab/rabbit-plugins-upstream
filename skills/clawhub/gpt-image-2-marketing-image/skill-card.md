## Description:

使用 GPT Image 2 按营销漏斗制作一整套 Campaign 图片，包括品牌认知KV、发布会视觉、落地页Hero、邮件头图、社交素材、线下Banner和会员沟通；通过 AI Hive 生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams and creative developers use this skill to define campaign source-of-truth inputs and generate GPT Image 2 visual assets for awareness, consideration, conversion, offline event, and retention channels through AI Hive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media passed with --image or --file are uploaded to AI Hive.

Mitigation: Only provide media and campaign details that are approved for upload to that service.

Risk: Running init stores an AI Hive API key locally.

Mitigation: Prefer environment variables for temporary use or protect the local config file and rotate the key if it may have been exposed.

Risk: Generated marketing assets can imply unsupported prices, dates, benefits, product specifications, or rights clearances.

Mitigation: Keep claims, dates, pricing, product facts, person likenesses, trademarks, and co-branding terms in the campaign source of truth and review final assets before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-marketing-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, JSON]

**Output Format:** [Markdown guidance with bash commands; generated image files and JSON task responses from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt text, optional reference images, batch size, routing mode, model parameters such as aspect ratio, task polling, and configurable output directory.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
