## Description:

Upscale images to 2K, 4K, or 8K resolution using WaveSpeed AI's Image Upscaler.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and creative production teams use this skill to upscale user-provided image URLs or local images through WaveSpeed AI into higher-resolution JPEG, PNG, or WebP outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to run unpinned WaveSpeed npm or MCP packages that can execute code locally.

Mitigation: Use a pinned reviewed package version, avoid administrator or root execution, and run the tooling in an isolated environment.

Risk: Image inputs or WaveSpeed API credentials may be sensitive.

Mitigation: Use the CLI login flow or environment variables instead of pasting keys into chat, and isolate workflows that process sensitive images or credentials.

## Reference(s):

- [WaveSpeedAI Image Upscaler on ClawHub](https://clawhub.ai/wavespeed/skills/wavespeed-image-upscaler)
- [WaveSpeed MCP Server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include WaveSpeed CLI commands, MCP tool guidance, and result URL handling.]

## Skill Version(s):

2.0.1 (source: server release metadata; artifact frontmatter says 2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
