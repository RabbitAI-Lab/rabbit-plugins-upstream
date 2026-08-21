## Description:

OpenClaw Workspace Initializer sets up and standardizes an OpenClaw agent workspace with required directories, WORKSPACE.md rules, multi-agent configuration safety guidance, and a memory log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when entering a new or incomplete OpenClaw workspace to create standard workspace directories, persist workspace rules, add multi-agent configuration safety guidance, and record initialization activity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can add persistent workspace instructions and memory logs that affect future agent behavior.

Mitigation: Review WORKSPACE.md, AGENTS.md, and memory log changes after first use, especially in workspaces that already have local conventions.

Risk: Workspace path rules may override output paths suggested by other skills.

Mitigation: Translate output locations to the workspace convention and report any path differences to the user.

Risk: Multi-agent configuration edits can overwrite other agents' changes if applied as full replacements.

Mitigation: Use partial configuration patching for targeted changes and avoid full configuration replacement except during initialization or migration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [Project documentation](https://github.com/dtsola/openclaw-workspace-initializer)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and workspace file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates workspace directories, WORKSPACE.md, AGENTS.md startup and configuration guidance, and memory logs when executed by an agent.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
