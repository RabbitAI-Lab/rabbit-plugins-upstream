## Description:

MarkItDown converts rich documents and public web pages into Markdown using Microsoft's MarkItDown CLI, with helper scripts for web-page conversion, batch conversion, and token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent users use this skill to convert PDFs, Office files, images, audio, YouTube content, HTML, and public URLs into Markdown before analysis, summarization, extraction, translation, Q&A, or knowledge-base ingestion. It is intended for content the user explicitly provides and for public web pages, not private or login-protected URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-based web fallback can reach internal network targets in ways the advertised SSRF protections do not fully cover.

Mitigation: Use the skill only for public URLs and local documents intended for conversion; avoid --allow-internal on shared, cloud, CI, production, or sensitive machines.

Risk: Optional OpenAI, Azure Document Intelligence, or plugin paths can share document content with external services.

Mitigation: Keep optional external capabilities disabled unless the user explicitly consents after being told what content will be sent and where.

Risk: Installing broad conversion dependencies on shared or sensitive hosts can increase operational exposure.

Mitigation: Review before installation, prefer pinned or minimal dependencies, and avoid running browser fallback as root when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown API Reference](references/reference.md)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown text and Markdown files, often accompanied by shell commands and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May estimate token cost locally; optional external OpenAI, Azure, or plugin paths require explicit user consent.]

## Skill Version(s):

1.7.6 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
