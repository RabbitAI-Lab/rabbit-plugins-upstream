## Description:

Converts documents and public web pages to Markdown for reading, analysis, and knowledge-base use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users convert rich-format files or public web pages to Markdown before summarizing, extracting information, or adding content to a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional reporting can share source names and local working-directory or command metadata with a configured receiver.

Mitigation: Leave SAVINGS_URL unset unless the receiver is trusted and that metadata may be shared.

Risk: Browser rendering of untrusted pages can cause unwanted local-network side effects.

Mitigation: Use --browser-fallback=off for untrusted pages when those side effects are unacceptable.

Risk: Internal URL access and optional plugins or external AI processing can expose private content.

Mitigation: Avoid --allow-internal, plugins, LLM image description, and Azure processing for private or regulated content unless explicitly approved.

## Reference(s):

- [MarkItDown skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown (upstream conversion library)](https://github.com/microsoft/markitdown)
- [Usage guide](artifact/references/USAGE-GUIDE.md)
- [Security guidance](artifact/references/SECURITY.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Guidance]

**Output Format:** [Markdown files or text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional batch conversion and local token-savings estimates.]

## Skill Version(s):

1.8.10 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
