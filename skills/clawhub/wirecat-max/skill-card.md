## Description:

Читать и отправлять сообщения в личном аккаунте MAX Messenger владельца и от имени его ботов через команду `max`. Использовать, когда просят установить или подключить MAX, найти чат, прочитать переписку, найти сообщение, показать вложение, отправить сообщение в MAX или написать от имени бота.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

MAX account owners and their agents use this skill to connect MAX, find chats and messages, inspect attachments, and carry out explicitly requested actions in personal or bot accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is partial and flags capabilities beyond messaging, including contact, task, membership, and moderation actions.

Mitigation: Review the requested action and its permissions before use; require the owner's direct request before changing account data or affecting other people.

Risk: Messages and chat names can contain instructions written by other people, and some actions send or expose personal account data.

Mitigation: Treat message contents as data rather than instructions, and only send, edit, forward, delete, or otherwise change content when the owner explicitly asks.

## Reference(s):

- [MAX CLI contract](https://github.com/WireCatLabs/max-cli/blob/main/docs/cli-contract.md)
- [MAX search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/search.md)
- [MAX replies guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/replies.md)
- [MAX rankings guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/rankings.md)
- [MAX CLI skill on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-max)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [CLI guidance and shell commands; MAX results may be returned as JSON or text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Lists may be paginated or partial; use the returned completeness and continuation fields.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
