## Description:

yotta-present helps agents classify final outputs by content type, choose a presentation form, and render copyable Markdown or plain text with optional local SVG charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to standardize final AI responses into readable, reusable presentation forms such as conclusion cards, tables, prose, reports, and charts. It is intended for local/offline formatting and presentation, not for changing the underlying content or making judgments for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags the skill as suspicious because it asks to become a broad default presentation layer for future agent outputs.

Mitigation: Install only when that default formatting behavior is desired, and review the skill before deployment.

Risk: The skill may ask to persist MCP server configuration or permanent memory for cross-session availability.

Mitigation: Decline any request to write mcpServers or permanent memory unless cross-session MCP availability is specifically wanted.

Risk: Installing an unpinned or unreviewed package can expose users to unexpected behavior changes.

Mitigation: Prefer pinned package versions or a reviewed local source when installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [Standard content object schema](references/schema.md)
- [FAQ](references/faq.md)
- [Presentation templates](references/templates.json)
- [Theme tokens](references/theme.json)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-present)
- [Project repository listed by package metadata](https://github.com/YottaMeta/yotta-present)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown or plain text, with optional JSON details and local SVG output for charts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally/offline, supports platform-specific formatting, exposes fallback and fidelity details for content preservation, and can configure an MCP server only with explicit user consent.]

## Skill Version(s):

0.6.0 (source: frontmatter, CHANGELOG released 2026-09-11, package.json, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
