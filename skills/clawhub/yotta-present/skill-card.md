## Description:

Yotta-present is a local presentation layer that helps agents classify final outputs by content type and render them as copyable Markdown, plain text, JSON, or optional SVG charts through a CLI or MCP tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to standardize final agent responses into presentation forms such as conclusion cards, tables, prose, reports, and charts while keeping output copyable and local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to make it a persistent default presentation layer across future sessions by editing MCP configuration and permanent memory.

Mitigation: Install or enable it only when that persistence is desired; prefer manual CLI use or require approval before MCP or permanent-memory edits.

Risk: The global installer can copy the skill into multiple agent environments.

Mitigation: Use an explicit --agent or --dir target unless broad installation across known agents is intentional.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-present)
- [README](README.md)
- [Standard content object schema](references/schema.md)
- [npm package @yottameta/yotta-present](https://www.npmjs.com/package/@yottameta/yotta-present)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, shell commands, guidance]

**Output Format:** [Markdown, plain text, JSON, and optional local SVG.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include form-choice explanations and warnings; chart output may be embedded as a data URI or written as a local SVG file.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
