## Description:

Converts documents and web pages to Markdown using Microsoft's MarkItDown CLI, with helper scripts for SPA-capable URL conversion, batch conversion, and optional token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent operators use MarkItDown to convert PDFs, Office files, images, audio/video, HTML pages, YouTube links, and direct URLs into Markdown before summarization, extraction, translation, Q&A, or knowledge-base ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch and render user-provided URLs, including through a local headless browser.

Mitigation: Avoid private or internal links unless the operator controls the network path and output handling.

Risk: Optional Azure, LLM, or plugin paths can share document content with external services or unreviewed plugins.

Mitigation: Require explicit approval for confidential files, keep plugins disabled by default, and review any plugin or cloud endpoint before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/markitdown-skill-2)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API reference](references/reference.md)
- [Token-Saving Methodology](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [markdown, text, shell commands, code, configuration, guidance]

**Output Format:** [Markdown files or Markdown/text guidance with inline shell and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated Markdown may be written to files; token estimates are optional and approximate.]

## Skill Version(s):

1.4.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
