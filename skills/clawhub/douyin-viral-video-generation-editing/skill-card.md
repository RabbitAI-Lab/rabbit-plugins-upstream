## Description:

生成与编辑抖音自然流、电商带货、商品卡和巨量千川短视频，支持文生视频、图生视频、参考视频、视频重制和延长，并通过 AI Hive 下载成片。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce operators use this skill to generate and revise Douyin short-video variants for organic posts, product demos, Qianchuan ads, and retention testing while keeping claims and calls to action tied to provided evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an AI Hive API key and may store local API configuration.

Mitigation: Use a scoped or revocable API key, keep local configuration access restricted, and rotate any key that may have been exposed.

Risk: The skill uploads user-selected media files to AI Hive and downloads generated results.

Mitigation: Upload only media that is authorized for processing and review the provider's privacy, retention, and commercial-use terms before use.

Risk: Generated marketing or product videos may include unsupported claims or conflict with platform advertising rules.

Mitigation: Review every generated asset against supplied product evidence, Douyin rules, and advertising-account policies before publishing or paid promotion.

Risk: Video generation may incur provider charges or depend on provider-side model availability.

Mitigation: Check AI Hive pricing, routing, and model availability before running batch generation or commercial campaigns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/douyin-viral-video-generation-editing)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key access](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and optional JSON task output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May download generated video or image files to the configured output directory; media uploads and generation depend on AI Hive runtime limits, pricing, and model availability.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
