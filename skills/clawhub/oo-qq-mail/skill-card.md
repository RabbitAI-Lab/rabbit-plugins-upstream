## Description:

QQ Mail lets agents operate a connected QQ Mail account to read, search, send, reply, forward, move, mark, delete, and download email attachments through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill when an assistant needs to handle QQ Mail tasks through an already connected OOMOL account, including mailbox inspection, message management, and composing or sending email.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that can execute unverified code.

Mitigation: Review and verify the installer source before use, and prefer a signed, versioned, or package-manager installation path for the oo CLI.

Risk: Write and destructive actions can alter or delete QQ Mail messages.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [QQ Mail Skill on ClawHub](https://clawhub.ai/oomol/skills/oo-qq-mail)
- [QQ Mail Homepage](https://mail.qq.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce QQ Mail action payloads and summarize connector JSON responses.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
