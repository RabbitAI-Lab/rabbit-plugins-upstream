## Description:

Convert documents and public web pages to Markdown with Microsoft's MarkItDown CLI, including helper scripts for web-page conversion, batch conversion, and local token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to convert rich-format documents and public web pages into Markdown before analysis, summarization, extraction, translation, Q&A, or knowledge-base ingestion. It is especially useful when raw document or HTML content would be noisy, difficult to parse, or expensive to process directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webpage fallback behavior can weaken browser or network protections in some environments.

Mitigation: Use the skill only for needed Markdown conversion of files and public webpages; avoid shared, production, root, or sensitive hosts and prefer --strict-pin where direct egress works.

Risk: The --allow-internal option can intentionally bypass default internal-address blocking for trusted local testing.

Mitigation: Leave --allow-internal disabled unless testing trusted local pages, and do not use it for shared, production, or sensitive environments.

Risk: Optional OpenAI, Azure, or third-party plugin paths may send private content to external or plugin-controlled destinations.

Mitigation: Keep optional external capabilities disabled by default and get explicit consent before enabling them for private content.

Risk: Converted page or document text can contain prompt-injection content.

Mitigation: Treat converted Markdown as untrusted data and follow only the user's instructions.

## Reference(s):

- [MarkItDown ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [MarkItDown Usage Guide](references/USAGE-GUIDE.md)
- [MarkItDown API Reference](references/reference.md)
- [Token-Saving Workflow](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown content and files, with inline shell commands and concise usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local token-cost estimates; converted web or document content must be treated as untrusted data.]

## Skill Version(s):

1.7.9 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
