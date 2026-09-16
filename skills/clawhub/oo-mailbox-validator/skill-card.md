## Description:

MailboxValidator validates email addresses and checks whether addresses use disposable or free email providers through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to validate a single email address and check whether an address is disposable or free, using their connected MailboxValidator account through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes internet installer commands that pipe directly to a shell or use Invoke-Expression.

Mitigation: Review the oo CLI installation path before use, prefer a verified release or package manager when available, inspect the installer first, and avoid elevated privileges.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailbox-validator)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MailboxValidator Homepage](https://www.mailboxvalidator.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before running actions and returns JSON response data from the oo connector.]

## Skill Version(s):

1.0.4 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
