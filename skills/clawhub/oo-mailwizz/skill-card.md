## Description:

MailWizz helps agents read, create, update, and unsubscribe mailing-list data through an OOMOL-connected MailWizz account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let agents manage MailWizz mailing lists and subscribers through OOMOL's oo CLI connector. It supports listing and retrieving lists or subscribers, creating or updating subscribers, and unsubscribing subscribers after explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write and unsubscribe actions can change subscriber state in MailWizz mailing lists.

Mitigation: Confirm the exact target, payload, and expected effect with the user before approving create, update, or unsubscribe actions.

Risk: The skill manages MailWizz through an OOMOL-connected account, so actions depend on the user's connected credentials and billing state.

Mitigation: Install and use the skill only when MailWizz management through OOMOL is intended, and resolve authentication, connection, or billing errors before retrying actions.

## Reference(s):

- [ClawHub MailWizz skill page](https://clawhub.ai/oomol/skills/oo-mailwizz)
- [MailWizz homepage](https://www.mailwizz.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown with inline bash and PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses JSON payloads and returns oo CLI JSON responses for connector actions.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
