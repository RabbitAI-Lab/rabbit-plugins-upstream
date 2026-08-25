## Description:

Generates narrative social carousel campaign images with AI Hive Nano Banana Pro, one frame at a time, while preserving campaign continuity and requiring evidence for proof or comparison claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External social media managers, ecommerce sellers, and brand teams use this skill to produce image-series briefs and rendered assets for Instagram, Xiaohongshu, Douyin, WeChat, LinkedIn, Pinterest, TikTok Shop, and similar campaign workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images and generated prompt content provided to the render command are sent to AI Hive.

Mitigation: Use brief mode when only inspecting the prompt, and avoid passing private images unless upload to AI Hive is intended.

Risk: The AI Hive API key may be stored on the local machine.

Mitigation: Protect ~/.ai-hive/config.json, prefer environment-based secrets where appropriate, and rotate exposed keys.

Risk: Generated marketing artwork can contain inaccurate text, claims, prices, certifications, or platform disclosures.

Mitigation: Manually review final images and add or correct regulated, legal, pricing, and disclosure text during post-production before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/social-media-marketing-image-set-generation)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, files, guidance]

**Output Format:** [Plain text prompts, CLI status JSON, shell commands, and downloaded PNG image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are downloaded locally when render is used; brief mode only prints the prompt and does not upload files.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
