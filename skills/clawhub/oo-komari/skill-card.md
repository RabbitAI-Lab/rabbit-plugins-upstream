## Description:

Komari helps an agent manage Komari monitoring resources through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Komari clients, metrics, ping tasks, notifications, clipboard entries, sessions, settings, and audit logs. It supports read workflows and state-changing Komari actions through validated JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes an unverified remote installer executed directly in a shell.

Mitigation: Use a pinned, signed, or checksum-verified oo CLI installation path before running Komari actions.

Risk: Write and destructive Komari actions can alter configuration, revoke sessions, delete records, or remove clients.

Mitigation: Require explicit user confirmation of the exact action, target, and payload before running state-changing commands.

Risk: Remote command execution and secret-bearing responses can expose sensitive systems or credentials.

Mitigation: Confirm remote execution requests explicitly and avoid displaying or storing tokens, database DSNs, client secrets, or command output beyond the task need.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-komari)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Komari homepage](https://github.com/komari-monitor/komari)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Komari command output is expected as JSON when actions run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
