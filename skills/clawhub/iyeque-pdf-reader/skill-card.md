## Description:

Extracts text, searches for terms, and inspects metadata in local PDF files for agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can read reports, locate evidence by searching PDF pages, and retrieve document metadata for summaries and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Processing large or untrusted PDFs can be resource-intensive.

Mitigation: Use --max_pages to limit how many pages the agent reads.

Risk: PDF passwords entered in shell commands can appear in history or logs.

Mitigation: Avoid placing PDF passwords in command arguments.

## Reference(s):

- [pdf-reader on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-pdf-reader)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns extracted text and pages read, search matches with page context, or PDF metadata; errors are returned as JSON.]

## Skill Version(s):

1.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
