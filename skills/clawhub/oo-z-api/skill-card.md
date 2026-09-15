## Description:

Z-API (z-api.io) helps an agent inspect Z-API action schemas and operate WhatsApp messaging actions through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to check Z-API instance status and send WhatsApp text, image, and location messages through OOMOL-managed Z-API credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends executing remote installer scripts directly without verification.

Mitigation: Review setup commands before installation; prefer an official signed or checksummed oo CLI installer, or manually download and inspect the installer before execution.

Risk: Write actions can send WhatsApp text, image, or location messages to contacts or groups.

Mitigation: Confirm the exact recipient, message content, payload, and intended effect before allowing any write action.

## Reference(s):

- [Z-API homepage](https://www.z-api.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-z-api)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require confirmation of recipient, payload, and effect.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
