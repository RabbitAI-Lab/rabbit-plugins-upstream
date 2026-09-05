## Description:

元呈 yotta-present is a presentation layer for AI agents that classifies an output, selects a form such as a conclusion card, table, checklist, prose, metrics board, QA card, report, or chart, and renders copyable Markdown or plain text with optional local SVG output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gon-kvs](https://clawhub.ai/user/gon-kvs)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI-agent users use this skill to standardize final responses into reusable presentation formats across web chat, plain text, Discord, WhatsApp, CLI, and MCP workflows. It is useful when an agent needs consistent Markdown, plain text, JSON, or local SVG presentation output without changing the underlying content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional setup can write MCP configuration or permanent memory, which may make the formatter broadly available across future agent sessions.

Mitigation: Require explicit user consent before any persistent write, prefer scoped installation over global mode, and verify the written configuration after setup.

Risk: Installing through npx can pull a package version that has not been reviewed in the local environment.

Mitigation: Pin or review the npm package version before installation when supply-chain control is required.

Risk: A broad default presentation layer can alter how final answers are formatted and perceived.

Mitigation: Use the documented bypass cases for raw code, logs, very long output, or user-requested plain text, and review formatted output before using it in sensitive contexts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gon-kvs/skills/yotta-present)
- [GitHub Repository](https://github.com/YottaMeta/yotta-present)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-present)
- [FAQ](references/faq.md)
- [Standard Content Object Schema](references/schema.md)
- [Named Presentation Templates](references/templates.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown, plain text, JSON, and optional local SVG files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports platform-specific rendering, named templates, form selection, length limits, and optional MCP or CLI execution.]

## Skill Version(s):

0.3.0 (source: frontmatter, package.json, CHANGELOG, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
