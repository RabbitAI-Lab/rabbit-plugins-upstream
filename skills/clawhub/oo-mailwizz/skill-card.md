## Description:

Operate MailWizz through the OOMOL oo CLI to inspect action schemas and read or manage mailing lists and subscribers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a connected MailWizz account: list and retrieve mailing lists or subscribers, create or update subscribers, and unsubscribe subscribers with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could run arbitrary code on a user's machine.

Mitigation: Review setup steps before installation and prefer a verified or package-manager installation path for the oo CLI.

Risk: MailWizz write and unsubscribe actions can change subscriber state.

Mitigation: Allow write or unsubscribe actions only after checking the exact target, payload, and intended effect with the user.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-mailwizz)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [MailWizz Homepage](https://www.mailwizz.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
