## Description:

Formats agent output as copyable Markdown or plain text, including conclusion cards, tables, reports, and charts, with optional local SVG and platform-aware rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to choose a presentation form for user-facing content and render it into copyable Markdown or plain text, with optional SVG cards or charts. It supports platform-specific formatting and provides CLI and MCP access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chart input can overwrite local files.

Mitigation: Reject embedded out/filename fields or restrict filesystem writes to an approved output folder.

Risk: Automatic formatting can block or rewrite replies, and host hook enforcement is unverified.

Mitigation: Keep companion rewriting opt-in, review rendered output, and verify host hook behavior before relying on it.

Risk: Installer coverage gaps leave companion behavior unverified.

Mitigation: Use an exact reviewed package version and approve saved settings separately.

## Reference(s):

- [Project homepage (metadata.clawdis)](https://github.com/YottaMeta/yotta-present)
- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-present)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-present)
- [Content object schema](references/schema.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Markdown, Plain text, SVG]

**Output Format:** [Copyable Markdown or plain text, optionally accompanied by a local SVG card or chart]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-aware formatting, content-preservation checks, and configurable length limits]

## Skill Version(s):

0.7.3 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
