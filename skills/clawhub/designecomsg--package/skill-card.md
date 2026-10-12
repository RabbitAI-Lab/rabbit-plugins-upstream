## Description:

Send third-party WhatsApp messages or sync/search WhatsApp history via wacli, not normal active chats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[designecomsg](https://clawhub.ai/user/designecomsg)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent send explicitly requested WhatsApp messages to third parties and to sync, search, or backfill WhatsApp history through the wacli CLI. It is not intended for routine active WhatsApp chats routed by OpenClaw.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Linking WhatsApp to OpenClaw exposes local WhatsApp auth/session state and message data to sends, history, media, and channel replies.

Mitigation: Install only when this access is intended, keep auth state local, and configure allowFrom and group policies tightly.

Risk: The wacli installer can resolve a mutable third-party CLI version.

Mitigation: Pin or independently verify the wacli CLI version before using it in a sensitive environment.

Risk: Outgoing WhatsApp messages can be sent to the wrong recipient or with unintended content if a request is ambiguous.

Mitigation: Require an explicit recipient and message text, confirm both before sending, and ask a clarifying question when either is unclear.

Risk: Optional voice-call support expands the integration surface.

Mitigation: Leave optional voice-call support disabled unless it is needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/designecomsg/skills/package)
- [Publisher profile](https://clawhub.ai/user/designecomsg)
- [wacli homepage](https://wacli.sh)
- [wacli Go module install target](https://github.com/steipete/wacli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and CLI arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce machine-readable JSON command variants when the wacli --json option is appropriate.]

## Skill Version(s):

1.0.0 (source: server release evidence; artifact package.json version is 2026.7.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
