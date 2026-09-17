## Description:

Chat API for WhatsApp helps agents inspect connected WhatsApp account state, read chats and messages, validate configuration, and send text or file messages through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Chat API for WhatsApp through an OOMOL-connected account, including reading settings, status, chats, messages, and outbound queues. It can also prepare schema-checked commands for sending text messages and files after confirming the exact recipient and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can ask users to execute a remotely fetched installer script without verification.

Mitigation: Review the installer path first; prefer a signed or package-manager installation source, or download and verify the installer before running it.

Risk: Message-sending actions can change external WhatsApp state.

Mitigation: Only allow send actions after checking the exact recipient and payload with the user.

## Reference(s):

- [Chat API for WhatsApp homepage](https://chat-api.com/en/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-chat-api-for-whatsapp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before forming action payloads; state-changing message actions require recipient and payload confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
