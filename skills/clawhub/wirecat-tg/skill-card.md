## Description:

Set up Telegram and use the `tg` CLI to find chats or people, read conversations, and send owner-requested messages from the owner's personal account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to set up a personal Telegram account, find chats and people, read conversations, and carry out explicitly requested Telegram actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional MCP connection can perform Telegram changes without enforcing the confirmation implied by an ask permission.

Mitigation: Use the CLI or a read-only MCP profile initially. Before enabling MCP writes, verify that the MCP client requests approval for each change; restrict history downloads to authorized chats and periods, and disable unused administrative capabilities.

## Reference(s):

- [CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [Search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [Topic search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/topic-search.md)
- [Query language guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/query-language.md)
- [Rankings guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown instructions with shell examples and structured CLI or MCP arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change a personal Telegram account according to profile permissions; sends require an explicit owner request.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
