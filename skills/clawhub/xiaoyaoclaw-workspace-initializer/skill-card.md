## Description:

OpenClaw Workspace Initializer standardizes an agent workspace by creating expected directories, workspace rules, multi-agent configuration safety guidance, and an initialization memory log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when entering a new or incomplete OpenClaw workspace to create the standard directory layout, persistent WORKSPACE.md rules, AGENTS.md startup guidance, and initialization log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent workspace rules and AGENTS.md changes can guide future agent behavior in the workspace.

Mitigation: Review WORKSPACE.md and any AGENTS.md additions before relying on the initialized workspace.

Risk: The skill creates and standardizes workspace directories and may append an initialization memory log.

Mitigation: Run it only in workspaces where the OpenClaw directory convention is desired, and inspect generated files after execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [GitHub documentation](https://github.com/dtsola/xiaoyaoclaw-workspace-initializer)
- [Yuque guide](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [WORKSPACE.md template](artifact/templates/WORKSPACE.md)
- [AGENTS configuration safety template](artifact/templates/AGENTS-config-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and generated workspace files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces persistent workspace guidance files, optional AGENTS.md additions, standard directories, and a dated memory log.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
