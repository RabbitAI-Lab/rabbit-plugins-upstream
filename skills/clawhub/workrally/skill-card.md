## Description:

WorkRally CLI helps agents create AI-generated comic-drama media and manage WorkRally projects, series, scenes, storyboards, assets, uploads, downloads, infinite canvases, and related command-line workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and AI agents use this skill to operate the WorkRally CLI for AI image, video, audio, prompt-optimization, project, series, scene, asset, upload, download, and canvas workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can enable broad live edits, deletions, and arbitrary WorkRally MCP tool calls against remote workspace data.

Mitigation: Install it only for trusted agents, use a limited API key where possible, and require explicit confirmation before deletes, overwrites, bulk changes, generic tool calls, or live collaborative canvas updates.

Risk: Incorrect project or canvas identifiers can cause generation or edits in the wrong workspace area.

Mitigation: Verify project and canvas IDs before generation or edits, and prefer documented WorkRally commands over generic passthrough calls when available.

## Reference(s):

- [WorkRally Skill on ClawHub](https://clawhub.ai/tencent-adm/skills/workrally)
- [WorkRally Homepage](https://workrally.qq.com)
- [WorkRally Open API](https://workrally.qq.com/open-api)
- [AI Generation Guide](references/ai-generation-guide.md)
- [Infinite Canvas Guide](references/canvas-guide.md)
- [Common Pitfalls](references/common-pitfalls.md)
- [Shotlist Guide](references/shotlist-guide.md)
- [Upload and Assets Guide](references/upload-and-assets-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code, Markdown]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WorkRally CLI commands that create or modify remote workspace resources.]

## Skill Version(s):

2.7.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
