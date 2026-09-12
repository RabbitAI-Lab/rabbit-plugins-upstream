## Description:

Generate videos from text prompts or source images using Alibaba's Wan 2.6 model through WaveSpeed AI, with configurable duration, resolution, audio guidance, prompt expansion, multi-shot mode, and seeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and external users use this skill to generate short videos from text prompts or animate user-selected images through WaveSpeed AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party WaveSpeed CLI or MCP service and may send selected prompts or media to WaveSpeed.

Mitigation: Use the skill only when that data sharing is acceptable, avoid sensitive local files unless intentional, and prefer reviewed or pinned package versions.

Risk: Video generation can incur paid usage.

Mitigation: Check pricing before running paid generations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-wan-26)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands, parameter tables, and usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides WaveSpeed CLI and MCP-oriented commands that can return generated video URLs or downloaded media files.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
