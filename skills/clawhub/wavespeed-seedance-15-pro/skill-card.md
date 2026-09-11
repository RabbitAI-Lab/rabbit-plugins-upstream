## Description:

Generate videos using ByteDance's Seedance V1.5 Pro model via WaveSpeed AI, supporting text-to-video and image-to-video generation with 4-12 second duration at up to 1080p, optional audio generation, camera control, smart duration, and configurable seeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to generate short videos from text prompts or animate images through WaveSpeed AI's Seedance V1.5 Pro endpoints. It helps agents provide setup guidance, parameter choices, pricing checks, and runnable WaveSpeed CLI or MCP commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npm and MCP setup commands can introduce supply-chain risk in sensitive environments.

Mitigation: Pin reviewed package versions before installation and run setup only in a restricted workspace.

Risk: WaveSpeed authentication and selected media files may expose account credentials, credits, prompts, or local assets to the external service.

Mitigation: Use the CLI login flow or environment variable handling, avoid pasting API keys into chat, and limit the workspace to media files needed for generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-seedance-15-pro)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include WaveSpeed CLI commands, MCP tool guidance, model parameters, pricing examples, and generated video output URLs.]

## Skill Version(s):

2.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
