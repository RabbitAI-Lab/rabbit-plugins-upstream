## Description:

Helps an agent read Google Chat spaces and messages, identify direct-message recipients, and send plain-text messages through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and teams can use this skill to review Google Chat conversations and space membership, find existing direct messages, and send or reply to plain-text messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running a remote CLI installation script in a shell.

Mitigation: Review the installation source and script before running it, especially on machines with sensitive data.

Risk: A mistyped or unconfirmed direct-message recipient could receive a message intended for someone else.

Mitigation: Confirm the resolved recipient and exact message payload with the user before sending; do not send when the recipient cannot be confirmed.

## Reference(s):

- [Google Chat skill on ClawHub](https://clawhub.ai/oomol/skills/oo-googlechat)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Google Chat](https://workspace.google.com/products/chat/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sent Google Chat messages are plain text; cards and attachments are not supported.]

## Skill Version(s):

1.0.3 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
