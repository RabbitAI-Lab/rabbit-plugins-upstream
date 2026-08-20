## Description:

Uses Nano Banana 2 through AI Hive to create livestream commerce image assets such as preview covers, live-room backgrounds, product explanation cards, promotion placeholders, and replay covers with safe areas for live UI and host placement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce operators, and agents use this skill to plan safe-area layouts and generate reusable base images for livestream commerce workflows. Operators add approved prices, offers, inventory, timing, and platform UI outside the generated image before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected reference images are sent to AI Hive for image generation.

Mitigation: Review prompts and uploaded images for private, sensitive, or unapproved content before use.

Risk: The skill can store an AI Hive API key in a local configuration file.

Mitigation: Use a dedicated key, keep the configuration file permission-restricted, and rotate the key if it may have been exposed.

Risk: Generated livestream graphics can become misleading if they include unapproved prices, discounts, inventory, timing, product claims, or altered demonstration facts.

Mitigation: Keep volatile commercial details out of generated images unless approved and manually checked; add live pricing, offers, inventory, and timing through the livestream system or design tool.

Risk: Important product or message areas can be obscured by comments, captions, product cards, or low-bitrate mobile playback.

Mitigation: Test each asset against the real livestream UI, small-screen previews, and low-bitrate playback before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/nano-banana-2-livestream-image)
- [AI Hive API endpoint](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash commands; generated assets are downloaded image files when commands are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a fixed Nano Banana 2 image model and fixed AI Hive API endpoint; supports optional reference images, task lookup, API-key initialization, and local image downloads.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
