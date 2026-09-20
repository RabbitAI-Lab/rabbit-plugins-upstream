## Description:

Formats AI outputs into copyable Markdown or plain text cards, tables, reports, prose, metrics, QA blocks, and optional local SVG charts using a local CLI or MCP tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to turn final AI responses into consistent, copyable presentation formats while preserving content and adapting output for web chat, Discord, WhatsApp, or plain text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent MCP configuration and memory changes could route future agent output through this formatter without the user noticing.

Mitigation: Require explicit user consent before writing mcpServers or permanent memory, verify the exact entries, prefer pinned or reviewed installs, and keep rollback notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [Project homepage](https://github.com/YottaMeta/yotta-present)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-present)
- [Schema reference](references/schema.md)
- [FAQ](references/faq.md)
- [Template definitions](references/templates.json)
- [Theme tokens](references/theme.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, plain text, JSON metadata, and optional local SVG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and offline; may request explicit consent before persistent MCP configuration or memory changes.]

## Skill Version(s):

0.6.3 (source: frontmatter, package.json, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
