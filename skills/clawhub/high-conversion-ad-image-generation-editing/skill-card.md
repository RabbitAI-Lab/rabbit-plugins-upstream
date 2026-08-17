## Description:

This skill helps marketing, design, and social media teams generate or edit conversion-focused advertising images from prompts and optional reference images through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, ecommerce sellers, designers, and social media operators use this skill to create product images, ad creatives, posters, campaign visuals, and social media graphics with prompt-based or reference-guided image generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive for generation or editing.

Mitigation: Use only prompts and images that are appropriate to share with AI Hive, and avoid confidential, regulated, or third-party restricted content unless approved.

Risk: The skill requires an AI Hive API key that may be stored locally.

Mitigation: Prefer environment variables or keep the local config file permission-restricted, rotate keys if exposed, and avoid committing credentials.

Risk: The skill's search wording is broader than its actual image-generation function.

Mitigation: Treat the skill as an AI Hive image generation and editing helper, and verify model availability and platform requirements before production use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/high-conversion-ad-image-generation-editing)
- [AI Hive chat](https://ai-hive.iclip.cn/chat)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands; generated assets are downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, optional reference images, batch size, model parameters, routing mode, and an output directory; --no-download returns task metadata instead of image files.]

## Skill Version(s):

1.0.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
