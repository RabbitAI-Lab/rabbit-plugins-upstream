## Description:

OpenClaw workspace initialization and standardization skill that sets up a standard directory structure, WORKSPACE.md rules, multi-agent configuration safety guidance, and a memory log for new or incomplete OpenClaw workspaces.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this skill to initialize or repair a workspace by creating standard folders, installing WORKSPACE.md guidance, adding multi-agent configuration safety notes to AGENTS.md when present, and recording an initialization log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent workspace guidance may conflict with existing AGENTS.md or WORKSPACE.md instructions in a workspace.

Mitigation: Install only where OpenClaw workspace rules are desired and review any AGENTS.md or WORKSPACE.md changes when the workspace already has agent instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [OpenClaw Workspace Initializer documentation](https://github.com/dtsola/openclaw-workspace-initializer)
- [WORKSPACE.md template](templates/WORKSPACE.md)
- [AGENTS config safety template](templates/AGENTS-config-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown files, inline shell commands, and concise status guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create directories, WORKSPACE.md, AGENTS.md additions when present, and memory/YYYY-MM-DD.md log entries.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
