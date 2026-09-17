## Description:

incident.io enables an agent to read incident.io incidents, actions, severities, and statuses through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and incident response teams use this skill to search and read incident.io operational data from an OOMOL-connected account. It supports read-only incident, action, severity, and status lookup workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill grants broad oo CLI command authority through an OOMOL-connected account.

Mitigation: Restrict use to the listed read-only incident.io actions and inspect the live connector schema before constructing each payload.

Risk: The setup guidance includes remote installer commands.

Mitigation: Prefer installing the oo CLI from a verified vendor source and avoid pipe-to-shell installer execution.

## Reference(s):

- [ClawHub incident.io skill page](https://clawhub.ai/oomol/skills/oo-incident-io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [incident.io homepage](https://incident.io)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON responses from the oo CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before running an incident.io action.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
