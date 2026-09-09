## Description:

Converts documents and public web pages to Markdown using Microsoft's MarkItDown CLI and helper scripts for URL conversion, batch processing, and token-cost estimation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent users use this skill to convert files or public webpages into Markdown before summarization, extraction, translation, question answering, or knowledge-base ingestion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webpage conversion fetches public URLs and may render pages in a local browser.

Mitigation: Avoid private, internal, authenticated, and sensitive URLs; keep internal-target protections enabled; run the skill in an isolated, unprivileged environment.

Risk: Converted webpage or document text may contain untrusted instructions or misleading content.

Mitigation: Treat converted Markdown as source material for review, not as instructions to execute or obey.

Risk: Optional plugins or external document and image analysis services can change data-flow and dependency risk.

Mitigation: Use pinned dependencies, enable optional external capabilities only with explicit user consent, and use plugins only from trusted sources.

## Reference(s):

- [MarkItDown project](https://github.com/microsoft/markitdown)
- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Usage Guide](references/USAGE-GUIDE.md)
- [API Reference](references/reference.md)
- [Token-Saving Methodology](references/TOKEN-SAVER.md)
- [Token Audit Methodology](references/TOKEN-AUDIT.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and occasional code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write Markdown files; token-cost estimates are approximate; optional external document and image analysis capabilities require explicit user consent.]

## Skill Version(s):

1.7.3 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
