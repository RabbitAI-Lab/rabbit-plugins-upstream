## Description:

Convert documents to Markdown from PDF, Word, Excel, PowerPoint, HTML, CSV, images, and audio with Microsoft MarkItDown for AI and RAG ingestion.

This skill is ready for commercial/non-commercial use.

## Publisher:

[carolz1](https://clawhub.ai/user/carolz1)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge-work agents use this skill to convert local or approved remote documents into structured Markdown for review, extraction, search, knowledge bases, and RAG pipelines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Document conversion can read local files with the current process privileges.

Mitigation: Use narrow APIs, validate paths against an approved root, skip symlinks unless explicitly required, and run with least privilege.

Risk: Remote URI conversion can expose services to SSRF, redirects, oversized responses, or private-network access.

Mitigation: Fetch remote content through an application-controlled downloader with scheme, host, redirect, timeout, size, MIME, and TLS controls, then pass the validated response to conversion.

Risk: OCR, audio transcription, Azure analysis, YouTube, and LLM image description can send document content outside the process.

Mitigation: Require explicit approval before external processing, use approved providers and regions, and prefer local parsing for private or regulated content.

Risk: Plugins execute Python in the same process and can access files, network, environment, and credentials.

Mitigation: Keep plugins disabled by default; pin, review, and sandbox any plugin that is needed for a specific conversion.

Risk: Converted Markdown can preserve prompt injection, misleading links, hidden text, or inaccurate extraction artifacts.

Mitigation: Treat converted Markdown as untrusted source data, separate it from instructions, preserve source provenance, and compare important outputs against the original document.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/carolz1/skills/markitdown)
- [Server-resolved source repository](https://github.com/CarolZ1/markitdown)
- [Microsoft MarkItDown project](https://github.com/microsoft/markitdown)
- [Microsoft MarkItDown on PyPI](https://pypi.org/project/markitdown/)
- [API reference](references/api_reference.md)
- [File formats and conversion behavior](references/file_formats.md)
- [Security and privacy](references/security.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell and Python code blocks; converted document outputs are Markdown files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include batch conversion manifests and degraded-output notes when full MarkItDown conversion is unavailable.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
