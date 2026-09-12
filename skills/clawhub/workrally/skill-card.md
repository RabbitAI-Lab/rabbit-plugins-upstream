## Description:

WorkRally is an agent-facing CLI skill for AIGC comic-drama workflows, including image, video, audio, music, 3D generation, prompt optimization, project and shot management, asset handling, file transfer, and WorkRally platform operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and AI agents use this skill to drive WorkRally CLI workflows for generated media production, shot and series management, canvas operations, uploads, downloads, and asset-library tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad cloud mutations including uploads, deletes, overwrites, edits to shared canvases, and changes to account projects.

Mitigation: Require explicit user confirmation before uploads, deletes, overwrites, shared-canvas edits, or project mutations.

Risk: The skill uses WorkRally API credentials and may persist API key configuration for CLI access.

Mitigation: Use narrowly scoped, revocable API keys and prefer isolated or controlled configuration directories for credential storage.

Risk: The installation path uses an unpinned global npm package.

Mitigation: Prefer a pinned, verified CLI version or install the CLI in an isolated environment before use.

## Reference(s):

- [WorkRally Skill on ClawHub](https://clawhub.ai/tencent-adm/skills/workrally)
- [tencent-adm Publisher Profile](https://clawhub.ai/user/tencent-adm)
- [WorkRally Homepage](https://workrally.qq.com)
- [WorkRally API Key Configuration](https://workrally.qq.com/open-api)
- [WorkRally CLI README](artifact/README.md)
- [AI Generation Guide](artifact/references/ai-generation-guide.md)
- [Canvas Guide](artifact/references/canvas-guide.md)
- [Common Pitfalls](artifact/references/common-pitfalls.md)
- [Shotlist Guide](artifact/references/shotlist-guide.md)
- [Upload and Assets Guide](artifact/references/upload-and-assets-guide.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with CLI commands, JSON examples, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily produces WorkRally CLI command guidance; command output is commonly JSON, table, or text depending on CLI options.]

## Skill Version(s):

2.9.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
