## Description:

Set up Telegram and read or send messages in the owner's personal account through tg. Use when asked to install or connect Telegram, find a chat or person, read a conversation, or send a message.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use this skill to set up Telegram and, when asked, find and read conversations or send messages from the owner's personal account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scan flags a broader scope than personal-account messaging, including private-data searches and administrative or bot-management features.

Mitigation: Review the skill and package capabilities before installation, and grant only the Telegram profile permissions needed for the task. Keep writes behind the owner's explicit request and approval.

Risk: The security scan has partial coverage and does not establish that unreported behavior is safe.

Mitigation: Treat the scan as incomplete and review the full skill and package before installation; do not rely on unreported behavior being safe.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wirecat/skills/wirecat-tg)
- [tg CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [Message search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [Topic search guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/topic-search.md)
- [Query language guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/query-language.md)
- [Statistics and rankings guide](https://github.com/WireCatLabs/tg-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command schemas]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by task; commands may read or change data in the owner's Telegram account.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
