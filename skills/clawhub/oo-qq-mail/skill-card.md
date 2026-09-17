## Description:

QQ Mail lets an agent operate a connected QQ Mail account through OOMOL, including reading, searching, sending, replying, forwarding, moving, marking, deleting, and downloading attachments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage a connected QQ Mail mailbox from an agent. It supports message discovery, message retrieval, attachment download, and state-changing mail workflows such as sending, replying, forwarding, moving, marking, and deleting messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote script execution for installing the required CLI.

Mitigation: Prefer a versioned package or official install path with checksum or signature verification before running the installer.

Risk: The skill can send, reply, forward, move, mark, or delete QQ Mail messages.

Mitigation: Confirm the exact target, payload, and expected effect with the user before executing any write or destructive action.

Risk: Using the skill requires connector access to a QQ Mail account.

Mitigation: Install and use the skill only when the user trusts OOMOL and is comfortable granting account access through the connector.

## Reference(s):

- [QQ Mail homepage](https://mail.qq.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub QQ Mail skill listing](https://clawhub.ai/oomol/skills/oo-qq-mail)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON; write and destructive actions require confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
