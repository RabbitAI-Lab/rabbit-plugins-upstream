## Description:

Set up Telegram and read or send messages in the owner's personal account through tg. Use when asked to install or connect Telegram, find a chat or person, read a conversation, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to guide setup and use of the tg command line interface for an owner's personal Telegram account, including finding chats, reading conversations, and carrying out explicitly requested actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The server security review rates this release suspicious, citing Telegram administration, bot, and task-management capabilities beyond its stated personal messaging purpose; the scan was incomplete.

Mitigation: Review the commands relevant to the task and the selected profile's permissions before use; keep permissions limited and require the owner's explicit request for Telegram writes.

## Reference(s):

- [CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [Search documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [Topic search documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/topic-search.md)
- [Query language documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/query-language.md)
- [Rankings documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command choice and action scope depend on the owner's request and the selected profile's permissions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
