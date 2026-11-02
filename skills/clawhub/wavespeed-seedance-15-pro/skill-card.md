## Description:

Generate videos using ByteDance's Seedance V1.5 Pro model via WaveSpeed AI. Supports text-to-video and image-to-video generation with 4-12 second duration at up to 1080p. Features audio generation, camera control, smart duration, and configurable seeds. Use when the user wants to create videos from text prompts or animate images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators can use the skill to generate short videos from text prompts or animate provided images, with optional generated audio and configurable camera behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected images are sent to WaveSpeed, and video generation uses paid credits.

Mitigation: Upload only intended media and check the estimated price before generation.

Risk: API credentials could be exposed if shared in chat.

Mitigation: Authenticate through the CLI and do not paste API keys into chat.

Risk: The CLI and MCP implementations are external to the artifact review.

Mitigation: Prefer reviewed, pinned CLI and MCP versions.

## Reference(s):

- [WaveSpeedAI MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Video, URLs, Shell commands]

**Output Format:** [Generated video file or output URL, with optional audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Text-to-video or image-to-video; 4-12 seconds; up to 1080p.]

## Skill Version(s):

2.1.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
