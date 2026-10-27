## Description:

Use the `max` CLI to connect to a MAX account or bot, find chats and messages, inspect attachments, and send messages when explicitly requested.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

MAX account owners and developers use this skill to manage conversations and bot interactions from the command line, including finding or reading messages and handling requested account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default MAX search may include private notes and imported Google Drive documents without first confirming those sources.

Mitigation: Keep searches within the chosen MAX profile and chat unless notes or Drive documents are explicitly requested. Start with read-only permissions, and approve history-download limits, background monitoring, and remote changes explicitly.

## Reference(s):

- [max-cli on ClawHub](https://clawhub.ai/wirecat/skills/max-cli)
- [CLI contract](https://github.com/WireCatLabs/max-cli/blob/main/docs/cli-contract.md)
- [Search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/search.md)
- [Query language](https://github.com/WireCatLabs/max-cli/blob/main/docs/query-language.md)
- [Topic search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/topic-search.md)
- [Replies guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/replies.md)
- [Rankings guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
