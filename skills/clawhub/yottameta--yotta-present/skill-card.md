## Description:

Yotta Present formats AI agent results by classifying content into presentation forms and rendering copyable Markdown or plain text, with optional local SVG charts through its CLI or MCP tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use yotta-present to standardize final AI responses into copyable cards, tables, reports, prose, QA, metrics, checklists, or charts across web chat, plain text, Discord, and WhatsApp. It is useful when an agent needs consistent presentation without changing the underlying content judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can become a persistent default presentation layer by adding MCP server configuration and permanent memory guidance.

Mitigation: Require explicit user consent before any persistent configuration or memory change; decline those changes for one-off use and use the CLI fallback instead.

Risk: The skill can write rendered output or SVG files to local paths selected by the caller.

Mitigation: Allow output paths only in directories where overwrites are acceptable, and review requested paths before running file-writing commands.

Risk: Presentation formatting can be inappropriate when exact bytes, line breaks, or table spacing must be preserved.

Mitigation: Use the documented exceptions for raw code, commands, logs, stack traces, and explicit bare-text requests.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [Standard content object schema](references/schema.md)
- [FAQ](references/faq.md)
- [Presentation templates](references/templates.json)
- [Theme tokens](references/theme.json)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-present)
- [agentskills.io standard](https://agentskills.io/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text, with optional JSON results and local SVG files for chart output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports platform-specific Markdown/plain-text rendering, named templates, length limits, and optional local SVG chart generation.]

## Skill Version(s):

0.5.0 (source: frontmatter, package.json, changelog released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
