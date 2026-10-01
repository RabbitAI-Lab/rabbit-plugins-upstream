## Description:

Formats agent output as copyable Markdown or plain text, with optional locally generated SVG charts and cards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users use this skill to present conclusions, tables, reports, and charts in a consistent, copyable format across chat platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Making this the default presentation layer can persistently change how an agent responds.

Mitigation: Enable it only if desired, and review proposed MCP server or permanent-memory changes before approving them.

Risk: An unpinned or broad multi-agent installation can expand the impact of future changes.

Mitigation: Prefer a pinned release in security-sensitive settings and limit installation to intended agents.

## Reference(s):

- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-present)
- [Project homepage](https://github.com/YottaMeta/yotta-present)
- [Content schema](artifact/references/schema.md)
- [Usage FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [Markdown, Plain text, SVG files]

**Output Format:** [Copyable Markdown or plain text; optional local SVG charts or cards]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Adapts presentation to the target chat platform; can report content-fidelity fallbacks.]

## Skill Version(s):

0.7.0 (source: ClawHub release metadata, SKILL.md, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
