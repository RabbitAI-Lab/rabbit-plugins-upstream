## Description:

Set up WhatsApp and read or send messages in the owner's personal account through wa. Use when asked to link or connect WhatsApp, find a WhatsApp chat or person, read a conversation, search messages, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents acting for a WhatsApp account owner use this skill to link WhatsApp, find chats or contacts, read and search stored conversations, and carry out explicitly requested messaging or account and group changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use of the unofficial client may lead to WhatsApp account restrictions.

Mitigation: Use only the owner's account, avoid bulk or unsolicited messages, respect configured rate limits, and stop when WhatsApp or the profile refuses a change.

Risk: Local message history and device keys can expose private account data if the computer is not protected.

Mitigation: Protect the computer that stores the history and keys, and enable background collection only when needed.

Risk: Messages, deletions, group administration, and privacy changes can affect the account and other people.

Mitigation: Review permissions for these actions, make only changes the owner explicitly requested, and do not treat MCP's 'ask' setting as a separate confirmation prompt.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wirecat/skills/wirecat-whatsapp)
- [CLI contract](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/cli-contract.md)
- [Search guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/search.md)
- [Query language guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/query-language.md)
- [MCP guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/mcp.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown guidance with shell commands and structured CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available results depend on the selected WhatsApp operation and the history stored locally.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
