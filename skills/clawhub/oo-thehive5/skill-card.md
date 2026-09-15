## Description:

TheHive 5 (strangebee.com). Use this skill for reading, creating, and updating TheHive 5 alerts and cases through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Security analysts, incident responders, and developers use this skill to inspect TheHive 5 action schemas, retrieve alerts and cases, and create alerts or cases through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Prefer an official package or download-and-verify installation flow before running the oo CLI.

Risk: Create actions can modify TheHive 5 alerts or cases through OOMOL-mediated access.

Mitigation: Confirm the exact action payload and expected effect with the user before executing write actions.

Risk: The skill routes TheHive 5 data through an OOMOL-connected account.

Mitigation: Install only when OOMOL-mediated access is acceptable for the user's TheHive 5 data and operational policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-thehive5)
- [TheHive 5 homepage](https://strangebee.com/thehive)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
