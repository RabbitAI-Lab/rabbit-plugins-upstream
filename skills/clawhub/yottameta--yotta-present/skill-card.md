## Description:

元呈 yotta-present formats agent outputs by classifying content, selecting a presentation form, and rendering copyable Markdown or plain text with optional local SVG charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill as a local presentation layer for final agent responses, converting JSON, Markdown, or plain text into consistent Markdown or plain text while preserving content order and adapting output for different platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks to become a persistent default presentation layer for future agent outputs.

Mitigation: Install it only when that default routing is intended, and decline permanent memory writes or MCP auto-configuration unless comfortable with future responses using this presentation layer.

Risk: The MCP and CLI paths can write rendered output such as Markdown, text, or SVG files.

Mitigation: Use explicit, reviewed output paths and avoid granting arbitrary file-write locations.

Risk: The authoritative security verdict is suspicious because persistent output routing and broad file-write behavior require review before installation.

Mitigation: Review the release before deployment and prefer pinned package versions or reviewed source archives.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [README](README.md)
- [Standard content object schema](references/schema.md)
- [FAQ](references/faq.md)
- [Templates](references/templates.json)
- [Theme tokens](references/theme.json)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-present)

## Skill Output:

**Output Type(s):** [text, markdown, code, files, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text, with optional JSON metadata and local SVG files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local/offline rendering with optional platform, channel, theme, template, max_len, SVG, and explanation controls; JSON output can include fallback and fidelity metadata.]

## Skill Version(s):

0.6.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
