## Description:

Upscale videos to 720p, 1080p, 2K, or 4K resolution using WaveSpeed AI's Ultimate Video Upscaler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and media operators use this skill to guide an agent through WaveSpeed video upscaling for user-provided video URLs or local video files uploaded through the WaveSpeed CLI. It is intended for producing higher-resolution video outputs at 720p, 1080p, 2K, or 4K.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads media to WaveSpeed for processing.

Mitigation: Upload only media the user intends to send to WaveSpeed, and avoid passing arbitrary URLs that were not supplied by the user or returned by a prior run.

Risk: The WaveSpeed CLI stores authentication locally after login.

Mitigation: Use the CLI login flow or environment variables without asking users to paste API keys into chat, and run the tools with least privilege.

Risk: Long videos and high target resolutions can incur material processing cost.

Mitigation: Quote the price before processing long videos and confirm the target resolution with the user.

Risk: Global npm installs may introduce supply-chain exposure.

Mitigation: Install only trusted WaveSpeed packages and prefer pinning reviewed package versions where the environment allows it.

## Reference(s):

- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)
- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-ultimate-video-upscaler)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of WaveSpeed CLI or MCP tools and may produce result URLs or downloaded video file paths after execution.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter reports 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
