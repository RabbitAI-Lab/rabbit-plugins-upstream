## Description:

Send third-party WhatsApp messages or sync/search WhatsApp history via wacli, not normal active chats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ajalao](https://clawhub.ai/user/ajalao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when they need to send WhatsApp messages to third parties, inspect synced messages, or search/backfill WhatsApp history through wacli. It is not intended for routine active WhatsApp chats with the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: wacli can access the user's WhatsApp account and local message history.

Mitigation: Install only after reviewing the upstream wacli project, prefer a pinned or verified release, and use the documented store controls.

Risk: Outgoing WhatsApp messages may be sent to the wrong recipient or with unintended text.

Mitigation: Require explicit recipient and message text, clarify ambiguity, and confirm recipient plus message before sending.

Risk: Synced or backfilled WhatsApp history may be incomplete or best-effort.

Mitigation: Use message inspection commands and verify stored messages when exact formatting or completeness matters.

## Reference(s):

- [wacli homepage](https://wacli.sh)
- [wacli Go module](https://github.com/openclaw/wacli)
- [ClawHub skill page](https://clawhub.ai/ajalao/skills/whatsapp-e)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request clarification or confirmation before proposing outgoing WhatsApp send commands.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
