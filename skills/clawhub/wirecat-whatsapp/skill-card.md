## Description:

Set up WhatsApp and read or send messages in the owner's personal account through wa. Use when asked to link or connect WhatsApp, find a WhatsApp chat or person, read a conversation, search messages, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an owner's WhatsApp account and find, read, search, or send messages through the wa command line. It also supports requested contact, chat, group, and account management tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the release suspicious because it adds task management, local-note search, and administrative controls beyond messaging; scanner coverage is incomplete.

Mitigation: Review whether these capabilities are needed and inspect the unresolved or obfuscated material before installation; grant only the account permissions required for the task.

Risk: The CLI operates on a real WhatsApp account, and the skill documents account-ban risk from unofficial use, bulk messaging, or unsolicited messages.

Mitigation: Send only messages explicitly requested by the owner, avoid bulk or unsolicited sends, and stop after a rate-limit or permission refusal.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-whatsapp)
- [CLI contract](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/cli-contract.md)
- [Search guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/search.md)
- [Query language guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/query-language.md)
- [MCP guide](https://github.com/WireCatLabs/whatsapp-cli/blob/main/docs/mcp.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Human-readable text and guidance, shell commands, and structured CLI JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies with the requested WhatsApp task and available local chat data.]

## Skill Version(s):

1.0.4 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
