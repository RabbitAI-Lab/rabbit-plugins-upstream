## Description:

yotta-present is a local presentation layer for AI agents that selects an output form and renders final responses as copyable Markdown or plain text, with optional JSON output and local SVG charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to standardize user-facing agent results into readable, reusable formats such as conclusion cards, tables, reports, prose, QA cards, and charts. It is intended for local formatting and presentation, not for content judgment or data analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent setup can make yotta-present a broad default formatting layer for future agent outputs.

Mitigation: Review the exact mcpServers entry and permanent-memory text before approving first-run setup; decline persistence when one-off CLI rendering is sufficient.

Risk: Routing final responses through a presentation layer may be unsuitable when exact raw formatting is required.

Mitigation: Use the documented raw-output exceptions for code, commands, CLI output, stack traces, logs, very long content written with --out, or explicit requests for bare text.

## Reference(s):

- [README](README.md)
- [Standard content object schema](references/schema.md)
- [FAQ and pitfalls](references/faq.md)
- [Named presentation templates](references/templates.json)

## Skill Output:

**Output Type(s):** [markdown, text, JSON, files, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON, and optional local SVG file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local offline rendering with platform adaptation, named templates, optional bolding, and length caps.]

## Skill Version(s):

0.2.1 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
