## Description:

Generates clean, portable Markdown for normalization, HTML-to-Markdown conversion, linting, table-of-contents generation, and platform-specific publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, technical writers, and documentation maintainers use this skill to convert, normalize, lint, and adapt Markdown or HTML content for platforms such as GitHub, GitLab, Obsidian, Notion, and CommonMark.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command-execution authority broader than its stated Markdown formatting purpose.

Mitigation: Install only if that authority is acceptable, run it in a constrained environment, and review proposed commands before execution.

Risk: The skill references API-key-related capabilities without documenting the exact service, transmitted data, or command allowlist.

Mitigation: Use explicit input files and avoid providing API keys unless the publisher documents the service, data handling, and allowed commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/markdown)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown and JSON with optional inline code blocks and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include normalized Markdown, lint reports, table-of-contents entries, metadata, and platform-specific publishing guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence; artifact frontmatter reports 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
