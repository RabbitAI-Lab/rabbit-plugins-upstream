## Description:

MailboxValidator lets agents validate email addresses and check disposable or free-mail provider status through the OOMOL MailboxValidator connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents supporting customer data quality and signup workflows use this skill to validate email addresses, identify disposable inboxes, and check whether an address belongs to a free email provider.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer commands can execute code from the network during first-time setup.

Mitigation: Prefer a verified, versioned oo CLI installation method and review installer contents before running setup commands.

Risk: MailboxValidator requests use OOMOL as an intermediary and depend on a connected MailboxValidator account.

Mitigation: Install only when that intermediary model is acceptable and confirm authentication and account-connection steps yourself.

## Reference(s):

- [MailboxValidator homepage](https://www.mailboxvalidator.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailbox-validator)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON connector responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns OOMOL connector JSON responses when actions run.]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
