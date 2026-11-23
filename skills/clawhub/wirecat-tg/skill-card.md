## Description:

Answer questions from the owner's Telegram history, and read or send messages in their personal account, through tg. Use for any question their chats could answer, even when it does not say Telegram: who said, advised or sent what, a past message, link, file, price or decision. Also to set up Telegram, find a chat or person, read a conversation or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Telegram account owners use this skill to search their chat history for answers, read conversations, and carry out message or account actions when explicitly requested. Agents can return findings with message locators and help owners set up Telegram or find chats and people.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review rates the skill suspicious because it provides broad Telegram access and includes actions beyond the stated purpose; scan coverage is incomplete.

Mitigation: Before installing, consider whether broad data searches and account-management actions are needed, and review behavior not covered by the scan.

Risk: The security review reports weak confirmation boundaries for writes.

Mitigation: Use an MCP client that reliably prompts before writes, and review each proposed Telegram change before it is carried out.

## Reference(s):

- [Tg Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-tg)
- [tg-cli CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [tg-cli search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [tg-cli topic search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/topic-search.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text responses with message locators and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings can include sensitive personal message content; commands may read or modify Telegram account data.]

## Skill Version(s):

1.0.9 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
