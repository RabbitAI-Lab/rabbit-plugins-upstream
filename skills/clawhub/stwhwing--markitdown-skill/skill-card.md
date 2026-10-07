## Description:

Converts rich-format documents and public web pages to Markdown for easier reading, analysis, and summarization by an agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users convert documents and public web pages into Markdown before extracting information, answering questions, or adding content to a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default headless-browser fallback may give untrusted pages access to the local network through page sub-resources.

Mitigation: For untrusted links or sensitive networks, use --browser-fallback=off or a network-isolated environment; do not use --allow-internal.

Risk: An HTTP proxy bypasses DNS pinning for fetched pages.

Mitigation: Where direct network access is available, use --strict-pin; otherwise account for the remaining proxy risk.

Risk: Optional OpenAI, Azure, or plugin features may send document content to external services.

Mitigation: Enable these features only after confirming the content may be sent to the selected service.

## Reference(s):

- [MarkItDown skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Microsoft MarkItDown library](https://github.com/microsoft/markitdown)
- [Security model](references/SECURITY.md)
- [Usage guide](references/USAGE-GUIDE.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands]

**Output Format:** [Markdown or plain text with conversion commands as needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Converted content may not preserve exact document layout.]

## Skill Version(s):

1.8.5 (source: ClawHub release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
