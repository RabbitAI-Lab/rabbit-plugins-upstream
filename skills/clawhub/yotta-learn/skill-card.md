## Description:

Captures agent mistakes, corrections, and insights as reusable learning records and organizes verified knowledge for cross-session search and reuse.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users capture command failures, user corrections, and useful discoveries for later review, and maintain a searchable knowledge base of verified guidance across agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Durable learning records and the shared knowledge base may retain material that should not persist.

Mitigation: Review entries before saving and avoid private or sensitive information unless explicitly requested.

Risk: Optional global hooks can trigger review on every prompt.

Mitigation: Leave global hooks disabled unless that behavior is wanted, and prefer a pinned package version.

Risk: MCP or memory configuration changes can affect how an agent reads and writes stored knowledge.

Mitigation: Review configuration changes before allowing the agent to write them.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-learn)
- [Project homepage](https://github.com/YottaMeta/yotta-learn)
- [Knowledge base reference](references/kb.md)
- [Hook setup reference](references/hooks-setup.md)
- [Learning record examples](references/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown learning records and knowledge-base entries, with text search results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Learning records and knowledge-base entries persist locally for later reuse.]

## Skill Version(s):

0.5.0 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
