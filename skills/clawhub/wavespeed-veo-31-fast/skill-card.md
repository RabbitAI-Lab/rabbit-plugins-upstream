## Description:

Generate and extend videos using Google's Veo 3.1 Fast model via WaveSpeed AI. Supports text-to-video, image-to-video, and video extension. Features up to 4K resolution, audio generation, and chained extensions up to 148 seconds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate videos from text prompts or source images, extend existing Veo-generated videos, quote pricing, and save outputs through WaveSpeed AI tooling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to WaveSpeed's remote service.

Mitigation: Use only prompts and media approved for that service and confirm the destination before upload or generation.

Risk: WaveSpeed credentials may be stored by the CLI or provided through WAVESPEED_API_KEY.

Mitigation: Authenticate through the CLI where possible, avoid pasting keys into chat, and store environment credentials only in approved secret stores.

Risk: The skill relies on unpinned WaveSpeed npm tooling.

Mitigation: Prefer pinned, reviewed package versions for the CLI or MCP server and run them as a normal user.

Risk: Video generation and extension can incur per-run costs and may download files to local paths.

Mitigation: Quote pricing before runs and confirm download paths before saving generated outputs.

## Reference(s):

- [WaveSpeedAI Veo 3.1 Fast Video Generation on ClawHub](https://clawhub.ai/wavespeed/skills/wavespeed-veo-31-fast)
- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide remote video generation, media upload, pricing checks, and MP4 download workflows.]

## Skill Version(s):

2.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
