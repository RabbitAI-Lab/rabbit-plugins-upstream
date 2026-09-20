## Description:

Operates OOMOL Console through the oo CLI for reading, creating, updating, and deleting account, team, billing, usage, Connection, and permission-group data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and OOMOL team administrators use this skill to inspect OOMOL account and team state and manage Console resources through the oo CLI. It supports read-only reporting as well as confirmed write and destructive administrative actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote oo CLI installer script.

Mitigation: Review the installer source before running it and install only if the user is comfortable using OOMOL's oo CLI with their OOMOL account.

Risk: Write and destructive OOMOL Console actions can change team members, Connection permissions, or related administrative state.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before execution.

Risk: Administrative Console operations may affect billing, usage visibility, or team-level access.

Mitigation: Use read-only list and get actions for inspection, and reserve state-changing actions for explicitly approved administrator workflows.

## Reference(s):

- [ClawHub OOMOL Console Skill](https://clawhub.ai/oomol/skills/oo-oomol-console)
- [OOMOL Console](https://console.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command results from oo CLI connector actions; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
