## Description:

Upscale videos to 720p, 1080p, 2K, or 4K resolution using WaveSpeed AI's Ultimate Video Upscaler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, video teams, developers, and agents use this skill to upscale a user-provided video URL or uploaded local video to 720p, 1080p, 2K, or 4K through WaveSpeed's hosted model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup uses unpinned npm and npx tools, which can change over time or resolve to an unexpected package.

Mitigation: Verify the package identity and publisher before installation, and prefer a pinned or isolated install for managed environments.

Risk: Upscaling sends uploaded videos or provided media URLs to WaveSpeed's hosted service.

Mitigation: Only upload videos or pass URLs that the user is comfortable sharing with WaveSpeed.

Risk: Credentials could be exposed if requested or pasted into chat.

Mitigation: Use wavespeed login or WAVESPEED_API_KEY in the execution environment, and do not ask the user to paste API keys into chat.

## Reference(s):

- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed Access Key](https://wavespeed.ai/accesskey)
- [ClawHub Skill Page](https://clawhub.ai/wavespeed/skills/wavespeed-ultimate-video-upscaler)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and guidance for WaveSpeed CLI or MCP use; model runs return an output video URL.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
