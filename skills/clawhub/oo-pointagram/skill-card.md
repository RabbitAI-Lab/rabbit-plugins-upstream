## Description:

Uses an OOMOL-connected Pointagram account to read and manage players and teams.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Pointagram users and teams can retrieve, create, update, and remove players and teams through their connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional CLI installer downloads and executes remote code.

Mitigation: Install only if you trust OOMOL and the oo CLI distribution path; review the installer before running it.

Risk: Write and destructive actions can change or remove Pointagram player and team data.

Mitigation: Review the target and exact payload with the user before writes, and obtain explicit approval before destructive actions.

## Reference(s):

- [Pointagram homepage](https://www.pointagram.com/)
- [oo CLI integration tool](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON]

**Output Format:** [Text with shell commands and JSON action responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action requests follow the connector's live schema.]

## Skill Version(s):

1.0.0 (source: skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
