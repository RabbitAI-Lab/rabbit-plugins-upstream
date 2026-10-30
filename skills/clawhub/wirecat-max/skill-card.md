## Description:

Читать и отправлять сообщения в личном аккаунте MAX Messenger владельца и от имени его ботов через команду `max`.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wirecat](https://clawhub.ai/user/wirecat)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to set up MAX and work with the owner's personal account or bots: find chats and messages, read conversations, inspect attachments, and carry out explicitly requested actions. The instructions emphasize limiting account access and keeping actions that affect other people under the owner's control.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill accesses the owner's real MAX account and can retain local message copies and notes, exposing sensitive conversation data.

Mitigation: Begin with read-only permissions, select specific chats and history limits, and enable monitoring, broader searches, or external AI only when needed. Keep message text out of logs and files.

Risk: Sending messages or other account changes can affect people outside the owner's device; bot writes may be allowed by default.

Mitigation: Carry out writes only when the owner explicitly requests the specific action, recipient, and content; check bot permissions and scopes before enabling writes.

## Reference(s):

- [Max Cli on ClawHub](https://clawhub.ai/wirecat/skills/wirecat-max)
- [CLI contract](https://github.com/WireCatLabs/max-cli/blob/main/docs/cli-contract.md)
- [Replies guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/replies.md)
- [Search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/search.md)
- [Topic search guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/topic-search.md)
- [Query language guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/query-language.md)
- [Rankings guide](https://github.com/WireCatLabs/max-cli/blob/main/docs/rankings.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance, shell commands, and CLI text or JSON/JSONL results when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI output may be limited to selected fields; message text should be reported only to the owner.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
