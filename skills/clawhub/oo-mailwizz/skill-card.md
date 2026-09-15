## Description:

MailWizz helps agents operate MailWizz mailing lists and subscribers through OOMOL's oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect MailWizz action schemas and manage mailing lists and subscribers through an OOMOL-connected account. It supports listing and retrieving lists and subscribers, creating or updating subscribers, and unsubscribing subscribers with confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup includes remote installer commands that execute content from OOMOL endpoints directly in a shell.

Mitigation: Do not run the remote installer commands unless the OOMOL installer endpoint is trusted and the installer has been inspected or verified through a safer channel.

Risk: Write and destructive MailWizz actions can change subscriber records or unsubscribe subscribers.

Mitigation: Confirm the exact payload, target list, subscriber, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub MailWizz Skill](https://clawhub.ai/oomol/skills/oo-mailwizz)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [MailWizz Homepage](https://www.mailwizz.com)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when actions are run with the oo CLI.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
