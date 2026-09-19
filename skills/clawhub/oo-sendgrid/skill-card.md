## Description:

SendGrid helps agents inspect SendGrid account data, list transactional templates, and send transactional email through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams using ClawHub agents use this skill to operate a connected SendGrid account, inspect account and template information, and send transactional email after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded shell or PowerShell scripts.

Mitigation: Review the OOMOL CLI installation path before installation and prefer a signed or version-pinned installer with checksum verification.

Risk: The send_email action can send transactional email from the connected SendGrid account.

Mitigation: Confirm the exact recipients, message content, and SendGrid account context before allowing send_email actions.

## Reference(s):

- [ClawHub SendGrid skill page](https://clawhub.ai/oomol/skills/oo-sendgrid)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [SendGrid homepage](https://sendgrid.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live SendGrid action schemas before request construction; write actions require confirmation of recipient, content, and account context.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
