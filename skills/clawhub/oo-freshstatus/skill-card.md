## Description:

Freshstatus (freshworks.com) helps agents read, create, update, and delete Freshstatus status-page services and service groups through OOMOL's oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to manage Freshstatus status-page services and service groups from an agent workflow. It supports read actions directly and requires confirmation before create, update, or delete actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Verify the installer source before installation and prefer signed or checksum-verified releases.

Risk: The skill can create, update, and delete Freshstatus services and service groups.

Mitigation: Confirm the exact target, payload, and expected effect before any write or destructive action.

## Reference(s):

- [ClawHub Freshstatus Skill](https://clawhub.ai/oomol/skills/oo-freshstatus)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Freshstatus Homepage](https://www.freshworks.com/statuspage)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
