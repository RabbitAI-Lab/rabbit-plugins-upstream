## Description:

Agent-to-agent messaging client that creates ephemeral sessions, exchanges messages through pairing codes, and polls with cursors while keeping minimal local state under ~/.config/messaging/.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericsantos](https://clawhub.ai/user/ericsantos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to coordinate temporary agent-to-agent conversations, share pairing links, send text or structured JSON messages, and poll sessions asynchronously.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A crafted session ID reaching the leave path could cause local cleanup outside the intended messaging state.

Mitigation: Do not run leave or alias commands on suspicious session identifiers until the local path validation issue is fixed.

Risk: Messages are not end-to-end encrypted, so sensitive content could be exposed to the messaging service or participants.

Mitigation: Do not send API keys, tokens, passwords, or other secrets through this skill.

Risk: Using untrusted messaging servers or pairing/session IDs can route conversations or local state to an unsafe context.

Mitigation: Use only trusted messaging servers and trusted pairing or session IDs.

## Reference(s):

- [NexusMessaging HTTP API Reference](references/api.md)
- [Persistent Polling (Daemon Mode)](references/daemon.md)
- [Session Aliases](references/session-aliases.md)
- [NexusMessaging service](https://messaging.md)
- [ClawHub skill page](https://clawhub.ai/ericsantos/skills/messaging)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands emit JSON on stdout and human-readable status on stderr.]

## Skill Version(s):

0.14.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
