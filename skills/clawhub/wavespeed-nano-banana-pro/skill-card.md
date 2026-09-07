## Description:

Generate and edit images using Google's Nano Banana Pro model via WaveSpeed AI, including text-to-image generation, natural-language image editing, native 4K resolution, flexible aspect ratios, multilingual text rendering, and camera-style controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate images from text prompts or edit existing images through WaveSpeed AI. It helps agents choose model IDs, parameters, CLI commands, and MCP tool calls for Nano Banana Pro workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, image contents, and uploaded local files are sent to an external image-generation provider.

Mitigation: Use a least-privilege environment and avoid confidential or sensitive images unless WaveSpeed's data handling terms are acceptable.

Risk: The workflow depends on WaveSpeed npm-distributed CLI or MCP tooling and stored credentials.

Mitigation: Verify the package source, use `wavespeed login` and `wavespeed status` for authentication, and avoid pasting API keys into chat.

Risk: Passing untrusted media URLs or unsupported parameters can create privacy, security, or reliability issues.

Mitigation: Only pass media URLs provided by the user or returned by prior WaveSpeed runs, prefix local uploads with `@`, and use documented parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-nano-banana-pro)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)
- [WaveSpeed access key page](https://wavespeed.ai/accesskey)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, model IDs, parameter tables, and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead the agent to invoke WaveSpeed tools that return generated image URLs or downloaded image files.]

## Skill Version(s):

2.0.1 (source: server release evidence; artifact frontmatter metadata.version is 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
