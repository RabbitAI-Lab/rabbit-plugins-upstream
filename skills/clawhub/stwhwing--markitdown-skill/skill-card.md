## Description:

Converts documents and public web pages to Markdown for easier reading, analysis, and knowledge-base use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users convert rich-format documents and public web pages into Markdown before summarizing, extracting information, or adding content to a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Token-saving metadata may be stored locally and posted to a configured receiver.

Mitigation: Set SAVINGS_URL to an empty value, off, none, or disabled to prevent spool and POST behavior.

Risk: Browser fallback and fetching untrusted pages may make additional network requests.

Mitigation: Use --browser-fallback=off for untrusted pages; avoid --allow-internal.

Risk: Optional LLM, Azure, or plugin conversion may expose private document contents to external services.

Mitigation: Do not enable these paths for private documents without explicit approval.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown (upstream conversion library, not publisher provenance)](https://github.com/microsoft/markitdown)
- [Skill security guidance](references/SECURITY.md)
- [Skill usage guide](references/USAGE-GUIDE.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown text or files, with optional token-saving estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Conversion may fetch public web pages or use optional external services; token-saving metadata may be spooled and posted.]

## Skill Version(s):

1.8.8 (source: server-resolved ClawHub release metadata; artifact frontmatter says 1.8.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
