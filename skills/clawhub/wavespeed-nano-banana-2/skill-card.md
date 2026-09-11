## Description:

Generate and edit images using Google's Nano Banana 2 model via WaveSpeed AI, with support for text-to-image generation, natural-language image editing, 4K outputs, flexible aspect ratios, multilingual text rendering, and camera-style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative production teams use this skill to generate images from prompts or edit user-provided images through the WaveSpeed AI hosted Nano Banana 2 model.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use of WaveSpeed AI sends prompts and uploaded images to a third-party cloud service.

Mitigation: Avoid uploading sensitive, regulated, or proprietary images unless the deployment has approval to use WaveSpeed AI for that data.

Risk: The skill depends on third-party CLI or MCP packages and local credentials.

Mitigation: Use pinned package versions or a restricted environment, and authenticate through the documented WaveSpeed login flow instead of sharing keys in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wavespeed/skills/wavespeed-nano-banana-2)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agents to return WaveSpeed CLI or MCP commands, model parameters, output URLs, and saved file paths when available.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter lists 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
