## Description:

CodeRabbit helps agents operate CodeRabbit through OOMOL's oo CLI connector for reading, creating, updating, and deleting organization data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to let an agent inspect CodeRabbit action schemas, run CodeRabbit connector actions, retrieve review metrics and audit logs, and manage organization roles, users, seats, and custom roles with confirmation for write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact CodeRabbit administration actions can change roles, seats, custom roles, or seat assignment modes.

Mitigation: Confirm the exact payload, target users or roles, and expected effect before running actions marked write or destructive.

Risk: The first-time setup path includes remote shell or PowerShell installation commands for the oo CLI.

Mitigation: Run the installer only after verifying that cli.oomol.com is an approved source for the environment.

Risk: The skill operates CodeRabbit through an OOMOL-connected account with server-side credential handling.

Mitigation: Install only when OOMOL is trusted to broker the connection and review proposed organization changes before execution.

## Reference(s):

- [ClawHub CodeRabbit skill](https://clawhub.ai/oomol/skills/oo-coderabbit)
- [CodeRabbit homepage](https://www.coderabbit.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown instructions with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions inspect live connector schemas before payload construction; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
