## Description:

Converts documents and web pages into Markdown with Microsoft's MarkItDown CLI, including utilities for JavaScript-rendered pages, WeChat articles, batch conversion, and token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to convert PDFs, Office files, images, audio, HTML, YouTube links, and webpages into Markdown before analysis, summarization, extraction, translation, or Q&A. It is especially suited for reducing token usage when working with large or richly formatted inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic processing of external URLs or documents can expose private or internal content.

Mitigation: Require user confirmation before fetching external URLs, avoid internal or private links, and process only content approved for the environment.

Risk: Headless browser fallback can execute untrusted webpage code during conversion.

Mitigation: Do not run browser fallback for untrusted sites in sensitive environments; use isolated execution when browser rendering is necessary.

Risk: Optional cloud, LLM, Azure Document Intelligence, or plugin features may send content to external services.

Mitigation: Use those options only for non-sensitive content or after explicit data-handling approval.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/stwhwing/markitdown-skill)
- [ClawHub skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill-2)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API Reference](references/reference.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown files and prose guidance with command and Python snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write converted Markdown files and print token-cost estimates; requires Python and the markitdown CLI, with optional browser and OCR dependencies for some inputs.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter version: 1.4.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
