## Description:

Classifies an agent’s content and renders it as copyable Markdown or plain text, with optional local SVG charts and cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent builders use it to format conclusions, tables, checklists, reports, and charts for chat or document delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chart output can overwrite files outside the selected output folder.

Mitigation: Require output-path containment, reject destinations supplied by content, and prevent overwrites; until these controls are confirmed, run the skill in a sandbox without access to important files.

Risk: First-use setup can write persistent MCP configuration and memory.

Mitigation: Get explicit user consent before either persistent write; if consent is declined, use the local CLI.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-present)
- [Project homepage](https://github.com/YottaMeta/yotta-present)

## Skill Output:

**Output Type(s):** [Markdown, Plain text, SVG graphics]

**Output Format:** [Copyable Markdown or plain text, with optional local SVG]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-adapted formatting; optional SVG output and length limits.]

## Skill Version(s):

0.7.2 (source: frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
