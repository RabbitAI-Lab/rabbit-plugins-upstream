## Description:

Set up WhatsApp and read or send messages in the owner's personal account through wa. Use when asked to link or connect WhatsApp, find a WhatsApp chat or person, read a conversation, search messages, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

WhatsApp account owners and their agents use this skill to link an account, find chats and contacts, read or search stored conversations, and carry out explicitly requested messaging and account-management actions through the wa CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The unofficial client can put the linked WhatsApp account at risk of a ban, especially through bulk or unsolicited messages.

Mitigation: Send only messages the owner explicitly requested, avoid bulk sends and unfamiliar recipients, and stop when WhatsApp or the CLI refuses or rate-limits a write.

Risk: The skill can send messages and change groups, privacy settings, and other account data, while retaining chats and device keys locally.

Mitigation: Restrict unused write permissions, require approval in the MCP client (an 'ask' permission alone does not provide a confirmation dialog), and enable background collection only when wanted.

## Reference(s):

- [CLI contract](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/cli-contract.md)
- [Search guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/search.md)
- [Query language guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/query-language.md)
- [MCP guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/mcp.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with CLI commands and command responses in JSON or JSONL]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command output varies by requested action and locally stored conversation history.]

## Skill Version(s):

1.0.3 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
