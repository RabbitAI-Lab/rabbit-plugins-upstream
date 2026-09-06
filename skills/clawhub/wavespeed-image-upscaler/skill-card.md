## Description:

Upscales user-provided images to 2K, 4K, or 8K with WaveSpeed AI's Image Upscaler, supporting JPEG, PNG, and WebP outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and image-production teams use this skill to upscale selected images through WaveSpeed AI while controlling target resolution and output format.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images are uploaded to WaveSpeed for processing.

Mitigation: Use only images appropriate for upload to WaveSpeed and work from a least-privileged workspace containing only files needed for the task.

Risk: The skill depends on WaveSpeed CLI or MCP packages for execution.

Mitigation: Install only trusted WaveSpeed packages, pin reviewed package versions in stricter environments, and avoid elevated shells for global npm installs.

Risk: Authentication material could be exposed if requested or pasted into chat.

Mitigation: Use `wavespeed login` or `WAVESPEED_API_KEY` in the environment; do not ask users to paste API keys into chat.

## Reference(s):

- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed Access Key Setup](https://wavespeed.ai/accesskey)
- [ClawHub Skill Page](https://clawhub.ai/wavespeed/skills/wavespeed-image-upscaler)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and parameter descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to produce WaveSpeed CLI or MCP usage steps and output URLs for upscaled images.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
