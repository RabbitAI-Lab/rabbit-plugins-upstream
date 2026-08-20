## Description:

生成与编辑小红书种草、好物分享、开箱测评和品牌合作视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, ecommerce operators, marketers, and agents use this skill to plan, generate, edit, extend, and download Xiaohongshu-style product seeding videos from prompts and user-provided media. It emphasizes truthful product representation, observable evidence, and clear audience fit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and user-selected media are sent to AI Hive for generation and upload flows.

Mitigation: Use only prompts and media that are appropriate to share with AI Hive, and avoid private or third-party media unless sharing is intended.

Risk: The init command stores an AI Hive API key on the local machine.

Mitigation: Treat the local config as a credential, keep file permissions restricted, and rotate the key if it is exposed.

Risk: Generated Xiaohongshu-style product videos could include unsupported claims, altered product details, or misleading social proof if prompts are not reviewed.

Mitigation: Review generated clips, captions, prices, claims, and visible product details against source materials and current platform rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/xiaohongshu-viral-seeding-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON task output from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper can submit video generation tasks, upload user-selected media, poll task status, and download generated video or image files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
