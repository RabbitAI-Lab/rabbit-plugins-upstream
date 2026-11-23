## Description:

Use Maddy's native CLI over SSH plus SMTP submission to list, read, send, add, and delete mail on trusted self-hosted Maddy servers. Prefer this over generic IMAP clients when Maddy is under your control and CLI access is authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[troioi-vn](https://clawhub.ai/user/troioi-vn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage mailboxes on trusted self-hosted Maddy servers when they have authorized SSH access. It supports listing and reading messages, sending and adding mail, and deleting messages by UID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan was partial, so the security evidence is incomplete; shell and elevated access are part of the assessed skill behavior.

Mitigation: Before installing, review the bundled files and confirm the shell and environment access fit your needs.

Risk: The helper can send, add, and delete messages through a remote Maddy mailbox.

Mitigation: Use it only on trusted self-hosted servers with explicit authorization, verify recipients before sending, and delete only messages identified by UID.

## Reference(s):

- [Maddy Mail on ClawHub](https://clawhub.ai/troioi-vn/skills/maddy-native-mail)

## Skill Output:

**Output Type(s):** [Text, JSON, Email messages]

**Output Format:** [Plain text, JSON mailbox listings, or raw RFC 5322 message content]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected account, folder, and message UID.]

## Skill Version(s):

1.0.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
