## Description:

Set up Telegram and read or send messages in the owner's personal account through tg. Use when asked to install or connect Telegram, find a chat or person, read a conversation, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Telegram account owners and their agents use this skill to set up access, find and read conversations, and perform explicitly requested messaging and account tasks through the tg CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default searches can include private sources beyond Telegram, such as local notes or imported Drive documents.

Mitigation: Set permitted chats and history limits, decide whether notes and Drive documents are in scope, and use the archive backend for local Telegram-only searches.

Risk: The MCP interface can perform writes without providing its own confirmation prompt.

Mitigation: Use readonly or deny permissions where possible, configure the MCP client to approve writes, and leave administrative, financial, and token-management operations disabled unless needed.

## Reference(s):

- [Tg Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-tg)
- [CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [Search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [Query language](https://github.com/WireCatLabs/tg-cli/blob/main/docs/query-language.md)
- [Rankings guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON command descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account actions follow the selected profile's permissions and the skill's explicit-action safeguards.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
