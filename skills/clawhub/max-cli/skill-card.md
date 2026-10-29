## Description:

Use the `max` CLI to read and send messages in the owner's personal MAX Messenger account or as their bots, and handle related account tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and assistants use this skill to connect to an owner's MAX account or bot, find and read chats, search messages, and perform requested account actions. The skill requires the owner's direct request for consequential actions such as sending, editing, or deleting messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Actions on a real MAX account can affect other people, and some changes such as deletion cannot be undone.

Mitigation: Use read-only access when sufficient; perform consequential actions only on the owner's direct request, confirm the target and content, and use dry-run checks when available.

Risk: Messages and notes may be retained locally, and history downloads can include more conversations than intended.

Mitigation: Limit downloaded history to the chats needed and deliberately choose whether to enable monitoring, auto-replies, or external processing.

Risk: MCP permissions marked `ask` allow the requested action without another server confirmation.

Mitigation: Review the profile's permissions and require an explicit owner request before consequential writes.

## Reference(s):

- [MAX CLI contract](https://github.com/WireCatLabs/max-cli/blob/main/docs/cli-contract.md)
- [Auto-replies guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/replies.md)
- [Message search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/search.md)
- [Topic search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/topic-search.md)
- [Query language guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/query-language.md)
- [Message rankings guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance, CLI commands, and text or JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected MAX command and may include chat, message, or account data.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
