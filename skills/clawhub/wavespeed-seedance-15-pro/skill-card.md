## Description:

Generate text-to-video and image-to-video clips with ByteDance's Seedance V1.5 Pro model through WaveSpeed AI, including duration, resolution, audio, camera, and seed controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to generate videos from prompts or animate user-provided images through WaveSpeed AI. It helps configure model endpoints, media inputs, duration, resolution, audio, camera movement, and seeds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running WaveSpeed npm packages introduces ordinary third-party package supply-chain risk.

Mitigation: Install only if you trust the WaveSpeed packages and account workflow; prefer a pinned or locally managed package version and run commands as an unprivileged user.

Risk: Media uploaded through the skill is sent to WaveSpeed for video generation.

Mitigation: Upload only media that the user intends to send to WaveSpeed, and pass only media URLs supplied by the user or returned by a prior WaveSpeed run.

Risk: API credentials could be exposed if pasted into chat or command text.

Mitigation: Use the WaveSpeed login flow or the WAVESPEED_API_KEY environment variable; do not ask users to paste API keys into chat.

Risk: Unsupported or malformed model parameters can cause failed runs or unintended outputs.

Mitigation: Use only the documented parameters and confirm the live schema with the WaveSpeed CLI or MCP tools when unsure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-seedance-15-pro)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key setup](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and model parameter tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WaveSpeed CLI commands, MCP run_model input guidance, generated media URLs, and optional downloaded video file paths.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
