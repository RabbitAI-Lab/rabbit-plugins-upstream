## Description:

Diagnoses SkillHub node connection and pairing failures for Android, iOS, and macOS companion apps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and support engineers use this skill to diagnose SkillHub node connection, pairing, configuration, network, and runtime failures across Android, iOS, and macOS companion apps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for command execution and file-writing authority without a clearly bounded command list or write scope.

Mitigation: Run it only in a tightly supervised diagnostic session, approve each command and file change, and restrict it to non-sensitive workspaces.

Risk: Connection diagnostics may involve credentials, API keys, production configuration, or logs that contain sensitive data.

Mitigation: Do not grant access to sensitive projects, credentials, or production configuration unless the publisher narrows API usage and repair behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/node-connect)
- [SkillHub skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON diagnostic results and command/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include execution logs, connection status, pairing metadata, retry outcomes, and troubleshooting recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata; SKILL.md frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
