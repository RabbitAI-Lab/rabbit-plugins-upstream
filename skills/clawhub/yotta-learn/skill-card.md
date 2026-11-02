## Description:

A cross-agent knowledge-base skill that helps agents capture reusable methods as reviewed entries and retrieve them across sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to record verified, cross-project methods in a categorized knowledge base and search those entries in later sessions. It also provides CLI and MCP setup guidance for sharing the library across agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Privacy checks can be bypassed, allowing sensitive content to enter a shared knowledge library.

Mitigation: Use manually redacted content, including drafts and later edits, and share the library only with trusted agents.

Risk: First-run setup can make persistent changes to global memory, MCP, or hook settings.

Mitigation: Require a preview and explicit opt-in before applying these changes.

Risk: Installer upgrades and integrations may be difficult to fully reverse.

Mitigation: Pin the installer version and keep backups before migration; removing the skill alone does not undo integrations or erase stored copies.

## Reference(s):

- [Knowledge base guide](references/kb.md)
- [Frequently asked questions](references/faq.md)
- [Usage walkthroughs](references/walkthroughs.md)
- [Project homepage](https://github.com/YottaMeta/yotta-learn)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-learn)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-learn)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Knowledge-base files]

**Output Format:** [Markdown knowledge entries, CLI commands, and MCP configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Entries can be categorized and marked as draft, verified, or deprecated.]

## Skill Version(s):

0.6.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
