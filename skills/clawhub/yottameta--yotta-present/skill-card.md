## Description:

元呈 yotta-present formats agent output into copyable Markdown, plain text, and optional local SVG presentations such as conclusion cards, tables, reports, metric boards, QA cards, and charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this skill to turn final AI outputs into structured, readable, copyable presentations while preserving content shape and degrading to safer forms when a requested layout cannot retain the source content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-use setup can persist an MCP server entry and memory guardrail if the user approves it.

Mitigation: Review the exact mcpServers and memory changes before approval; decline setup and use the CLI fallback if persistent changes are not wanted.

Risk: Unpinned package installation can resolve to a newer or unexpected package version.

Mitigation: Use a pinned or otherwise verified package source where possible.

Risk: Using the skill as the default presentation layer can alter how final answers are formatted.

Mitigation: Install it only when a default output-presentation layer is desired, and keep raw output paths for code, logs, traces, or other content that must remain byte-faithful.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [Project homepage](https://github.com/YottaMeta/yotta-present)
- [Schema reference](references/schema.md)
- [FAQ](references/faq.md)
- [Templates](references/templates.json)
- [Theme tokens](references/theme.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, plain text, JSON metadata, and optional local SVG output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local formatter with optional MCP setup; chart output can be embedded as Markdown data URI or written as a local SVG.]

## Skill Version(s):

0.6.4 (source: SKILL.md frontmatter, package.json, skill-manifest.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
