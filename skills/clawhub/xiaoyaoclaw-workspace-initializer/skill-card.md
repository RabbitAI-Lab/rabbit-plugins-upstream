## Description:

Initializes and standardizes an OpenClaw workspace by creating expected directories, adding workspace rules, adding multi-agent configuration safety guidance, and recording an initialization log.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dtsola](https://clawhub.ai/user/dtsola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external OpenClaw users use this skill when entering a new or incomplete workspace to establish standard folders, persistent WORKSPACE.md rules, AGENTS.md startup and configuration safety guidance, and a memory log.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create workspace folders and persistent guidance files.

Mitigation: Review the expected folder structure and WORKSPACE.md or AGENTS.md text before installing or running the skill.

Risk: Persistent AGENTS.md startup and configuration guidance can affect future agent behavior in the workspace.

Mitigation: Confirm the startup rule and configuration safety guidance match local conventions before making them persistent.

Risk: Chinese-language workspace rules may not match every team's preferred directory conventions or language defaults.

Mitigation: Adapt the workspace template text before use when a team needs different naming, organization, or language conventions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dtsola/skills/xiaoyaoclaw-workspace-initializer)
- [Project documentation linked by the skill](https://github.com/dtsola/xiaoyaoclaw-workspace-initializer)
- [OpenClaw guide linked by the skill](https://www.yuque.com/dtsola/igp1aa/adcicbai2zlem0bz)
- [Related memory-distill project linked by the skill](https://github.com/dtsola/xiaoyaoclaw-memory-distill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create workspace directories, write WORKSPACE.md and AGENTS.md guidance, and append a memory log when executed by an agent.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
