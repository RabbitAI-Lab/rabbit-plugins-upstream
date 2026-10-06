## Description:

Reads PDFs for bounded text extraction, full-text search, and metadata inspection in agent workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other agent users can extract text, search for evidence, and inspect metadata in PDFs to support document review and summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: PDF contents supplied to the agent may be returned in chat or a workflow.

Mitigation: Only provide PDFs whose contents may be shared with the agent and the intended output destination.

Risk: Passwords supplied in command arguments may appear in shell history or logs.

Mitigation: Do not pass PDF passwords on the command line.

## Reference(s):

- [PDF Reader on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-pdf-reader)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured JSON containing extracted text, search matches, or PDF metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Extraction and search read up to 500 pages per request by default; a smaller page limit can be selected.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
