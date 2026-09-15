## Description:

Converts documents and public web pages into Markdown with MarkItDown, including helper scripts for URL conversion, batch conversion, and local token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to convert rich-format files and public URLs into Markdown before analysis, summarization, extraction, translation, question answering, or knowledge-base ingestion. It is also useful when estimating the token cost of converted content locally.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The web-page fallback may fetch public URLs and render untrusted JavaScript in a local Chromium process.

Mitigation: Use the skill only where this behavior is acceptable, avoid running it as root, and avoid --allow-internal on shared or sensitive machines.

Risk: Optional LLM, Azure, or plugin paths may send document content outside the local machine.

Mitigation: Enable those paths only after confirming the destination and trustworthiness of the service or plugin source.

Risk: Converted page or document text can contain prompt-injection content.

Mitigation: Treat converted Markdown as untrusted data for analysis, not as instructions to execute.

## Reference(s):

- [ClawHub MarkItDown skill page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [MarkItDown project homepage](https://github.com/microsoft/markitdown)
- [MarkItDown API Reference](references/reference.md)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Markdown, Files, Shell commands, Guidance]

**Output Format:** [Markdown files and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create converted Markdown files and local token estimates; optional external LLM, Azure, and plugin capabilities require explicit consent.]

## Skill Version(s):

1.7.9 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
