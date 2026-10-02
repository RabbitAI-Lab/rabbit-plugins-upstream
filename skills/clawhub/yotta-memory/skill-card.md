## Description:

Helps AI agents preserve and retrieve local, permission-aware memories across sessions, with searchable context and rollback support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to retain task context, preferences, boundaries, and commitments between sessions and retrieve relevant memories when work resumes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-term memories may retain sensitive information or access secrets.

Mitigation: Avoid storing bearer tokens or agent keys in memories; keep them in a key file or secret store and review retained content.

Risk: MCP access and optional providers or LAN services can extend access to stored memories.

Mitigation: Enable only the integrations needed, review their configuration and access boundaries, and use pinned npm versions for installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage (listed in release metadata)](https://github.com/YottaMeta/yotta-memory)
- [User guide](USER_GUIDE.md)
- [Memory protocol](references/protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions]

**Output Format:** [Text and Markdown, including locally stored memory files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Persists local memories for reuse across sessions.]

## Skill Version(s):

0.21.1 (source: ClawHub release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
