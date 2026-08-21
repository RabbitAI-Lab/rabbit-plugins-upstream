## Description:

Turns product images, selling points, target region, audience, language, and duration into three localized e-commerce talking-head video concepts, then generates a product-sale MP4 after the user selects a concept.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and agent workflows use this skill to create localized cross-border e-commerce talking-head sale videos from product images and selling points. The skill supports a two-stage workflow where the agent presents three structured concepts before generating the final video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkFox product images, prompts, generated media, API keys, and account, SMS, or billing flows.

Mitigation: Review before installing and use only when you trust LinkFox with those inputs, credentials, and account flows.

Risk: Endpoint override variables can send LinkFox requests to another destination.

Mitigation: Avoid setting LINKFOX_* endpoint override variables unless you fully control the destination.

Risk: The skill includes mandatory region-to-race prompt rules.

Mitigation: Review those prompt rules before production use and confirm they meet applicable policy, legal, and brand requirements.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-expert-aigc-videogen-sale)
- [带货口播编排参考](artifact/references/api.md)
- [带货口播提示词](artifact/references/prompt.md)
- [linkfox-aigc-videogen-sale 编排用例](artifact/examples/test-cases.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance, structured JSON schemes, shell-command delegation, and local MP4 media path strings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The normal flow returns three candidate schemes and waits for user selection before final generation; successful generation reports local media_paths only.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
