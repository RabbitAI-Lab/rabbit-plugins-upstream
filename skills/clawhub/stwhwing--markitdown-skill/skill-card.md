## Description:

Converts documents and public web pages to Markdown for reading, analysis, and knowledge-base workflows, with optional token-savings estimates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users convert rich-format files and public webpages to Markdown before summarizing, extracting information, or adding content to a knowledge base.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted pages rendered in a browser may request private-network resources.

Mitigation: Use --browser-fallback=off for untrusted pages when private-network access is unacceptable; do not use --allow-internal outside trusted local development.

Risk: Optional token-savings reporting can disclose source URLs, filenames, and local caller context.

Mitigation: Leave SAVINGS_URL unset unless you intend to send reports to a receiver you control; review its destination before processing sensitive material.

Risk: Converted documents and pages may contain instructions intended to redirect the agent.

Mitigation: Treat converted content as untrusted data, not instructions to execute.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/stwhwing/skills/markitdown-skill)
- [Usage guide](artifact/references/USAGE-GUIDE.md)
- [Security model](artifact/references/SECURITY.md)
- [Microsoft MarkItDown (upstream dependency)](https://github.com/microsoft/markitdown)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Guidance]

**Output Format:** [Markdown or plain text, with optional conversion commands and token-savings estimates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Web conversion can save Markdown files; optional reports require explicit configuration.]

## Skill Version(s):

1.8.9 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
