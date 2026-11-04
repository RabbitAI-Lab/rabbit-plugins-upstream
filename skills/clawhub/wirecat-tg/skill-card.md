## Description:

Set up Telegram and read or send messages in the owner's personal account through tg. Use when asked to install or connect Telegram, find a chat or person, read a conversation, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and personal Telegram account owners use this skill to set up Telegram access, find and read conversations, and carry out requested messaging or account tasks through the tg CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote Telegram writes may proceed without confirmation unless the MCP client enforces approval for each operation.

Mitigation: Start with a readonly profile and verify that the client requests approval for each write before enabling MCP writes.

Risk: The skill includes powerful personal-account and bot operations, including financial, credential-management, and destructive administration actions.

Mitigation: Keep those permissions disabled unless specifically needed, and allow only the requested operations.

Risk: Broad history downloads or additional data sources and external processing can expose personal message data.

Mitigation: Use bounded history downloads and explicitly approve additional data sources or external processing.

## Reference(s):

- [tg CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [Message search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [Query language guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/query-language.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Text]

**Output Format:** [Plain-language guidance with shell command examples and structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and results depend on the selected Telegram profile and its permissions.]

## Skill Version(s):

1.0.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
