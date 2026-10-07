## Description:

Provides file-based, persistent memory for AI agents, with cross-session recall, semantic search, and access boundaries for shared and private memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to save important information, restore context across sessions, and search locally stored memories while separating shared facts from private preferences and boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent memory can retain sensitive information or credentials.

Mitigation: Review the memory root, enable encryption, and do not store bearer tokens in remembered content.

Risk: Unauthenticated server access can expose memory to other users on the network.

Mitigation: Avoid --no-auth except on trusted local networks.

Risk: Configured provider, model, or embedding commands can execute local processes.

Mitigation: Configure only provider, model, and embedding commands you fully trust.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage (listed in Clawdis metadata)](https://github.com/YottaMeta/yotta-memory)
- [User guide](artifact/USER_GUIDE.md)
- [Memory protocol](artifact/references/protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Text or Markdown memory and context responses; optional structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write persistent local Markdown memory files and return recalled content across sessions.]

## Skill Version(s):

0.22.4 (source: ClawHub release, SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
