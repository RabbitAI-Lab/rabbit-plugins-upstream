## Description:

yotta-present is a local presentation layer for AI agents that classifies an output by content type, selects a presentation form, and renders copyable Markdown or plain text with optional local SVG charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and external agent users use this skill to turn final AI responses, reports, tables, checklists, metrics, Q&A, and chart-ready data into consistent, copyable Markdown or plain-text deliverables. It is also useful when an agent needs a local CLI or MCP presentation layer with platform-specific formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make itself an agent-wide default presentation layer through persistent MCP configuration and memory guidance.

Mitigation: Install only when an agent-wide default renderer is intended, require explicit user consent before persistent writes, and decline MCP or permanent-memory setup for one-off CLI formatting.

Risk: Broad multi-agent installation can change default output behavior across more environments than intended.

Mitigation: Scope installation to the intended agent or directory and avoid global multi-agent installation unless that scope is deliberate.

Risk: Rendered output may be inappropriate for logs, code, sensitive findings, or content where exact wording must be preserved.

Mitigation: Use the documented raw-output exceptions for code, commands, stacks, logs, and exact text, and review rendered output before sharing.

Risk: Unpinned package installation can fetch a newer package than the reviewed release.

Mitigation: Prefer pinned package versions or install from reviewed artifacts when reproducibility matters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [README](README.md)
- [Standard content object schema](references/schema.md)
- [FAQ](references/faq.md)
- [Template definitions](references/templates.json)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-present)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, JSON status output, and optional local SVG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local offline rendering; supports form selection, named templates, platform adaptation, form-choice explanations, and optional length limits.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence; artifact files remain at 0.2.1 and release notes state only skill-card.md was removed)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
