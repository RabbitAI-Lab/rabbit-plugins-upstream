## Description:

SMS Alert lets an agent operate SMS Alert through an OOMOL-connected account to send SMS or OTP messages, validate OTPs, and inspect account balances, sender IDs, and templates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage SMS Alert messaging workflows from an agent, including direct SMS delivery, OTP generation and validation, sender/template lookup, and credit balance checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes running a remote installer directly in the shell.

Mitigation: Review OOMOL's official installer or use a documented installation path with verification before running installation commands.

Risk: Write actions can send SMS or generate OTP messages and may consume SMS Alert credits.

Mitigation: Confirm exact recipients, message content, and credit impact with the user before running write actions.

Risk: The skill uses OOMOL as an intermediary for SMS Alert account access.

Mitigation: Install and use the skill only when the user accepts OOMOL-mediated access to the connected SMS Alert account.

## Reference(s):

- [ClawHub SMS Alert Skill](https://clawhub.ai/oomol/skills/oo-sms-alert)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [SMS Alert Homepage](https://www.smsalert.co.in/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for invoking SMS Alert actions through the oo CLI; connector responses are JSON.]

## Skill Version(s):

1.0.4 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
