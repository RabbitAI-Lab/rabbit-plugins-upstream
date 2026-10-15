## Description:

Use a connected Gmail account to read and search messages, manage drafts and mailbox organization, send email, and update account settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with a connected Gmail account use this skill to find and read mail, compose and send messages, organize their mailbox, and manage Gmail settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time installation instructions can run remote installer scripts on the user's machine.

Mitigation: Review the installer path and use a verified, version-pinned CLI source; do not allow an agent to run remote install scripts automatically.

Risk: Sending mail or changing labels, filters, and settings can have unintended or destructive effects.

Mitigation: Confirm the exact target and effect with the user before sending, deleting, or changing mailbox state or settings.

## Reference(s):

- [Gmail skill on ClawHub](https://clawhub.ai/oomol/skills/oo-gmail)
- [oo CLI project](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Gmail](https://workspace.google.com/gmail/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Natural-language text or Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report Gmail action results from the connected account.]

## Skill Version(s):

1.0.6 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
