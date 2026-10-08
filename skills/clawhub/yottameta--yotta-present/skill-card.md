## Description:

Formats agent responses as copyable cards, tables, reports, charts, and prose adapted for different messaging platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to present AI responses as readable, reusable Markdown or plain text, with optional local SVG visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-use setup can persistently change the agent's MCP configuration and memory, affecting future responses.

Mitigation: Review the proposed MCP server entry and memory rule, require explicit approval for each persistent change, and decline the memory rule if future-session formatting is unwanted.

Risk: Unpinned package commands may install code that differs from the reviewed release.

Mitigation: Use a pinned package version or a reviewed local checkout instead of unpinned npx commands.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/yottameta/skills/yotta-present)
- [Project homepage (listed in skill metadata)](https://github.com/YottaMeta/yotta-present)
- [Content schema](references/schema.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, SVG]

**Output Format:** [Platform-adapted Markdown or plain text, with optional local SVG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Formats existing content; does not perform data analysis or change conclusions.]

## Skill Version(s):

0.7.1 (source: server release, skill frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
