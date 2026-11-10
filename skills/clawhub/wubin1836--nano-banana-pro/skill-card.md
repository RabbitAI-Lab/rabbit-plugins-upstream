## Description:

通过 AI Hive 使用 Nano Banana Pro 生成和编辑商业图片，支持文生图、图生图、多参考融合、品牌与商品一致性、广告海报、电商详情页和社媒素材。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, ecommerce teams, and developers use this skill to generate and edit commercial product, brand, advertising, marketplace listing, and social media images with reference-image consistency.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored AI Hive API keys may be kept on disk and could be sent to a custom API endpoint if the base URL is changed.

Mitigation: Use the default AI Hive endpoint unless the custom endpoint is fully trusted; protect the config file and prefer environment-scoped credentials where practical.

Risk: Reference images selected for generation or editing are uploaded to AI Hive.

Mitigation: Review image content and permissions before upload, and avoid sending sensitive, confidential, or unauthorized brand or person assets.

Risk: Generated commercial imagery can contain inaccurate text, altered logos, inconsistent products, or misleading claims.

Mitigation: Review generated text, product details, legal copy, pricing, and brand assets against approved source files before publishing.

Risk: The helper depends on an unpinned requests package.

Mitigation: Install dependencies in a virtual environment with pinned versions for managed deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro)
- [AI Hive OpenAPI endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API access page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with shell commands; generated image files and JSON task status from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload selected reference images and download generated image outputs to a local directory; requires an AI Hive API key.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
