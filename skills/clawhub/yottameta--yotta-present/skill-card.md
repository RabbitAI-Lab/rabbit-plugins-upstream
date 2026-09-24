## Description:

yotta-present is a local presentation layer that helps agents classify AI output into forms such as conclusion cards, tables, reports, prose, and charts, then render copyable Markdown or plain text with optional local SVG.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and external users use yotta-present to standardize final AI responses into readable, copyable presentation forms while preserving source content where possible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create a persistent presentation layer that influences broad categories of future agent output.

Mitigation: Before installation or first use, confirm the exact mcpServers entry and any persistent memory or AGENTS.md text to be written, require explicit user consent, and keep a removal copy.

Risk: Unpinned install commands or package resolution may install code that differs from the reviewed release.

Mitigation: Prefer a pinned package version or reviewed release archive for installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [Source homepage](https://github.com/YottaMeta/yotta-present)
- [Schema reference](references/schema.md)
- [FAQ reference](references/faq.md)
- [Templates reference](references/templates.json)
- [Theme reference](references/theme.json)

## Skill Output:

**Output Type(s):** [Markdown, Text, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Copyable Markdown or plain text, with optional JSON results and local SVG files for charts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and offline; platform, channel, theme, and length options can alter formatting.]

## Skill Version(s):

0.6.5 (source: server release metadata, SKILL.md frontmatter, package.json, skill-manifest.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
