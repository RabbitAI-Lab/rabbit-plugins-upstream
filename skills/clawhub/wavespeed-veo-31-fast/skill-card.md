## Description:

Generate and extend videos using Google's Veo 3.1 Fast model via WaveSpeed AI. Supports text-to-video, image-to-video, and video extension. Features up to 4K resolution, audio generation, and chained extensions up to 148 seconds. Use when the user wants to create videos from text or images, or extend existing Veo-generated videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos from text prompts or source images and to extend existing Veo-generated videos through WaveSpeed AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs WaveSpeed npm packages without pinned versions.

Mitigation: Pin reviewed package versions or run the tools in a restricted environment before using the skill in sensitive workflows.

Risk: The workflow authenticates with WaveSpeed, stores a local login key, uploads explicitly marked local media files, and can incur generation costs.

Mitigation: Use `wavespeed login` or managed environment credentials, review local files before prefixing them with `@`, and quote pricing before model runs when cost matters.

## Reference(s):

- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)
- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-veo-31-fast)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include WaveSpeed model IDs, CLI commands, MCP tool mapping, pricing notes, media handling constraints, and output URLs.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
