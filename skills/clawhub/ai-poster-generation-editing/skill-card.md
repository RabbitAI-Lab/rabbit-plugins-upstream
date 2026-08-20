## Description:

用 AI Hive Nano Banana Pro 生成、局部修改和跨尺寸适配商业海报，先建立美术方向、主视觉、信息层级与标题/日期/CTA/二维码/法律信息留白，再完成产品发布、活动、促销、展览、招聘、直播预告与门店开业视觉。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Brand, ecommerce, and marketing teams use this skill to create, revise, and resize commercial poster art systems for product launches, events, promotions, exhibitions, recruitment, livestreams, and store openings while preserving approved facts, copy zones, and channel production constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User-specified image assets are uploaded to AI Hive and generated outputs are downloaded from presigned URLs.

Mitigation: Use only assets you are authorized to upload and review presigned upload or download destinations when strict host allowlisting is required.

Risk: The skill can save an AI Hive API key in a local user configuration file.

Mitigation: Treat the API key as a credential and keep the local configuration file restricted.

Risk: Generated poster text, prices, legal terms, recruitment conditions, QR codes, and print requirements may be inaccurate or unsuitable for final release.

Mitigation: Use generated text only as placeholders or low-risk drafts, then apply approved copy and production review before publishing or printing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/ai-poster-generation-editing)
- [AI Hive API Endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON configuration examples, API task status JSON, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated poster images are saved locally; API task status can be returned as formatted JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
