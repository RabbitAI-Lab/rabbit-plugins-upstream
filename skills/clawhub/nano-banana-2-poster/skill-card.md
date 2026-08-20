## Description:

使用 Nano Banana 2 设计具有明确焦点、信息层级、文字安全区和渠道比例的海报底图或短标题海报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Designers, marketers, and agent users use this skill to plan poster hierarchy and generate poster backgrounds or short-title poster visuals with Nano Banana 2 through AI Hive. It supports event, exhibition, recruiting, product, film concept, social media, and marketplace poster workflows from text prompts or approved reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly provided reference images are sent to AI Hive for generation.

Mitigation: Use only approved images and prompts, avoid sensitive or unlicensed material, and review whether sending the content to AI Hive is acceptable for the intended workflow.

Risk: The init command can store an AI Hive API key in a local configuration file.

Mitigation: Keep the local key file protected, prefer environment-based secrets when appropriate, and rotate the key if it may have been exposed.

Risk: Generated poster text, dates, pricing, product details, identities, or venue information may be wrong or misleading.

Mitigation: Use approved source material for real-world claims and perform final human review of spelling, numbers, compliance-sensitive copy, and factual details before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-poster)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and generated image files downloaded by the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are saved locally by the helper script unless no-download mode is used; task status can also be returned as JSON.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
