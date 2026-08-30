## Description:

Drive the Skills Manager CLI (`skm`) to initialize the hub, adopt unmanaged skills, list or toggle skills per AI tool, and diagnose or repair symlink sync.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiweiyeah](https://clawhub.ai/user/jiweiyeah)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when managing Skills Manager from a terminal, SSH session, CI job, or headless machine. It helps initialize the skill hub, enable or disable skills for supported AI tools, adopt unmanaged skill directories, and diagnose or repair local link issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apply commands can move local skill directories or repair links across AI tool folders.

Mitigation: Use dry-run and diagnostic commands first, review the reported changes, and run apply commands only when those local file changes are intended.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/jiweiyeah/skills/skills-manager-cli)
- [Skills Manager Website](https://skillsmanager.freeourdays.com)
- [Skills Manager GitHub Repository](https://github.com/jiweiyeah/skills-manager)
- [Skills Manager GitHub Releases](https://github.com/jiweiyeah/skills-manager/releases)
- [skm JSON contracts](references/json.md)
- [skm tool ids](references/tools.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may inspect or modify local Skills Manager configuration, skill folders, and tool links when the user chooses apply operations.]

## Skill Version(s):

2.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
