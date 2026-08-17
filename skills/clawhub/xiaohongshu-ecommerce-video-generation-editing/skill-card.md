## Description:

为小红书电商与品牌合作生成和编辑商品页演示、可购物笔记视频、开箱测评、蒲公英合作及聚光投放素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, creators, and brand teams use this skill to generate and revise Xiaohongshu ecommerce videos, including shoppable notes, product demos, unboxing clips, creator-collaboration edits, and ad-ready variants. The skill emphasizes accurate product facts, creator intent, disclosure space, and review against current platform and commercial-content rules before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to AI Hive for generation.

Mitigation: Only provide media and prompt content intended for AI Hive processing, and avoid unrelated private files.

Risk: Running init stores an AI Hive API key in the user's home directory.

Mitigation: Review AI Hive API key permissions before use, especially on shared machines, and keep the local configuration file restricted.

Risk: AI Hive usage may incur provider costs.

Mitigation: Confirm account, routing, and generation settings before submitting tasks.

## Reference(s):

- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)
- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/xiaohongshu-ecommerce-video-generation-editing)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [Markdown instructions with bash commands and JSON API responses; generated media files may be downloaded by the CLI.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses prompts and optional image, video, or audio inputs to submit AI Hive video generation tasks, poll task status, and download generated media.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
