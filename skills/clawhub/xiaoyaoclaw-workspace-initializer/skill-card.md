## Description:

OpenClaw workspace initialization and standardization for agents, including a standard directory structure, WORKSPACE.md rules, multi-agent configuration safety guidance, and a memory log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when entering a new or incomplete OpenClaw workspace to create standard folders, persist workspace rules, and keep shared agent configuration changes safer.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create workspace folders and persist rules that affect future agent behavior.

Mitigation: Install it only in workspaces where this standard layout and persistent guidance are desired.

Risk: AGENTS.md updates can influence startup behavior for later agents in shared workspaces.

Mitigation: Review any AGENTS.md changes after execution, especially in shared or multi-agent environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [Publisher profile](https://clawhub.ai/user/dtsola)
- [Project documentation](https://github.com/dtsola/openclaw-workspace-initializer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and workspace file guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create workspace directories, WORKSPACE.md, AGENTS.md guidance, and a memory log when executed by an agent.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
