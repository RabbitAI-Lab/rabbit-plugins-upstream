## Description:

Generates clean, portable Markdown that renders consistently across parsers and supports normalization, HTML-to-Markdown conversion, lint checks, table of contents generation, and target-platform adaptation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, documentation writers, and agent users use this skill to normalize Markdown, convert HTML or plain text into Markdown, generate tables of contents, and adapt documents for GitHub, GitLab, Obsidian, Notion, or CommonMark workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests command execution and describes broad API and file capabilities that are not clearly scoped to Markdown formatting.

Mitigation: Use it only where command execution is disabled or tightly controlled, and review any proposed commands or file writes before running them.

Risk: The skill mentions API key setup even though the security guidance says the publisher has not clarified why API keys are required.

Mitigation: Avoid providing API keys or secrets unless the publisher documents the required service, data flow, and command behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/markdown)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown, JSON lint reports or TOC data, and plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include normalized Markdown, lint findings, generated table-of-contents entries, and document metadata such as word, heading, and table counts.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
