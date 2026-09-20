## Description:

Pushover helps agents operate a Pushover account through the OOMOL connector for reading, sending, updating, and deleting Pushover data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and operators use this skill to send Pushover notifications, manage delivery groups and team users, inspect messages and app limits, and handle Open Client workflows through an OOMOL-connected Pushover account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential-revealing or credential-persisting actions may expose or store Pushover application or Team API tokens.

Mitigation: Require explicit confirmation before revealing or storing tokens, avoid logging credentials, and prefer OOMOL-connected credentials where possible.

Risk: Write or destructive actions can send notifications, change delivery groups, remove users, alter licenses, or cancel emergency retries.

Mitigation: Fetch the live action schema and confirm the exact target, payload, and expected effect before running write or destructive actions.

Risk: First-time setup includes remote oo CLI installer commands.

Mitigation: Inspect or verify the installer and prefer the documented install guide before running one-line install commands.

## Reference(s):

- [Pushover homepage](https://pushover.net)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Pushover skill page](https://clawhub.ai/oomol/skills/oo-pushover)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
