## Description:

Generate and edit images using ByteDance's Seedream V4.5 model via WaveSpeed AI, including text-to-image generation and multi-image editing with custom resolutions up to 4096x4096.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to generate new images or edit supplied images through WaveSpeed AI when a task needs high-quality text rendering, custom image sizes, or multi-image composition.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup and MCP examples use npm or npx commands that may resolve the latest package version at install time.

Mitigation: Use trusted WaveSpeed packages, prefer pinned versions or locked project installs, and avoid elevated privileges when installing or running npm commands.

Risk: Authentication and image uploads send credentials or user media to WaveSpeed-managed services.

Mitigation: Use scoped, revocable API keys, rely on the CLI login flow instead of pasting keys into chat, and upload only images intended for WaveSpeed processing.

Risk: Passing arbitrary media URLs could expose unintended remote content to the image model workflow.

Mitigation: Only pass media URLs provided by the user or returned by a previous trusted WaveSpeed run.

## Reference(s):

- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)
- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-seedream-45)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline bash commands and model parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces WaveSpeed CLI or MCP invocation guidance that returns generated or edited image URLs and optional downloaded files.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
