## Description:

使用 GPT Image 2 通过 AI Hive 为人物或商品替换背景，并保持主体边缘、透明细节、透视、接触阴影、反射和光线一致。

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and marketing teams use this skill to replace product and portrait image backgrounds while preserving subject identity, packaging, edges, shadows, reflections, and lighting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reference images and prompts are uploaded to AI Hive for processing.

Mitigation: Use only media intended for upload and avoid sensitive or restricted content unless approved for this service.

Risk: The skill stores or reads an AI Hive API key locally.

Mitigation: Use environment variables or the initialized config with restricted file permissions, and rotate any exposed keys.

Risk: Custom base URLs or model parameters can change where data is sent or how generation behaves.

Mitigation: Use the default AI Hive endpoint and vetted parameters unless the deployment owner has reviewed the change.

Risk: Generated background replacements can imply false use, endorsement, certification, or commercial claims.

Mitigation: Review outputs against source images, preserve original evidence for high-risk products, and disclose synthetic composition where needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/gpt-image-2-background-replace)
- [Publisher profile](https://clawhub.ai/user/wubin1836)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash command examples and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an AI Hive API key and at least one reference image for the fixed image-generation workflow.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
