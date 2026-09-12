## Description:

Animates characters from images using driving videos with WaveSpeed AI's Wan 2.2 Animate model, supporting animate and replace modes with 480p or 720p outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to animate an image character from a reference video or replace a video subject with an image character while preserving motion and scene.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned npm tools that can use stored WaveSpeed credentials.

Mitigation: Review before installing, prefer pinned package versions, and use scoped or revocable WaveSpeed credentials.

Risk: Image and video inputs are sent to WaveSpeed for processing and may include sensitive media.

Mitigation: Do not upload private or proprietary images or videos unless the user is comfortable sending them to WaveSpeed.

Risk: Video generation can incur usage-based costs.

Mitigation: Check pricing before runs and start with lower-resolution test runs when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-wan-22-animate)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces WaveSpeed CLI or MCP usage guidance that returns generated video output URLs or downloaded files.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
