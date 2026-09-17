## Description:

BigMailer (bigmailer.io). Use this skill for ANY BigMailer request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate BigMailer through an OOMOL-connected account, including reading, creating, updating, upserting, and deleting brands, contacts, and contact lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can run remote installer scripts directly in a shell.

Mitigation: Review the installer path before installing; prefer manually downloading the oo CLI from a trusted release source, verifying integrity, and approving setup commands yourself.

Risk: Write and destructive BigMailer actions can modify or remove contacts and contact lists.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or delete actions.

## Reference(s):

- [BigMailer Homepage](https://www.bigmailer.io/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-bigmailer)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, text]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands call the oo CLI BigMailer connector and may return JSON responses with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
