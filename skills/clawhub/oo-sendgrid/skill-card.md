## Description:

SendGrid operates a connected SendGrid account through the OOMOL oo CLI for account, scope, template, and transactional email tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect SendGrid account details, API key scopes, transactional templates, and to send transactional email through a connected SendGrid account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only from a trusted, versioned source with verification before using this skill.

Risk: The send_email action sends transactional email through SendGrid.

Mitigation: Confirm the exact email payload and intended effect with the user before execution.

## Reference(s):

- [ClawHub SendGrid Skill](https://clawhub.ai/oomol/skills/oo-sendgrid)
- [SendGrid Homepage](https://sendgrid.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SendGrid action results, live schema inspection steps, setup guidance, and confirmation prompts for email-send operations.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
