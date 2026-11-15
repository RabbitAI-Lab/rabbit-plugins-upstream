## Description:

Set up Telegram and use tg to find chats or people, read conversations, and send messages from the owner's personal account when asked.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to set up Telegram and, when asked, search chats, read conversations, or send messages from the owner's personal account. It also guides safe use of Telegram's command line and profile permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review marked the skill suspicious because reported capabilities include cross-source search and destructive administration beyond its stated Telegram messaging purpose. The review also notes incomplete scanning.

Mitigation: Review the command scope and limit access to the Telegram tasks needed; account for uncovered components and unresolved references before installing.

## Reference(s):

- [CLI contract](https://github.com/WireCatLabs/tg-cli/blob/main/docs/cli-contract.md)
- [Search documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/search.md)
- [Topic search documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/topic-search.md)
- [Query language documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/query-language.md)
- [Rankings documentation](https://github.com/WireCatLabs/tg-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance and shell commands; task results may be text or structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the requested Telegram task and the selected profile's permissions.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
