## Description:

为抖音电商、抖店、商品卡和直播间生成与编辑商品页演示、SKU 视频、直播讲解片段及千川投放素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, ecommerce operators, and agent users use this skill to generate and edit Douyin ecommerce product-page videos, SKU variants, livestream explanation clips, Qianchuan ad materials, and supplier-footage revisions through AI Hive video generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product images, videos, audio, and prompts are uploaded to AI Hive for processing.

Mitigation: Use the skill only when organizational policy permits that service, and avoid uploading confidential customer media or unreleased business assets unless approved.

Risk: API keys may be stored in a local configuration file under ~/.ai-hive.

Mitigation: Prefer an environment variable or scoped API key when persistent local storage is not desired, and keep any local configuration file access-restricted.

Risk: Generated ecommerce videos can contain inaccurate SKU details, claims, prices, platform UI, or promotional information if prompts or source materials are not controlled.

Mitigation: Review generated assets against the approved SKU, packaging, accessories, factual claims, and current Douyin ecommerce or advertising rules before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/douyin-ecommerce-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill can submit AI Hive video-generation tasks, poll task state, upload media, and download generated media files through its helper script.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
