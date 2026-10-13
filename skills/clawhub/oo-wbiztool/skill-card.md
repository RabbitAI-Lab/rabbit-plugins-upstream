## Description:

Helps agents send, schedule, track, and cancel WhatsApp messages through a connected Wbiztool account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams with a connected Wbiztool account use this skill to send or schedule WhatsApp text, image, and file messages to a number or group, check message status, and cancel queued messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests running unverified remote installer scripts on the user's machine.

Mitigation: Review the skill before installation and install the oo CLI through a verified, user-reviewed method instead of piping a remote script directly to a shell.

Risk: Sending or canceling messages can cause unintended changes.

Mitigation: Confirm the recipient, message, and effect before sending; require explicit approval of the target before cancellation.

## Reference(s):

- [Wbiztool on ClawHub](https://clawhub.ai/oomol/skills/oo-wbiztool)
- [Wbiztool](https://wbiztool.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text or Markdown with shell commands and message status results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Message sends and cancellations require user confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
