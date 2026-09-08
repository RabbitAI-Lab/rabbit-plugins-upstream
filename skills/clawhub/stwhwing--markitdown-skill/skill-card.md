## Description:

Converts documents and public web pages into Markdown using Microsoft's MarkItDown CLI, with helpers for SPA/WeChat page handling, batch conversion, and local token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, engineers, and agent operators use this skill to convert PDFs, Office documents, HTML, YouTube pages, media transcripts, and user-supplied public URLs into Markdown before analysis, summarization, extraction, translation, Q&A, or knowledge-base ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The URL conversion path can fetch and render untrusted public web pages.

Mitigation: Use trusted public URLs, review converted Markdown before relying on it, and avoid using the skill for private, internal, or authenticated pages.

Risk: Internal-network protections may be under-scoped if internal access is explicitly allowed.

Mitigation: Leave the default URL guard enabled and use '--allow-internal' only in a contained local development environment.

Risk: The browser fallback may disable Chromium sandboxing when running as root or after a sandboxed launch failure.

Mitigation: Run the browser fallback as a non-root user with Chromium sandboxing available whenever possible.

Risk: The full unpinned MarkItDown dependency set can increase dependency exposure.

Mitigation: Install a pinned minimal MarkItDown extra set that matches the required file types instead of the full 'all' extra set when practical.

Risk: Optional LLM, Azure Document Intelligence, or plugin features can send document content to external services.

Mitigation: Keep optional external capabilities disabled unless the user has explicitly approved the data flow and destination.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown upstream project](https://github.com/microsoft/markitdown)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API Reference](references/reference.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown files or Markdown-formatted text, with shell/Python command examples and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write converted Markdown files; token estimates are approximate; optional external LLM, Azure, or plugin paths require explicit user consent.]

## Skill Version(s):

1.7.2 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
