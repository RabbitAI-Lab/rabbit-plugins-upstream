## Description:

MarkItDown helps agents convert documents and public web pages into Markdown using Microsoft's MarkItDown CLI and library, with helpers for SPA and WeChat pages plus local token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent users use this skill to convert user-provided files or public URLs into Markdown before summarization, extraction, translation, Q&A, or knowledge-base ingestion. It is also used to reduce token cost by working with cleaned Markdown instead of raw rich documents or raw HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch user-provided public links and may render some pages in a local browser with browser sandboxing disabled.

Mitigation: Use it only for user-provided public URLs, keep the default internal URL blocking enabled, avoid --allow-internal except for trusted local development, and review converted content before relying on it.

Risk: Optional LLM, Azure Document Intelligence, or plugin features may send document content to external endpoints or allow third-party plugin behavior.

Mitigation: Enable those features only with explicit user consent, avoid sensitive or internal documents, and prefer local MarkItDown conversion for private content.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/markitdown-skill-2)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown API Reference](references/reference.md)
- [Usage Guide](references/USAGE-GUIDE.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [markdown, text, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, plain text, and shell or Python command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Converted Markdown may be written to files; token estimates are approximate and based on a chars/4 heuristic.]

## Skill Version(s):

1.5.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
