## Description:

Operate QQ Mail through an OOMOL-connected account for reading messages, managing mail state, downloading attachments, and sending email.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate a connected QQ Mail account, including listing folders, searching and reading messages, downloading attachments, sending mail, and confirming state-changing message actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can lead an agent to execute a remote installer script for the oo CLI.

Mitigation: Install the oo CLI manually from a trusted source and verify the installer before use.

Risk: The skill can send email and change message state, including moving or deleting messages.

Mitigation: Review the exact payload and target mailbox item before approving send, move, mark, or delete actions.

Risk: Using the connector grants access to a connected QQ Mail account through OOMOL.

Mitigation: Install only when OOMOL is trusted and the account connection scope is acceptable for the intended mailbox.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-qq-mail)
- [QQ Mail Homepage](https://mail.qq.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON when run with the --json flag.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
