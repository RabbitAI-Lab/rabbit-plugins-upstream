## Description:

WorkRally helps agents use the authenticated WorkRally CLI to create and manage AIGC comic-video workflows, including image, video, audio, music, 3D generation, prompt optimization, projects, series, shots, canvases, assets, uploads, and downloads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tencent-adm](https://clawhub.ai/user/tencent-adm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content-production agents use this skill to operate WorkRally from the command line for AIGC media creation, short-series planning, shot generation, canvas editing, and asset management. It is intended for users who have a WorkRally account and are prepared to let an agent act with their configured credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad authenticated mutation power over a WorkRally account, including deletes, uploads, downloads, canvas changes, and generic tool calls.

Mitigation: Review commands before execution, especially delete, overwrite, upload, download, and `tools call` commands; grant the agent only credentials appropriate for the task.

Risk: API keys may be stored in a persistent WorkRally config file or exposed through environment variables.

Mitigation: Store the API key only in a protected config directory or controlled environment, and use `WORKRALLY_CONFIG_DIR` for isolated or non-persistent runtimes.

Risk: Canvas overwrite and deletion commands can remove existing collaborative content.

Mitigation: Prefer incremental canvas updates and confirm overwrite or deletion requests before running them.

## Reference(s):

- [WorkRally Skill Page](https://clawhub.ai/tencent-adm/skills/workrally)
- [WorkRally Homepage](https://workrally.qq.com)
- [WorkRally API Key Setup](https://workrally.qq.com/open-api)
- [Shotlist Guide](references/shotlist-guide.md)
- [Canvas Guide](references/canvas-guide.md)
- [Upload and Assets Guide](references/upload-and-assets-guide.md)
- [AI Generation Guide](references/ai-generation-guide.md)
- [Common Pitfalls](references/common-pitfalls.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands often produce JSON when the skill recommends `-o json`; generated media and project changes are created through the authenticated WorkRally CLI.]

## Skill Version(s):

2.8.0 (source: release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
