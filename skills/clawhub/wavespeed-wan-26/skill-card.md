## Description:

Generate videos using Alibaba's Wan 2.6 model via WaveSpeed AI. Supports text-to-video and image-to-video generation with up to 15 seconds duration at 720p or 1080p. Features audio-guided generation, prompt expansion, multi-shot mode, and configurable seeds. Use when the user wants to create videos from text prompts or animate images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate short videos from text prompts or animate source images, with optional audio guidance, multi-shot generation, prompt expansion, and seed controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source images or audio submitted for generation are uploaded to WaveSpeed.

Mitigation: Submit only media the user intends to upload to WaveSpeed.

Risk: Video generation requests incur usage charges.

Mitigation: Check the estimated generation cost before submitting a request.

Risk: The WaveSpeed login stores an API credential for later use.

Mitigation: Keep API keys out of chat and use the documented WaveSpeed login flow.

## Reference(s):

- [WaveSpeed Wan 2.6 skill release](https://clawhub.ai/wavespeed/skills/wavespeed-wan-26)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Video, Shell commands, Guidance]

**Output Format:** [Generated video files or hosted video URLs; Markdown instructions with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Videos can be 5, 10, or 15 seconds long at supported 720p or 1080p settings.]

## Skill Version(s):

2.1.1 (source: server-resolved release metadata; artifact frontmatter lists 2.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
