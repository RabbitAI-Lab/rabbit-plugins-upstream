## Description:

This skill lets agents inspect Encharge connector schemas and run Encharge actions through an OOMOL-connected account instead of calling the Encharge API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Encharge action schemas and run Encharge connector actions through an OOMOL-connected account, including sending transactional email after confirming the payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts for the oo CLI, which creates a local security risk if the installer source is not verified.

Mitigation: Review the oo CLI installation path before installing, prefer official package-manager or version-pinned installers with signature or checksum verification, and avoid running remote shell or PowerShell installer pipelines from an elevated session.

Risk: The send_email action changes Encharge state by sending transactional email.

Mitigation: Confirm the exact email payload and intended effect with the user before allowing the send_email action.

## Reference(s):

- [ClawHub Encharge Skill](https://clawhub.ai/oomol/skills/oo-encharge)
- [Encharge Homepage](https://encharge.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
