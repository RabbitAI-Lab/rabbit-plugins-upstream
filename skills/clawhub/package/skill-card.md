## Description:

Send third-party WhatsApp messages or sync/search WhatsApp history via wacli, not normal active chats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[designecomsg](https://clawhub.ai/user/designecomsg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users use this release to connect WhatsApp Web chats to agents and, through the bundled wacli skill guidance, send third-party WhatsApp messages or search and sync WhatsApp history when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release can operate as a full WhatsApp channel that observes inbound chats and sends replies, broader than the wacli helper framing.

Mitigation: Install it only when a full WhatsApp channel is intended, review chat access policies before enabling it, and keep messageReceived hooks disabled unless needed.

Risk: Linked WhatsApp accounts may expose message content or media metadata to local processing or logs.

Mitigation: Use a separate WhatsApp number where possible and configure dmPolicy, groupPolicy, and allowFrom to limit who agents can monitor or reply to.

## Reference(s):

- [wacli homepage](https://wacli.sh)
- [ClawHub skill page](https://clawhub.ai/designecomsg/skills/package)
- [Publisher profile](https://clawhub.ai/user/designecomsg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the wacli binary and a linked WhatsApp account for operational commands.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact package.json reports 2026.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
