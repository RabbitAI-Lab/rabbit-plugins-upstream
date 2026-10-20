## Description:

Provides AI agents with persistent, file-based memory for restoring context across sessions, recording and organizing memories, and retrieving them with type-based access boundaries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent users use it to restore prior context at session start, record facts, preferences, boundaries, and commitments, and retrieve or archive memories across sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verified flaws may expose private memories.

Mitigation: Postpone storing sensitive memories until the flaws are fixed; evaluate with isolated, non-sensitive data using local stdio and core tools.

Risk: Imported records may write outside the intended storage folder.

Mitigation: Avoid untrusted imports and retain an independently verified backup.

Risk: Exposed web-console or remote MCP access may increase data exposure.

Mitigation: Keep the web console on loopback and protect remote MCP traffic with TLS or an encrypted tunnel; do not rely on token scope restrictions or --keep-memories for protection.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown memory files, retrieved context text, and command or configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context content and retained entries depend on the user's memory store and configuration.]

## Skill Version(s):

0.23.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
