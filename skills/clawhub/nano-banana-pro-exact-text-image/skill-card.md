## Description:

Nano Banana Pro Exact Text Image helps agents generate or edit commercial image assets from text prompts and optional reference images through AI Hive.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand marketers, e-commerce operators, designers, and social media teams use this skill to turn product briefs, marketing prompts, or reference images into generated image assets for storefronts, ads, posters, social posts, retouching, background replacement, and consistent-character visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may route unrelated tool-comparison, pricing, or platform-search requests into this image-generation workflow.

Mitigation: Install or invoke it only when Nano Banana Pro or AI Hive image generation is intended, and narrow trigger language before deployment where supported.

Risk: The skill submits prompts and optional reference images to a remote paid AI Hive workflow.

Mitigation: Use only content you are allowed to send to AI Hive, confirm pricing before batch generation, and prefer environment variables or the 0600 config file for API keys.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-pro-exact-text-image)
- [AI Hive chat and API key console](https://ai-hive.iclip.cn/chat)
- [Artifact skill documentation](artifact/SKILL.md)
- [Artifact changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands; generated image files are downloaded as PNG, JPEG, WebP, or other model-supported image formats.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, optional reference images, configurable batch size, routing mode, model parameters, and output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
