## Description:

MarkItDown converts user-supplied documents and public web pages into Markdown using Microsoft's MarkItDown CLI, with helper utilities for URL conversion, batch conversion, and token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, employees, and external agent users use this skill to turn files and public web links into Markdown before analysis, summarization, extraction, translation, Q&A, or knowledge-base preparation. It is especially useful when rich documents or web pages should be reduced to cleaner text before being passed to an AI agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The web-page converter can fetch attacker-controlled URLs and has weak SSRF protection.

Mitigation: Process only user-supplied public HTTP or HTTPS URLs, avoid internal, private, authenticated, or sensitive targets, and do not enable internal-target overrides except for trusted local development.

Risk: The web-page converter may run a local headless browser on untrusted pages.

Mitigation: Prefer no-browser conversion for untrusted pages, and run browser fallback only in an isolated environment where page code cannot access sensitive local state.

Risk: Optional LLM, Azure Document Intelligence, or plugin features can send document content to external services.

Mitigation: Keep optional external features disabled for sensitive content unless the user explicitly consents to the destination and data flow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown upstream project](https://github.com/microsoft/markitdown)
- [MarkItDown API Reference](references/reference.md)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text or files, with inline shell command examples and optional token estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Core local conversion produces Markdown; URL conversion fetches public pages, may use a local browser fallback, and optional LLM, Azure, or plugin features require explicit user consent.]

## Skill Version(s):

1.7.1 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
