## Description:

Creates and edits feed, social, article, podcast, course, and video cover images with Nano Banana Pro while emphasizing a single visual focus, truthful information gaps, title-safe layout, and thumbnail testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, and developers use this skill to generate or edit cover images for short videos, social posts, articles, podcasts, courses, and product review thumbnails while checking visual focus, title-safe space, authorized inputs, and promise alignment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images are sent to AI Hive for image generation.

Mitigation: Use only prompts and images that are approved for upload to that service and avoid confidential or unlicensed source material.

Risk: The initialization flow can store an API key in the user's home directory.

Mitigation: Keep the API key private, prefer environment variables when appropriate, and maintain restrictive permissions on any saved configuration file.

Risk: Generated cover imagery could imply unsupported claims, misleading comparisons, or clickbait-style promises.

Mitigation: Follow the skill's thumbnail test and prompt constraints: use authorized facts, avoid fabricated numbers or conclusions, and ensure the content actually delivers on the visual information gap.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/wubin1836/skills/viral-cover-image-generation-editing)
- [AI Hive API Endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API Key Setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with inline bash commands; the CLI can print JSON task data and save generated PNG image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed public_model_nano_banana_pro image model through AI Hive; prompts and approved reference images may be sent to the service.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
