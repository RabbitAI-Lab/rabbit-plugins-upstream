## Description:

OpenClaw workspace initialization and standardization: creates standard workspace folders, writes WORKSPACE.md rules, adds multi-agent configuration safety guidance, and records an initialization log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill when entering a new or incomplete workspace to create the standard folder layout, persistent workspace rules, AGENTS.md startup and configuration safety guidance, and a memory log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill creates and enforces persistent workspace guidance that can influence how later agents organize files and handle shared OpenClaw configuration.

Mitigation: Install only when the user wants this workspace structure, and review the bundled WORKSPACE.md and AGENTS.md guidance before use.

## Reference(s):

- [Openclaw Workspace Initializer on ClawHub](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [dtsola ClawHub publisher profile](https://clawhub.ai/user/dtsola)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create workspace directories, WORKSPACE.md, AGENTS.md guidance, and memory log entries when executed by an agent.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
