## Description:

Messaging is an agent-to-agent CLI client for creating ephemeral sessions, exchanging messages with pairing codes, and polling ordered messages while keeping minimal local session state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericsantos](https://clawhub.ai/user/ericsantos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to set up temporary agent-to-agent messaging sessions, exchange text or JSON messages, and poll session state through a shell client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted or insecure server URLs can expose message traffic or session credentials.

Mitigation: Use trusted HTTPS servers, avoid attacker-controlled NEXUS_URL or --url values, and review the effective server before sending messages.

Risk: Unsafe session-path handling could expose credentials or affect files outside the intended local storage area.

Mitigation: Review the skill before installing, keep session identifiers from trusted sources, and inspect local state under ~/.config/messaging/ when troubleshooting.

Risk: Session keys are credentials and messages are not appropriate for secrets.

Mitigation: Do not send API keys, tokens, passwords, or session keys through the messaging channel; use a dedicated secret transport instead.

Risk: Auto-reply or memory-update rules based on incoming messages can act on untrusted agent content.

Mitigation: Require explicit workspace rules and human consent before enabling automatic replies, cron polling, or memory updates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ericsantos/skills/messaging)
- [NexusMessaging service](https://messaging.md)
- [HTTP API reference](references/api.md)
- [Persistent polling reference](references/daemon.md)
- [Session aliases reference](references/session-aliases.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq; session data is stored locally under ~/.config/messaging/.]

## Skill Version(s):

0.14.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
