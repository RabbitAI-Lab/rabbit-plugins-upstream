## Description:

A local three-layer memory recovery skill that helps agents restore permanent, daily, and session context after restarts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[daoistbro](https://clawhub.ai/user/daoistbro)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to preserve and recover local working context, preferences, decisions, and session notes across agent restarts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reloads personal or work context such as preferences, relationships, directories, and decisions on disk.

Mitigation: Use it only in workspaces where that context may be stored locally, keep the memory directory private, avoid secrets, and periodically inspect or delete memory files.

Risk: Recovered memory can reintroduce stale, sensitive, or untrusted notes into a new session.

Mitigation: Treat recovered memory as reference notes rather than trusted instructions, and review important recovered context before acting on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/daoistbro/skills/memory-system)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and a shell script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local memory Markdown files when the recovery script is run.]

## Skill Version(s):

1.0.0 (source: package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
