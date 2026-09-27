## Description:

Formats agent responses as copyable cards, tables, reports, and charts for different messaging platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to present existing answers as readable, copyable Markdown or plain text, with optional local SVG charts. Users can opt out of rendering or keep their own output conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup may make the skill a persistent default for future agent responses and change agent configuration.

Mitigation: Review the exact server configuration and permanent memory text before explicitly approving either change; use the CLI-only mode to avoid persistence.

Risk: An unpinned package launch may run code that changes between uses.

Mitigation: Prefer a pinned package version or reviewed local source in sensitive environments.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-present)
- [Project homepage (listed in ClawHub metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-present)
- [Output schema](references/schema.md)
- [Frequently asked questions](references/faq.md)

## Skill Output:

**Output Type(s):** [Markdown, Plain text, SVG charts]

**Output Format:** [Copyable Markdown or plain text, optionally with a local SVG chart]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Platform-specific formatting; optional JSON reports rendering fallback and content fidelity.]

## Skill Version(s):

0.6.6 (source: SKILL.md frontmatter, CHANGELOG.md, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
