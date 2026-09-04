## Description:

Converts documents and public web pages to Markdown with Microsoft's MarkItDown CLI, including PDFs, Office files, images with OCR, audio or video transcripts, HTML, YouTube pages, and direct URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to convert files and public web pages into Markdown before analysis, summarization, extraction, translation, Q&A, or knowledge-base ingestion. It is especially useful for reducing context size when working with large or richly formatted sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically fetch web pages and render them in an unsandboxed headless browser.

Mitigation: Use it only for files and public URLs the user intends to fetch, keep internal URL blocking enabled, avoid --allow-internal except for trusted local development, and prefer --no-browser or an isolated environment for untrusted pages.

Risk: Optional LLM, Azure Document Intelligence, or plugin features can send document content to external services or introduce third-party plugin behavior.

Mitigation: Do not enable --llm-model, Azure Document Intelligence, or plugins for private documents unless the user explicitly accepts that data flow; prefer local MarkItDown conversion for sensitive content.

Risk: Conversion fidelity can vary for complex layouts, images, audio, video, or JavaScript-rendered pages.

Mitigation: Review converted Markdown against the source for fidelity-critical tasks and install only the needed optional dependencies such as Tesseract, a browser, or media transcription backends.

## Reference(s):

- [MarkItDown API Reference](references/reference.md)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown on PyPI](https://pypi.org/project/markitdown/)
- [Azure AI Document Intelligence](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown files or Markdown/text responses, with shell command and Python code snippets for conversion workflows.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write converted Markdown files; token estimates are approximate and use a chars/4 heuristic.]

## Skill Version(s):

1.5.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
