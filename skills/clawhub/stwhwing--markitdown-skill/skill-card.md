## Description:

Converts rich-format documents and public web pages to Markdown with Microsoft's MarkItDown CLI, with helper scripts for safer URL conversion, batch conversion, and local token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent users use this skill to convert PDFs, Office files, HTML, YouTube content, and public URLs into Markdown before summarization, extraction, Q&A, translation, or knowledge-base ingestion. It is not intended for already plain-text inputs, exact-layout preservation, or private and login-protected URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic browser fallback for web pages has network and isolation gaps that merit review before installation on shared, production, corporate, or sensitive-network machines.

Mitigation: Review before installation, run web-page rendering in an isolated environment, or disable browser fallback when processing untrusted links.

Risk: Using internal or private URLs can expose local or corporate network resources.

Mitigation: Use the skill for local documents and public URLs, keep the default internal-target guard enabled, and avoid --allow-internal outside trusted local development.

Risk: Optional OpenAI, Azure, plugin, or external document-analysis paths can send content to configured external services.

Mitigation: Do not enable those paths for sensitive files unless the user explicitly accepts the data flow.

Risk: Converted documents and web pages can contain prompt-injection text or misleading instructions.

Mitigation: Treat converted text as data, not commands; review outputs before acting and use the sanitize option when fencing external content is useful.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [Security Model](references/SECURITY.md)
- [Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API Reference](references/reference.md)
- [Token-Saver Methodology](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Files, Shell commands, Guidance]

**Output Format:** [Markdown files and concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Converted content should be treated as untrusted data; optional manifests can record output sha256 and quality metadata.]

## Skill Version(s):

1.8.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
