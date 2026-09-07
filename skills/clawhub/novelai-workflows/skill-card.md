## Description:

NovelAI creative workflows for OpenClaw: fiction context, chapter planning, image prompting, V5/V4.5 generation, img2img, inpainting, Vibe/Director tools, cost-aware execution, and secret-safe asset records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[techotaku39](https://clawhub.ai/user/techotaku39)

### License/Terms of Use:

MIT

## Use Case:

Developers and OpenClaw users use this skill to guide NovelAI-assisted fiction writing and image workflows, including story context assembly, chapter planning, prompt generation, image editing, cost checks, and safe generation records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a NovelAI token configured in the host environment.

Mitigation: Keep NOVELAI_TOKEN in host-managed secrets or environment configuration only; do not paste tokens into chat, prompts, logs, command arguments, config examples, or generation metadata.

Risk: Image operations depend on a pinned third-party NovelAI Image MCP package.

Mitigation: Review and approve the pinned novelai-image-mcp package before use, and run the MCP server with limited filesystem and network access where possible.

Risk: NovelAI image generation, editing, Vibe, Director tools, and retries can consume account credits or usage allowance.

Mitigation: Use the available subscription and cost-estimation tools before ambiguous, high-resolution, batch, or retry operations, and wait for user confirmation when costs are unclear.

Risk: The dedicated upscale route was observed returning 404 in the reference test environment.

Mitigation: Treat upscale_image as unavailable unless the active server returns an image, and describe larger-resolution img2img or local upscaling as different fallback operations.

## Reference(s):

- [OpenClaw NovelAI on ClawHub](https://clawhub.ai/techotaku39/skills/novelai-workflows)
- [OpenClaw NovelAI README](README.md)
- [OpenClaw NovelAI Quick Start](docs/QUICK-START.md)
- [OpenClaw NovelAI Full User Manual](docs/FULL-USER-MANUAL.md)
- [OpenClaw NovelAI Costs and Quotas](docs/COSTS-AND-QUOTAS.md)
- [OpenClaw NovelAI Compatibility Notes](COMPATIBILITY.md)
- [NovelAI Image MCP](https://github.com/xinvxueyuan/NovelAI-Image-MCP)
- [NovelAI Image Models](https://docs.novelai.net/en/image/models/)
- [NovelAI Text Models](https://docs.novelai.net/en/text/models/)
- [NovelAI Persistent API Token](https://docs.novelai.net/en/text/usersettings/account/)
- [OpenClaw Skills](https://docs.openclaw.ai/skills)
- [OpenClaw ClawHub Quickstart](https://docs.openclaw.ai/clawhub/quickstart)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline commands, configuration snippets, and structured generation metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local project-state files and secret-free generation records when the agent executes the documented helper workflow.]

## Skill Version(s):

0.1.1 (source: frontmatter and changelog, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
